name: "Reasoning Strategy Prompt Library & Orchestration Agent"
description: |

## Purpose
Build a library of context engineering frameworks — one prompt template per reasoning strategy — and an orchestrator agent that selects and applies the right strategy (or combination) for any given task.

## Core Principles
1. **Context is King**: Include ALL necessary documentation, examples, and caveats
2. **Validation Loops**: Provide executable checks the AI can run and fix
3. **Information Dense**: Use keywords and patterns from the codebase
4. **Progressive Success**: Start simple, validate, then enhance
5. **Global rules**: Follow all rules in CLAUDE.md

---

## Goal

Build two things:

1. **Reasoning Strategy Prompt Library** (`library/`) — A collection of reusable, XML-structured prompt templates, one per reasoning strategy (CoT, ToT, ReACT, ReWOO, Self-Refine, etc.), following the existing XML/PromptScript conventions in `examples/`. Each template is self-contained, parameterizable, and includes the reasoning pattern, instructions, constraints, and output format.

2. **Orchestrator Agent** (`.claude/agents/reasoning-orchestrator.md`) — A Claude Code subagent that, given a user task/goal, selects the optimal strategy or combination of strategies, instantiates the correct prompt template(s), and coordinates sub-agents (researcher, planner, builder, validator) to produce high-quality LLM outputs.

---

## Why

- **Problem solved**: Engineers currently must manually select reasoning strategies and hand-write prompt templates for each task. This is slow, inconsistent, and requires deep knowledge of the strategy landscape.
- **User impact**: Any developer can describe a task and get a best-practice, strategy-optimized prompt — without knowing which strategy to use.
- **Business value**: Builds a reusable, growing library that compounds in value with each new strategy added. Directly supports the JobAI branch mission.

---

## What

### User-visible behavior
- Run `/execute-prp PRPs/reasoning-strategy-prompt-library.md` → the orchestrator agent and full library are created
- A developer describes a task (e.g. "analyze this legal document for risks") → the router selects the best strategy → instantiates and returns a ready-to-use prompt
- Each library template is a standalone `.md` file following XML/PromptScript conventions, usable independently or via the router

### Technical requirements
- One `.md` file per strategy in `library/strategies/`
- A strategy router in `library/router.md`
- Four sub-agent definitions in `.claude/agents/`
- An orchestrator agent in `.claude/agents/reasoning-orchestrator.md`
- All templates follow the XML structure in `examples/ContextEngineer.md` and `examples/PromptEngineerTemplate.md`

### Success Criteria
- [ ] At least 15 strategy templates covering all major categories (single-path, multi-path, tree/graph, self-refinement, decomposition, retrieval-augmented, multi-agent, meta-reasoning)
- [ ] Each template is self-contained and usable without the orchestrator
- [ ] Router correctly selects strategy given a task description
- [ ] Orchestrator coordinates sub-agents to build new templates autonomously
- [ ] All files follow XML/PromptScript conventions from `examples/`
- [ ] `library/README.md` documents usage clearly

---

## All Needed Context

### Documentation & References

```yaml
# MUST READ - Include these in your context window

- file: assets/ReasoningStrategies.txt
  why: PRIMARY REFERENCE — exhaustive guide to all strategies with examples, tradeoffs,
       and comparisons. Read this in full before writing any template.
  critical: Covers 40+ strategies across 8 categories. Each strategy section includes
            what it is, when to use it, tradeoffs, and notable implementations.

- file: examples/ContextEngineer.md
  why: Shows the XML template structure to follow — OBJECTIVE_AND_PERSONA, INSTRUCTIONS,
       CONSTRAINTS, CHAIN_OF_THOUGHT, TREE_OF_THOUGHT, OUTPUT_FORMAT sections.
  critical: This is the canonical template pattern for this repo.

- file: examples/PromptEngineerTemplate.md
  why: Minimal XML template skeleton — use as base for each strategy template.

- file: examples/AppBuilder_Unabridged.md
  why: Shows CONSTRAINTS (DOS/DONTS), TOOL_INTEGRATION, ITERATIVE_PROCESS patterns.

- file: examples/ContextEngineer - Template.md
  why: Shows TEMPLATE_STRUCTURE definition with REASONING_FRAMEWORK, ITERATIVE_PROCESS,
       FEW_SHOT_EXAMPLES, METRICS_AND_EVALUATION, RECAP sections.

- file: use-cases/agent-factory-with-subagents/CLAUDE.md
  why: Pattern for multi-phase orchestrator with sub-agents — Phase 0 clarification,
       Phase 1-N parallel sub-agents, autonomous execution.
  critical: Shows exactly how to define sub-agent coordination workflow.

- file: .claude/agents/ (in use-cases/agent-factory-with-subagents/.claude/agents/)
  why: Real sub-agent definition files to mirror for our 4 sub-agents.

- file: PRPs/EXAMPLE_multi_agent_prp.md
  why: Shows complete PRP with task list, pseudocode, and validation gates.

- url: https://arxiv.org/pdf/2510.26493
  why: MOST IMPORTANT external reference — academic paper on reasoning strategies.
       Agent should WebFetch this for additional depth on strategy selection.

- url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  why: Anthropic's own guide on context engineering for agents.

- url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
  why: Claude prompt engineering best practices — critical for template quality.

- url: https://platform.claude.com/docs/en/resources/prompt-library/library
  why: Claude's prompt library — reference examples of high-quality prompts.
```

### Current Codebase Tree

```bash
context-engineering-intro/
├── .claude/
│   ├── commands/
│   │   ├── generate-prp.md
│   │   └── execute-prp.md
│   └── settings.local.json
├── PRPs/
│   ├── templates/prp_base.md
│   └── EXAMPLE_multi_agent_prp.md
├── examples/
│   ├── ContextEngineer.md              ← XML template pattern
│   ├── ContextEngineer - Template.md   ← Template structure definition
│   ├── PromptEngineerTemplate.md       ← Minimal skeleton
│   ├── AppBuilder_Unabridged.md        ← Full orchestrator example
│   └── ResumeTemplateC/               ← Multi-file context system example
├── assets/
│   └── ReasoningStrategies.txt        ← PRIMARY REFERENCE (~90KB)
├── use-cases/
│   └── agent-factory-with-subagents/
│       ├── CLAUDE.md                  ← Orchestration workflow pattern
│       └── .claude/agents/            ← Sub-agent definition examples
├── CLAUDE.md
└── INITIAL.md
```

### Desired Codebase Tree

```bash
context-engineering-intro/
├── .claude/
│   ├── commands/
│   │   ├── generate-prp.md
│   │   ├── execute-prp.md
│   │   └── build-strategy.md          ← NEW: slash command to add a new strategy
│   └── agents/
│       ├── strategy-researcher.md     ← NEW: researches a strategy in depth
│       ├── strategy-planner.md        ← NEW: plans template structure
│       ├── strategy-builder.md        ← NEW: writes the XML template
│       └── strategy-validator.md      ← NEW: validates template quality
├── library/
│   ├── README.md                      ← NEW: usage guide + strategy index
│   ├── router.md                      ← NEW: strategy selector prompt
│   └── strategies/
│       ├── cot_chain_of_thought.md    ← NEW
│       ├── cot_zero_shot.md           ← NEW
│       ├── few_shot.md                ← NEW
│       ├── plan_and_solve.md          ← NEW
│       ├── self_consistency.md        ← NEW
│       ├── tree_of_thought.md         ← NEW
│       ├── graph_of_thought.md        ← NEW
│       ├── self_refine.md             ← NEW
│       ├── reflexion.md               ← NEW
│       ├── chain_of_verification.md   ← NEW
│       ├── least_to_most.md           ← NEW
│       ├── react.md                   ← NEW
│       ├── rewoo.md                   ← NEW
│       ├── step_back.md               ← NEW
│       ├── analogical_prompting.md    ← NEW
│       └── skeleton_of_thought.md     ← NEW
├── .claude/
│   └── agents/
│       └── reasoning-orchestrator.md ← NEW: master orchestrator
...
```

### Known Gotchas

```yaml
# CRITICAL: This is NOT a Python project — deliverables are .md and .xml files
# All templates must follow XML/PromptScript conventions (see CLAUDE.md Style section)
# Opening and closing XML tags required for ALL sections and subsections

# CRITICAL: Each strategy template must be SELF-CONTAINED
# A user should be able to copy any single template and use it without the orchestrator

# CRITICAL: PromptScript notation — use consistently across all templates:
#   [ ] = tasks, { } = inputs, ( ) = context, < > = output format
#   | = options, @ = multi-turn, -> = sequences, [[ ]] = loops

# CRITICAL: The router must NOT hardcode strategy selection
# It should reason about the task and select based on task properties:
#   - Is the task decomposable? → Least-to-Most, Skeleton-of-Thought
#   - Does it require tool use? → ReACT, ReWOO
#   - Does it require verification? → CoVe, Self-Verify
#   - Does it require creativity/exploration? → ToT, GoT
#   - Is it a well-defined single-path problem? → CoT, Plan-and-Solve

# CRITICAL: Sub-agent definitions follow the pattern in:
#   use-cases/agent-factory-with-subagents/.claude/agents/pydantic-ai-planner.md
# They define: role, trigger, inputs, outputs, constraints, workflow steps

# PATTERN: File naming — snake_case for strategy files, kebab-case for agents
# e.g.: library/strategies/chain_of_thought.md, .claude/agents/strategy-builder.md
```

---

## Implementation Blueprint

### Data Models and Structure

```xml
<!-- Each strategy template follows this XML structure (from examples/ContextEngineer.md) -->

<OBJECTIVE_AND_PERSONA>
  You are an expert [role appropriate to task]. Your goal is to [specific outcome].
  You will apply the [STRATEGY NAME] reasoning strategy.
</OBJECTIVE_AND_PERSONA>

<STRATEGY_OVERVIEW>
  [Strategy name and 1-2 sentence description]
  Best used when: [task characteristics]
  Avoid when: [contraindications]
</STRATEGY_OVERVIEW>

<CONTEXT_AND_TONE>
  [Background, operating assumptions, voice]
</CONTEXT_AND_TONE>

<CONSTRAINTS>
  <DOS>[Mandatory inclusions]</DOS>
  <DONTS>[Strict prohibitions]</DONTS>
</CONSTRAINTS>

<REASONING_FRAMEWORK>
  <!-- Strategy-specific reasoning instructions -->
  <!-- e.g., for CoT: -->
  <CHAIN_OF_THOUGHT>
    Before answering, reason step by step:
    1. Decompose the problem
    2. Address each component
    3. Synthesize into final answer
  </CHAIN_OF_THOUGHT>
</REASONING_FRAMEWORK>

<INSTRUCTIONS>
  [Step-by-step execution plan using PromptScript notation]
  [task_step_1]{input} -> [task_step_2] -> <output_format>
</INSTRUCTIONS>

<ITERATIVE_PROCESS>
  [Self-critique and refinement step]
  Draft -> Critique -> Revise -> Final
</ITERATIVE_PROCESS>

<FEW_SHOT_EXAMPLES>
  Input: [example input]
  Output: [example ideal output]
</FEW_SHOT_EXAMPLES>

<METRICS_AND_EVALUATION>
  [Success criteria for the output]
</METRICS_AND_EVALUATION>

<OUTPUT_FORMAT>
  [Exact structure of the final response]
</OUTPUT_FORMAT>

<RECAP>
  [Final summary instruction to maintain focus]
</RECAP>
```

### Router Structure

```xml
<!-- library/router.md -->
<OBJECTIVE_AND_PERSONA>
  You are a Reasoning Strategy Router. Given a task description, you select the
  optimal reasoning strategy or combination of strategies from the library.
</OBJECTIVE_AND_PERSONA>

<SELECTION_FRAMEWORK>
  Evaluate the task against these dimensions:
  - Complexity: [Simple | Multi-step | Highly complex]
  - Decomposability: [Atomic | Decomposable | Hierarchical]
  - Verification needs: [None | Self-check | Formal verification]
  - Tool use required: [None | Web search | Code execution | External APIs]
  - Exploration needed: [Linear | Branching | Graph]
  - Domain: [Math/Logic | Creative | Research | Code | Analysis]
</SELECTION_FRAMEWORK>

<STRATEGY_DECISION_TREE>
  <!-- Maps task properties → strategy recommendation -->
</STRATEGY_DECISION_TREE>
```

---

### List of Tasks

```yaml
Task 1: Read and internalize PRIMARY REFERENCE
ACTION:
  - Read assets/ReasoningStrategies.txt in full
  - Read examples/ContextEngineer.md (XML pattern to follow)
  - Read examples/PromptEngineerTemplate.md (minimal skeleton)
  - Read examples/AppBuilder_Unabridged.md (CONSTRAINTS/TOOL_INTEGRATION patterns)
  - Read use-cases/agent-factory-with-subagents/.claude/agents/pydantic-ai-planner.md
    (sub-agent definition pattern)
  - WebFetch https://arxiv.org/pdf/2510.26493 for additional strategy depth
OUTPUT: Deep understanding of all 40+ strategies and XML template conventions

Task 2: Create library directory structure
ACTION:
  - CREATE library/
  - CREATE library/strategies/
  - CREATE .claude/agents/ (if not exists)
OUTPUT: Directory scaffold ready

Task 3: Build core single-path strategy templates (highest value, most used)
CREATE library/strategies/cot_chain_of_thought.md:
  - MIRROR XML pattern from examples/ContextEngineer.md
  - REASONING_FRAMEWORK: step-by-step linear decomposition
  - FEW_SHOT_EXAMPLES: math problem, logical deduction
  - Include "Think step by step" instruction pattern

CREATE library/strategies/cot_zero_shot.md:
  - Simpler version: just append "Let's think step by step"
  - When to use: quick tasks where few-shot is overkill

CREATE library/strategies/few_shot.md:
  - Template with {examples} input parameter
  - Instructions for selecting high-quality examples

CREATE library/strategies/plan_and_solve.md:
  - Two-phase: explicit plan → execute
  - INSTRUCTIONS: [plan]{task} -> [execute]{plan} -> <result>

Task 4: Build multi-path and tree/graph strategy templates
CREATE library/strategies/self_consistency.md:
  - Sample multiple CoT paths → majority vote
  - INSTRUCTIONS: [[generate_path]{task}]*N -> [vote]{paths} -> <consensus>

CREATE library/strategies/tree_of_thought.md:
  - BFS/DFS over branching thought paths with evaluation
  - REASONING_FRAMEWORK: generate branches, evaluate each, select best
  - Include ToT evaluation rubric

CREATE library/strategies/skeleton_of_thought.md:
  - Generate outline first → fill sections in parallel
  - Best for: long-form content, structured documents

Task 5: Build self-refinement strategy templates
CREATE library/strategies/self_refine.md:
  - Generate → critique → revise loop
  - ITERATIVE_PROCESS: [generate] -> [critique]{output} -> [revise]{critique} -> [[repeat]]*N

CREATE library/strategies/reflexion.md:
  - Reflect on failures → store insights → retry
  - Include memory/context store pattern

CREATE library/strategies/chain_of_verification.md:
  - Generate answer → create verification questions → check → revise
  - INSTRUCTIONS: [answer]{question} -> [verify_questions]{answer} -> [check] -> [revise]

Task 6: Build decomposition and retrieval strategy templates
CREATE library/strategies/least_to_most.md:
  - Decompose into subproblems → solve easiest first → build up
  - INSTRUCTIONS: [decompose]{task} -> [[solve_subproblem]]*N -> [synthesize]

CREATE library/strategies/react.md:
  - Interleave Reasoning + Acting (tool use)
  - TOOL_INTEGRATION: when/how to call tools, observation format
  - Pattern: Thought → Action → Observation → Thought → ...

CREATE library/strategies/rewoo.md:
  - ReACT variant: plan all tool calls first, then execute
  - Two phases: Planner (writes full plan) → Solver (executes)
  - CRITICAL: reduces token usage vs ReACT by separating planning from execution

Task 7: Build meta-reasoning strategy templates
CREATE library/strategies/step_back.md:
  - Ask high-level/abstract question first → then solve specific
  - INSTRUCTIONS: [step_back]{specific_question} -> [answer_abstract] -> [apply_to_specific]

CREATE library/strategies/analogical_prompting.md:
  - LLM generates its own relevant examples before solving
  - INSTRUCTIONS: [generate_examples]{task_type} -> [solve_with_examples]

Task 8: Build the strategy router
CREATE library/router.md:
  - XML template with SELECTION_FRAMEWORK
  - Decision logic mapping task properties → strategy
  - Output: strategy name + library file path + instantiation instructions
  - Include combination patterns (e.g., ToT + Self-Refine for hard creative tasks)

Task 9: Create sub-agent definitions
CREATE .claude/agents/strategy-researcher.md:
  - Role: Given a strategy name, research it deeply in assets/ReasoningStrategies.txt
    and via WebFetch of the arxiv paper
  - Output: structured research notes (when to use, examples, gotchas)
  - MIRROR pattern from: use-cases/agent-factory-with-subagents/.claude/agents/pydantic-ai-planner.md

CREATE .claude/agents/strategy-planner.md:
  - Role: Given research notes, plan the XML template structure
  - Output: template outline with all sections stubbed

CREATE .claude/agents/strategy-builder.md:
  - Role: Given template outline, write the full XML template
  - Must follow XML/PromptScript conventions exactly
  - Output: complete .md file content

CREATE .claude/agents/strategy-validator.md:
  - Role: Review a completed template for quality
  - Checks: XML structure valid, PromptScript notation correct,
    self-contained usage, examples present, metrics defined
  - Output: pass/fail with specific feedback

Task 10: Create the reasoning orchestrator agent
CREATE .claude/agents/reasoning-orchestrator.md:
  - Role: Given a user task, orchestrate full strategy selection and template delivery
  - Phase 0: Clarify task if ambiguous (1-2 questions max)
  - Phase 1: Invoke strategy-researcher for best matching strategy
  - Phase 2: Invoke strategy-planner + strategy-builder in sequence
  - Phase 3: Invoke strategy-validator; iterate if fails
  - Phase 4: Return instantiated prompt template ready to use
  - MIRROR orchestration pattern from: use-cases/agent-factory-with-subagents/CLAUDE.md

Task 11: Create the /build-strategy slash command
CREATE .claude/commands/build-strategy.md:
  - Accepts: strategy name or description
  - Orchestrates: researcher → planner → builder → validator
  - Saves to: library/strategies/{strategy_name}.md
  - Reports: confidence score and usage notes

Task 12: Write library/README.md
CREATE library/README.md:
  - Strategy index table (name, file, best for, avoid when)
  - Quick start: how to use a template directly
  - Quick start: how to use the router
  - Quick start: how to use the orchestrator
  - How to add a new strategy with /build-strategy
```

---

### Per-Task Pseudocode

```
# Task 3-7: Each strategy template follows this pseudocode

TEMPLATE = {
  OBJECTIVE_AND_PERSONA: "Expert [role]. Apply [STRATEGY].",
  STRATEGY_OVERVIEW: {
    description: "1-2 sentences from assets/ReasoningStrategies.txt",
    best_for: ["task type 1", "task type 2"],
    avoid_when: ["contraindication 1"]
  },
  REASONING_FRAMEWORK: strategy_specific_instructions,
  INSTRUCTIONS: promptscript_task_sequence,
  ITERATIVE_PROCESS: "Draft -> Critique -> Revise",
  FEW_SHOT_EXAMPLES: [
    {input: "example task", output: "example ideal output using this strategy"}
  ],
  METRICS_AND_EVALUATION: ["criterion 1", "criterion 2"],
  OUTPUT_FORMAT: "exact structure",
  RECAP: "one-line focus reminder"
}

# Task 8: Router pseudocode
ROUTER_LOGIC = {
  given: task_description,
  evaluate: {
    has_tool_use: check for "search", "browse", "execute", "API" keywords,
    needs_verification: check for "verify", "check", "validate", "prove",
    is_decomposable: check for "list", "steps", "plan", "multiple",
    needs_exploration: check for "creative", "options", "alternatives",
    is_math_logic: check for numbers, equations, formal reasoning
  },
  select: {
    has_tool_use AND sequential -> "ReACT",
    has_tool_use AND plan_first -> "ReWOO",
    needs_verification -> "Chain-of-Verification",
    is_decomposable AND simple -> "Least-to-Most",
    is_decomposable AND parallel -> "Skeleton-of-Thought",
    needs_exploration -> "Tree-of-Thought",
    is_math_logic -> "Chain-of-Thought",
    default -> "Plan-and-Solve"
  }
}

# Task 10: Orchestrator pseudocode
ORCHESTRATOR = {
  phase_0: clarify(task) if ambiguous,
  phase_1: researcher.run(strategy=router.select(task)),
  phase_2: {
    planner.run(research_notes),
    # then sequentially:
    builder.run(template_outline)
  },
  phase_3: {
    validation = validator.run(template),
    if not validation.passed:
      builder.revise(validation.feedback),
      validator.run(revised_template)  # iterate max 2x
  },
  phase_4: return instantiated_template
}
```

---

### Integration Points

```yaml
FILES_TO_CREATE:
  - library/README.md
  - library/router.md
  - library/strategies/*.md (16 files)
  - .claude/agents/strategy-researcher.md
  - .claude/agents/strategy-planner.md
  - .claude/agents/strategy-builder.md
  - .claude/agents/strategy-validator.md
  - .claude/agents/reasoning-orchestrator.md
  - .claude/commands/build-strategy.md

REFERENCES_TO_READ_FIRST:
  - assets/ReasoningStrategies.txt (primary)
  - examples/ContextEngineer.md (XML pattern)
  - use-cases/agent-factory-with-subagents/CLAUDE.md (orchestration pattern)
  - use-cases/agent-factory-with-subagents/.claude/agents/pydantic-ai-planner.md (sub-agent pattern)

NO_CODE_REQUIRED:
  - This is entirely a prompt/template/markdown engineering project
  - No Python, no tests, no linting tools needed
  - Validation is manual review of template quality
```

---

## Validation Loop

### Level 1: Structure Check (run after each template is created)

```bash
# Verify all required XML sections exist in each template
# For each file in library/strategies/:
grep -l "<OBJECTIVE_AND_PERSONA>" library/strategies/*.md   # all should match
grep -l "<REASONING_FRAMEWORK>" library/strategies/*.md     # all should match
grep -l "<INSTRUCTIONS>" library/strategies/*.md            # all should match
grep -l "<OUTPUT_FORMAT>" library/strategies/*.md           # all should match
grep -l "<FEW_SHOT_EXAMPLES>" library/strategies/*.md       # all should match

# Verify all files exist
ls library/strategies/ | wc -l    # should be >= 15
ls .claude/agents/ | wc -l        # should be >= 5 (4 sub-agents + orchestrator)
```

### Level 2: Content Quality Check

For each strategy template, verify:
- [ ] `<STRATEGY_OVERVIEW>` references the strategy correctly (compare to `assets/ReasoningStrategies.txt`)
- [ ] `<REASONING_FRAMEWORK>` contains strategy-specific instructions (not generic)
- [ ] `<FEW_SHOT_EXAMPLES>` has at least one concrete input/output example
- [ ] `<METRICS_AND_EVALUATION>` has measurable criteria
- [ ] PromptScript notation used in `<INSTRUCTIONS>` (look for `->`, `[ ]`, `{ }`, `< >`)
- [ ] Template is self-contained: paste it into a fresh Claude chat and it works

For the router (`library/router.md`):
- [ ] Has decision logic covering all 8 strategy categories
- [ ] Maps task properties → strategy file path
- [ ] Handles combination strategies (e.g., ReACT + Self-Refine)

For each sub-agent (`.claude/agents/*.md`):
- [ ] Defines: role, trigger condition, inputs, outputs, constraints
- [ ] Defines: step-by-step workflow
- [ ] Specifies: what to output and where to save it

### Level 3: Integration Test

Manual test — run in a Claude Code session:
```
1. Open a new Claude Code session in this repo
2. Ask: "I need to analyze pros and cons of three architectural approaches"
   → Orchestrator should select Tree-of-Thought or Step-Back
   → Should return the instantiated template

3. Ask: "I need to search the web for current LLM benchmarks and summarize findings"
   → Orchestrator should select ReACT or ReWOO
   → Should return the correct tool-use template

4. Ask: "I need to write a detailed technical blog post about vector databases"
   → Orchestrator should select Skeleton-of-Thought
   → Should return the outline-first template
```

---

## Final Validation Checklist

- [ ] All 16 strategy templates exist in `library/strategies/`
- [ ] All templates have required XML sections (verified with grep)
- [ ] `library/router.md` covers all 8 strategy categories
- [ ] `library/README.md` has complete strategy index table
- [ ] All 4 sub-agent definitions exist and follow the factory pattern
- [ ] `reasoning-orchestrator.md` defines all 5 phases
- [ ] `/build-strategy` slash command exists and is runnable
- [ ] Each template tested standalone (copy-paste test in fresh session)
- [ ] No Python/code files created — this is a pure prompt/template project

---

## Anti-Patterns to Avoid

```yaml
- DO NOT create Python files — this is a markdown/XML template project
- DO NOT make templates generic/interchangeable — each must be strategy-specific
- DO NOT skip the FEW_SHOT_EXAMPLES — they are critical for one-shot usability
- DO NOT use vague METRICS_AND_EVALUATION — be specific and measurable
- DO NOT hardcode task types in the router — use property-based reasoning
- DO NOT define sub-agents without specifying their exact input/output contract
- DO NOT create a monolithic "master prompt" — keep each strategy as a separate file
- DO NOT ignore the PromptScript notation — it's required by CLAUDE.md
- DO NOT copy the strategy description verbatim from ReasoningStrategies.txt —
  adapt it into actionable prompt instructions
```

---

## Confidence Score: 8/10

**Reasoning**: The deliverables are well-defined markdown/XML files following clear existing patterns (`examples/ContextEngineer.md`, `use-cases/agent-factory-with-subagents/`). The primary reference (`assets/ReasoningStrategies.txt`) is comprehensive and co-located. The main risk is template quality consistency across 16 files — the validator sub-agent and manual test mitigate this. Deducting 2 points because the router's strategy selection logic requires nuanced judgment that may need iteration, and the orchestrator coordination involves multi-step sub-agent handoffs that are harder to validate mechanically.
