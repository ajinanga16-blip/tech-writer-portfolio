import os
import re
import subprocess
from openai import OpenAI

# Initialize OpenAI client (uses your environment variable)
client = OpenAI()

BASE_PATH = "docs/user-guides"
NAV_FILE = "mkdocs.yml"


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def generate_content(title):
    prompt = f"""
You are a senior technical writer.

Follow these rules strictly:
- Use clear, concise language
- Follow this exact structure:
  Overview
  Who should use this
  Prerequisites
  Steps
  Tips and best practices
  Troubleshooting

- Output ONLY valid Markdown
- Do not add explanations

Create a user guide for:

Feature: {title}
User: Financial Analyst
"""

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
    inside_section = False
    inserted = False

    for line in lines:
        new_lines.append(line)

        if line.strip() == "- User Guides:":
            inside_section = True
            continue

        if inside_section:
            if line.startswith("    - "):
                continue
            else:
                if not inserted:
                    new_lines.insert(len(new_lines)-1, entry)
                    inserted = True
                inside_section = False

    if not inserted:
        new_lines.append(entry)

    with open(NAV_FILE, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


def run_command(cmd):
    print(f"\n▶ Running: {cmd}")
    subprocess.run(cmd, shell=True)


def main():
    print("\n=== FULLY AUTOMATED DOCS PIPELINE ===\n")

    title = input("Enter feature title: ").strip()
    slug = slugify(title)

    folder_path = os.path.join(BASE_PATH, slug)
    file_path = os.path.join(folder_path, "index.md")

    if os.path.exists(folder_path):
        print("❌ Guide already exists. Use a different title.")
        return

    print("🤖 Generating content from GPT...")
    content = generate_content(title)

    os.makedirs(folder_path)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ File created: {file_path}")

    update_nav(title, slug)
    print("✅ Navigation updated")

    run_command("git add .")
    run_command(f'git commit -m "Auto-generated guide: {title}"')
    run_command("git push origin master")
    run_command("py -m mkdocs gh-deploy --force")

    print("\n🎉 FULL AUTOMATION COMPLETE")


if __name__ == "__main__":
    main()