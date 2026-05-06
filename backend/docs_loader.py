import os

DOCS_PATH = "docs"


def load_docs():

    documents = []

    for root, dirs, files in os.walk(DOCS_PATH):

        for file in files:

            if file.endswith(".md"):

                path = os.path.join(root, file)

                try:

                    with open(path, "r", encoding="utf-8") as f:

                        text = f.read()

                    relative_path = path.replace("docs\\", "").replace("\\", "/")

                    page_link = f"https://ajinanga16-blip.github.io/tech-writer-portfolio/{relative_path.replace('index.md', '')}"

                    documents.append({
                        "path": relative_path,
                        "link": page_link,
                        "content": text
                    })

                except:
                    pass

    return documents