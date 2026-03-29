# Markdown Format Requirements

Every `.md` file in this folder is a v2.0 context-engineered prompt in Markdown format. Content is identical to the corresponding `.xml` file — only the markup syntax differs.

---

## Section Heading Structure

Each of the 16 template sections becomes an `##` heading. Subsections use `###`.

```
## SYSTEM_INSTRUCTIONS
## OBJECTIVE_AND_PERSONA
### Objective
### Persona
## CONTEXT
## INSTRUCTIONS
### Phase 1: Understand
### Phase 2: Execute
### Phase 3: Deliver
## CHAIN_OF_THOUGHT          ← optional
## TREE_OF_THOUGHT            ← optional
## TOOL_INTEGRATION           ← conditional
## CONSTRAINTS
### DOs
### DONTs
### Boundaries
## TONE_AND_STYLE
## FEW_SHOT_EXAMPLES
### Example 1 (Positive)
### Example 2 (Anti-example)
## ITERATIVE_PROCESS
## POLISH_FOR_PUBLICATION
## RESPONSE_FORMAT
## FLEXIBILITY
### Conditional Logic
### User Overrides
### Defaults
## METRICS
## RECAP
```

---

## Formatting Conventions

**Code examples**: Use fenced code blocks with language tag

````markdown
```xml
<SYSTEM_INSTRUCTIONS>
  ...
</SYSTEM_INSTRUCTIONS>
```
````

**DOs and DONTs**: Bold prefix on bullet lists

```markdown
### DOs
- **DO** explain your reasoning step by step
- **DO** verify all factual claims before delivery

### DONTs
- **DON'T** deliver without completing the iterative loop
- **DON'T** skip the EVALUATE scoring step
```

**METRICS section**: Markdown table

```markdown
| Metric            | Measurement Method         | Target |
|-------------------|----------------------------|--------|
| Task Completion   | All requirements addressed | 100%   |
| Domain Metric 1   | Domain-specific check      | ≥85%   |
| User Satisfaction | Clarity + usefulness       | ≥4/5   |
```

**ITERATIVE_PROCESS cycle**: Numbered list with sub-bullets for scoring dimensions

```markdown
1. **DRAFT** → Generate initial response
2. **EVALUATE** → Score against criteria:
   - Domain Dimension 1: [0-100%]
   - Domain Dimension 2: [0-100%]
   - Domain Dimension 3: [0-100%]
3. **REFINE** → Address all dimensions below 85%
4. **VALIDATE** → Confirm all ≥85%; repeat if needed

**Max Iterations**: 3
**User Checkpoints**: No
```

**RECAP section**: Emoji-prefixed structure

```markdown
🎯 **Primary Objective**: [1-sentence restatement]

⚡ **Critical Requirements**:
1. [Most important must-have]
2. [Strategy reminder]
3. [Third priority]

🚫 **Absolute Avoids**: [Top 1-2 DONTs]

✅ **Final Reminder**: [The one thing that must not be forgotten]
```

---

## Complete Section Order Reference

All 16 sections in order. Required sections must always be present. Optional/conditional sections follow the same rules as the XML version.

| # | Section | Status |
|---|---------|--------|
| 1 | `## SYSTEM_INSTRUCTIONS` | Required |
| 2 | `## OBJECTIVE_AND_PERSONA` | Required |
| 3 | `## CONTEXT` | Required |
| 4 | `## INSTRUCTIONS` | Required |
| 5 | `## CHAIN_OF_THOUGHT` | Optional — include when strategy uses CoT/Plan-and-Solve/Least-to-Most |
| 6 | `## TREE_OF_THOUGHT` | Optional — include when strategy uses ToT or GoT |
| 7 | `## TOOL_INTEGRATION` | Conditional — include ONLY for tool-using personas (ReAct/ReWOO) |
| 8 | `## CONSTRAINTS` | Required |
| 9 | `## TONE_AND_STYLE` | Required |
| 10 | `## FEW_SHOT_EXAMPLES` | Required |
| 11 | `## ITERATIVE_PROCESS` | Required |
| 12 | `## POLISH_FOR_PUBLICATION` | Required |
| 13 | `## RESPONSE_FORMAT` | Required |
| 14 | `## FLEXIBILITY` | Required |
| 15 | `## METRICS` | Required |
| 16 | `## RECAP` | Required |
