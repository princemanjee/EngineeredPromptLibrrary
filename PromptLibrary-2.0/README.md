# PromptLibrary 2.0

## Overview

The upgraded prompt library — 225 personas rebuilt as fully context-engineered v2.0 prompts. Every prompt in this library uses `examples/!!MasterContextTemplate.xml` as its structural base and the `Guidelines/` documents as its construction guide.

**What makes a v2.0 prompt different from v1.x:**
- All 13 required template sections present and populated (not placeholders)
- `ITERATIVE_PROCESS` with domain-specific DRAFT → EVALUATE → REFINE → VALIDATE cycle
- `METRICS` table with ≥3 domain-specific numeric targets
- Self-grading rubric (0–100% per dimension, ≥85% threshold)
- Sub-agent patterns where the persona handles multi-stage tasks
- Reasoning strategy declared in `SYSTEM_INSTRUCTIONS` and activated in the appropriate optional sections
- Quality-first: no section trimmed to save tokens

Each prompt exists in two formats — identical content, different markup:
- `XML/[name].xml` — structured XML with tags and nesting
- `Markdown/[name].md` — equivalent H2/H3 Markdown

---

## Folder Structure

```
PromptLibrary-2.0/
├── README.md               ← This file
├── XML/
│   ├── README.md           ← XML format requirements and section tag reference
│   └── [225 .xml files]
└── Markdown/
    ├── README.md           ← Markdown format requirements and section heading reference
    └── [225 .md files]
```

---

## Naming Conventions

File names mirror the source library 1:1. Do not rename files during upgrade.

| Source | XML Output | Markdown Output |
|--------|-----------|-----------------|
| `PromptLibrary-XML/chef.xml` | `PromptLibrary-2.0/XML/chef.xml` | `PromptLibrary-2.0/Markdown/chef.md` |
| `PromptLibrary-XML/data_scientist.xml` | `PromptLibrary-2.0/XML/data_scientist.xml` | `PromptLibrary-2.0/Markdown/data_scientist.md` |
| `PromptLibrary-XML/financial_analyst.xml` | `PromptLibrary-2.0/XML/financial_analyst.xml` | `PromptLibrary-2.0/Markdown/financial_analyst.md` |

**Rules:**
- Preserve underscores, hyphens, and lowercase exactly as in the source filename
- XML files use `.xml` extension; Markdown files use `.md` extension
- `!!MasterContextTemplate.xml` is the template file — do **not** create a 2.0 version of it
- Total at completion: 225 files in `XML/` and 225 files in `Markdown/`

---

## Format Requirements

### XML Format
- Required header: `<?xml version="1.0" encoding="UTF-8"?>`
- Source comment: `<!-- Source: [original filename] -->`
- Root tag: `<CONTEXT_ENGINEERING_TEMPLATE>...</CONTEXT_ENGINEERING_TEMPLATE>`
- All 16 sections as uppercase XML tags with 2-space indentation per nesting level
- All tags must be opened and closed; nested tags properly indented
- See `XML/README.md` for full spec and section tag list

### Markdown Format
- Each of the 16 sections rendered as `## SECTION_NAME`
- Subsections as `### Subsection`
- Code examples in fenced code blocks (` ``` `)
- METRICS section as a Markdown table
- DOs/DONTs as bold-prefixed bullet lists
- Same content as the XML version — only the markup syntax differs
- See `Markdown/README.md` for full spec

---

## Completion Progress

**0 / 225 prompts completed**

Source prompts are in `PromptLibrary-XML/`. Upgrade one prompt at a time following `PRPs/phase3-task2-prompt-upgrade-process.md`.

---

## Reference Documents

Every v2.0 prompt must be built using these guidelines:

| Document | Purpose |
|----------|---------|
| `Guidelines/prompt-construction-guidelines.md` | How to build each section; v1→v2 delta; worked examples |
| `Guidelines/strategy-selection-guide.md` | How to select the right reasoning strategy for each persona |
| `Guidelines/quality-standards.md` | 100-point scoring rubric; 27-item ship-it checklist |
| `Guidelines/prompt-components.md` | Required vs optional components reference |
| `Guidelines/csvs/` | Per-component cognitive framework and strategy rankings |
| `examples/!!MasterContextTemplate.xml` | The canonical 16-section template |
