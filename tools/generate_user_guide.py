import os
import re
import subprocess

BASE_PATH = "docs/user-guides"
NAV_FILE = "mkdocs.yml"

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def update_nav(title, slug):
    nav_entry = f'    - {title}: user-guides/{slug}/index.md\n'

    with open(NAV_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    inserted = False

    for line in lines:
        new_lines.append(line)
        if "User Guides:" in line and not inserted:
            new_lines.append(nav_entry)
            inserted = True

    with open(NAV_FILE, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

def run_command(cmd):
    print(f"\n▶ Running: {cmd}")
    subprocess.run(cmd, shell=True)

def main():
    print("\n=== FULL AUTOMATION PIPELINE ===\n")

    title = input("Enter article title: ").strip()
    slug = slugify(title)

    folder_path = os.path.join(BASE_PATH, slug)
    file_path = os.path.join(folder_path, "index.md")

    if os.path.exists(folder_path):
        print("❌ Guide already exists.")
        return

    print("\nPaste FULL GPT Markdown (type END on a new line to finish):")

    content_lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        content_lines.append(line)

    content = "\n".join(content_lines)

    os.makedirs(folder_path)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n✅ File created: {file_path}")

    # Update navigation
    update_nav(title, slug)
    print("✅ Navigation updated")

    # Git + deploy
    run_command("git add .")
    run_command(f'git commit -m "Add guide: {title}"')
    run_command("git push origin master")
    run_command("py -m mkdocs gh-deploy --force")

    print("\n🎉 DONE: Fully automated pipeline executed")

if __name__ == "__main__":
    main()