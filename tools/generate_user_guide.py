import os
import re

BASE_PATH = "docs/user-guides"

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def get_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

def create_user_guide():
    print("\n=== User Guide Generator ===\n")

    title = input("Enter article title: ").strip()
    slug = slugify(title)

    folder_path = os.path.join(BASE_PATH, slug)
    file_path = os.path.join(folder_path, "index.md")

    if os.path.exists(folder_path):
        print("❌ Error: Guide already exists.")
        return

    print("\nEnter Overview (press ENTER twice to finish):")
    overview = get_input("> ")

    os.makedirs(folder_path)

    content = f"""# {title}

## Overview
{overview if overview else "Describe what this feature does."}

## Who should use this
- Financial Analysts
- Business Users

## Prerequisites
- Access to the application
- Required permissions enabled

## Steps
1. Navigate to the relevant module
2. Configure required inputs
3. Review the output
4. Save or submit

## Tips and best practices
- Validate inputs before submission
- Use versioning for comparison
- Review data before finalizing

## Troubleshooting
- Ensure required fields are populated
- Check user permissions
- Retry the process if validation fails

---

👉 Previous: [Forecasting Overview](../forecasting-overview/)
👉 Next: [Review and Submit a Forecast](../review-submit-forecast/)
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n✅ Created: {file_path}")

if __name__ == "__main__":
    create_user_guide()