import os
import re
import subprocess
import requests
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

BASE_PATH = "docs/user-guides"
NAV_FILE = "mkdocs.yml"

# Load environment variables
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_BASE = os.getenv("JIRA_BASE_URL")


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def fetch_jira_ticket(ticket_id):
    if not JIRA_BASE:
        raise Exception("❌ JIRA_BASE_URL is not set")

    url = f"{JIRA_BASE}/rest/api/3/issue/{ticket_id}"

    print(f"📡 Calling JIRA API: {url}")

    response = requests.get(
        url,
        auth=(JIRA_EMAIL, JIRA_TOKEN),
        headers={"Accept": "application/json"}
    )

    print(f"📊 JIRA response status: {response.status_code}")

    if response.status_code != 200:
        raise Exception(f"❌ JIRA fetch failed:\n{response.text}")

    data = response.json()

    title = data["fields"]["summary"]

    # JIRA description can be complex (ADF), convert safely
    description = str(data["fields"]["description"])

    return title, description


def generate_content(title, jira_content):
    prompt = f"""
You are a senior technical writer.

Convert the following JIRA ticket into a user guide.

JIRA DETAILS:
{jira_content}

Follow structure:
Overview
Who should use this
Prerequisites
Steps
Tips and best practices
Troubleshooting

Output ONLY Markdown.
"""

    print("🤖 Sending request to OpenAI...")

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def update_nav(title, slug):
    entry = f"    - {title}: user-guides/{slug}/index.md\n"

    with open(NAV_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    inserted = False

    for line in lines:
        new_lines.append(line)

        if line.strip() == "- User Guides:" and not inserted:
            new_lines.append(entry)
            inserted = True

    with open(NAV_FILE, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


def run(cmd):
    print(f"\n▶ {cmd}")
    subprocess.run(cmd, shell=True)


def main():
    print("\n=== JIRA → GPT → DOCS PIPELINE ===\n")

    print("DEBUG:")
    print("JIRA_BASE =", JIRA_BASE)
    print("JIRA_EMAIL =", JIRA_EMAIL)
    print("JIRA_TOKEN =", "SET" if JIRA_TOKEN else "NOT SET")

    ticket_id = input("\nEnter JIRA Ticket ID (e.g., SCRUM-1): ").strip()

    print("\n📥 Fetching JIRA ticket...")
    title, description = fetch_jira_ticket(ticket_id)

    print(f"✅ Title fetched: {title}")

    slug = slugify(title)

    folder = os.path.join(BASE_PATH, slug)
    file_path = os.path.join(folder, "index.md")

    if os.path.exists(folder):
        print("❌ Guide already exists.")
        return

    print("\n🤖 Generating documentation...")
    content = generate_content(title, description)

    os.makedirs(folder)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ File created")

    update_nav(title, slug)
    print("✅ Navigation updated")

    run("git add .")
    run(f'git commit -m "Auto-generated from JIRA: {ticket_id}"')
    run("git push origin master")
    run("py -m mkdocs gh-deploy --force")

    print("\n🎉 FULL PIPELINE COMPLETE")


if __name__ == "__main__":
    main()