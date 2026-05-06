from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware
from backend.docs_loader import load_docs

app = FastAPI()

client = OpenAI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load documentation
DOCUMENTS = load_docs()

print("✅ Documentation loaded")


class Question(BaseModel):
    question: str


@app.post("/ask")
def ask_question(data: Question):

    docs_text = ""

    for doc in DOCUMENTS:

        docs_text += f"""

SECTION:
{doc['path']}

LINK:
{doc['link']}

CONTENT:
{doc['content']}

-------------------------
"""

    prompt = f"""
You are an AI Documentation Assistant for a Technical Writing portfolio website.

Your responsibilities:
- Answer ONLY using the provided documentation
- Structure responses clearly
- Use headings and bullet points
- Keep responses concise
- Mention the most relevant documentation section
- ALWAYS include documentation source links

If answer is unavailable, say:
'I could not find this information in the documentation.'

RESPONSE FORMAT:

### Answer

Brief explanation.

#### Key Details
- Point 1
- Point 2
- Point 3

#### Source
[Section Name](Full documentation link)

DOCUMENTATION:
{docs_text}

QUESTION:
{data.question}
"""

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    return {"answer": answer}