# XML Format Requirements

Every `.xml` file in this folder is a v2.0 context-engineered prompt in XML format.

---

## Required File Header

Every XML prompt must begin with exactly this header:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- CONTEXT ENGINEERING TEMPLATE v2.0 -->
<!-- Source: [original filename from PromptLibrary-XML/] -->

<CONTEXT_ENGINEERING_TEMPLATE>
```

And end with:

```xml
</CONTEXT_ENGINEERING_TEMPLATE>
```

---

## Indentation Standard

- 2 spaces per nesting level
- Root-level sections (direct children of `<CONTEXT_ENGINEERING_TEMPLATE>`): 2-space indent
- Subsections within a section: 4-space indent
- Content within subsections: 6-space indent

```xml
<CONTEXT_ENGINEERING_TEMPLATE>

  <SYSTEM_INSTRUCTIONS>
    [content here at 4 spaces]
  </SYSTEM_INSTRUCTIONS>

  <OBJECTIVE_AND_PERSONA>
    <Objective>
      [content here at 6 spaces]
    </Objective>
    <Persona>
      [content here at 6 spaces]
    </Persona>
  </OBJECTIVE_AND_PERSONA>

</CONTEXT_ENGINEERING_TEMPLATE>
```

---

## All 16 Section Tags (in order)

Required sections (must be present in every v2.0 prompt):

```
1.  <SYSTEM_INSTRUCTIONS>
2.  <OBJECTIVE_AND_PERSONA>
3.  <CONTEXT>
4.  <INSTRUCTIONS>
8.  <CONSTRAINTS>
9.  <TONE_AND_STYLE>
10. <FEW_SHOT_EXAMPLES>
11. <ITERATIVE_PROCESS>
12. <POLISH_FOR_PUBLICATION>
13. <RESPONSE_FORMAT>
14. <FLEXIBILITY>
15. <METRICS>
16. <RECAP>
```

Conditional/optional sections (include when applicable):

```
5.  <CHAIN_OF_THOUGHT>     — Include when strategy uses CoT, Plan-and-Solve, or Least-to-Most
6.  <TREE_OF_THOUGHT>      — Include when strategy uses ToT or GoT
7.  <TOOL_INTEGRATION>     — Include ONLY when persona uses external tools (ReAct/ReWOO)
```

---

## Complete Structural Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- CONTEXT ENGINEERING TEMPLATE v2.0 -->
<!-- Source: [filename].xml -->

<CONTEXT_ENGINEERING_TEMPLATE>

  <SYSTEM_INSTRUCTIONS>
    [Strategy declaration and core behavior — 2–4 sentences]
  </SYSTEM_INSTRUCTIONS>

  <OBJECTIVE_AND_PERSONA>
    <Objective>
      [Measurable goal statement]
    </Objective>
    <Persona>
      [Named role + identity traits]
    </Persona>
  </OBJECTIVE_AND_PERSONA>

  <CONTEXT>
    [Domain description, use case, strategy justification]
  </CONTEXT>

  <INSTRUCTIONS>
    <Phase name="Understand">
      [Input parsing, goal identification, sub-agent role if applicable]
    </Phase>
    <Phase name="Execute">
      [Core task execution with strategy mechanics]
    </Phase>
    <Phase name="Deliver">
      [Output assembly, scoring gate, final check]
    </Phase>
  </INSTRUCTIONS>

  <!-- Optional: include if strategy uses CoT/Plan-and-Solve/Least-to-Most -->
  <CHAIN_OF_THOUGHT>
    Activation: [Always | On complex requests | When multi-step reasoning needed]
    Visibility: [Show reasoning | Hide reasoning | Show on request]
    Pattern: [Step pattern appropriate to strategy]
  </CHAIN_OF_THOUGHT>

  <!-- Optional: include if strategy uses ToT or GoT -->
  <TREE_OF_THOUGHT>
    Trigger: [When to activate branching]
    Branches: [K=N branches maximum]
    Depth: [N levels]
    Evaluation: [Criteria for selecting best branch]
  </TREE_OF_THOUGHT>

  <!-- Conditional: include ONLY if persona uses external tools -->
  <TOOL_INTEGRATION>
    <AvailableTools>
      [List tools the persona uses]
    </AvailableTools>
    <UsageRules>
      [ReAct loop OR ReWOO plan format]
    </UsageRules>
  </TOOL_INTEGRATION>

  <CONSTRAINTS>
    <DOs>
      - [DO 1]
      - [DO 2]
      - [DO 3]
    </DOs>
    <DONTs>
      - [DONT 1]
      - [DONT 2]
      - [DONT 3]
    </DONTs>
    <Boundaries>
      [Scope, length, time, domain limits]
    </Boundaries>
  </CONSTRAINTS>

  <TONE_AND_STYLE>
    [Tone descriptor(s) + format notes]
  </TONE_AND_STYLE>

  <FEW_SHOT_EXAMPLES>
    <Example type="positive">
      Input: [example input]
      Output: [example output showing strategy in action]
    </Example>
    <Example type="negative">
      Input: [example input]
      Output: [what NOT to do and why]
    </Example>
  </FEW_SHOT_EXAMPLES>

  <ITERATIVE_PROCESS>
    <Cycle>
      1. DRAFT → [domain-specific output description]
      2. EVALUATE → Score against criteria:
         - [Domain Dimension 1]: [0-100%]
         - [Domain Dimension 2]: [0-100%]
         - [Domain Dimension 3]: [0-100%]
      3. REFINE → Address all dimensions scoring below 85%
      4. VALIDATE → Confirm all ≥85%; repeat if needed
    </Cycle>
    Max Iterations: [2-5]
    User Checkpoints: [Yes | No]
  </ITERATIVE_PROCESS>

  <POLISH_FOR_PUBLICATION>
    Pre-Delivery Checklist:
      □ [Domain-specific check 1]
      □ [Domain-specific check 2]
      □ [Domain-specific check 3]
      □ Format matches specification
      □ No placeholder text remains
  </POLISH_FOR_PUBLICATION>

  <RESPONSE_FORMAT>
    Structure: [Narrative | Sectioned | Bullet-list | Hybrid | JSON]
    Markup: [Markdown | Plain | XML | Code]
    <Template>
      [Output skeleton]
    </Template>
    Length Target: [X-Y words | Flexible with justification]
  </RESPONSE_FORMAT>

  <FLEXIBILITY>
    <ConditionalLogic>
      IF [condition A] → THEN [behavior A]
      IF [condition B] → THEN [behavior B]
      IF [ambiguity detected] → THEN [ask clarification | state assumption]
    </ConditionalLogic>
    <UserOverrides>
      Adjustable: [list parameters]
      Syntax: "Override: [parameter]=[value]"
    </UserOverrides>
    <Defaults>
      [Default behaviors when user doesn't specify]
    </Defaults>
  </FLEXIBILITY>

  <METRICS>
    | Metric              | Measurement Method              | Target  |
    |---------------------|---------------------------------|---------|
    | Task Completion     | All requirements addressed      | 100%    |
    | [Domain Metric 1]   | [Domain-specific method]        | ≥85%    |
    | [Domain Metric 2]   | [Domain-specific method]        | ≥85%    |
    | [Domain Metric 3]   | [Domain-specific method]        | ≥85%    |
    | User Satisfaction   | Clarity + usefulness            | ≥4/5    |
    | Iteration Reduction | Drafts needed before acceptance | ≤2      |
  </METRICS>

  <RECAP>
    🎯 Primary Objective: [1-sentence restatement]

    ⚡ Critical Requirements:
      1. [Most important must-have]
      2. [Second priority — often the strategy reminder]
      3. [Third priority]

    🚫 Absolute Avoids: [Top 1-2 DONTs restated]

    ✅ Final Reminder: [The strategy or quality behavior that must not be forgotten]
  </RECAP>

</CONTEXT_ENGINEERING_TEMPLATE>
```
