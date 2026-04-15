import os
import re

skills = [
    "dentist",
    "developer-relations-consultant",
    "devops-engineer",
    "diagram-generator",
    "dietitian",
    "digital-art-gallery-guide",
    "doctor",
    "drunk-person",
    "educational-content-creator",
    "elocutionist",
    "emergency-response-professional",
    "emoji-translator",
    "english-pronunciation-helper",
    "english-translator-and-improver",
    "essay-writer",
]

base = r"C:\Code\GitHub\EngineeredPromptLibrrary\prompt-library-plugin\skills"

for skill in skills:
    path = os.path.join(base, skill, "SKILL.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Structure:
    # ---\nfrontmatter\n---\n\n## When to Use\n\n{when_to_use_text}\n\n# Title\n\n{rest}
    # We want:
    # ---\nfrontmatter\n---\n\n# Title\n\n## When to Use\n\n{when_to_use_text}\n\n{rest}

    # Find frontmatter end
    fm_end = content.index("---", 3) + 3  # skip opening ---

    after_fm = content[fm_end:]  # starts with \n\n## When to Use\n\n...

    # Extract ## When to Use block
    wtu_match = re.search(r'\n\n## When to Use\n\n(.*?)\n\n(# .+?\n)', after_fm, re.DOTALL)
    if not wtu_match:
        print(f"SKIP (no match): {skill}")
        continue

    when_to_use_text = wtu_match.group(1).strip()
    title_line = wtu_match.group(2).rstrip()  # e.g. "# Dentist"

    # Everything after the title line
    title_start = after_fm.index(wtu_match.group(2))
    rest = after_fm[title_start + len(wtu_match.group(2)):]

    # Rebuild
    frontmatter = content[:fm_end]
    new_content = (
        frontmatter
        + "\n\n"
        + title_line
        + "\n\n"
        + "## When to Use"
        + "\n\n"
        + when_to_use_text
        + "\n\n"
        + rest.lstrip("\n")
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Fixed: {skill}")
