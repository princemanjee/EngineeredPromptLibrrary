# Reasoning Strategy Prompt Library

A curated library of 17 reasoning strategy prompt templates for AI agents. Each template provides a complete, production-ready system prompt that applies a specific reasoning strategy — with persona, constraints, framework, examples, and output format.

## Quick Start

**Select a strategy**: Use `library/router.md` for guided selection across 6 dimensions.

**Use a template**: Copy the contents of any `.md` file in `library/strategies/` as a system prompt (or prepend it to your user message).

**Add a strategy**: Run `/build-strategy` in Claude Code, or manually follow the Research → Plan → Build → Validate pipeline using the agents in `.claude/agents/`.

---

## Strategy Index

### Single-Path Reasoning

| Strategy | File | Best For |
|---|---|---|
| Chain-of-Thought (CoT) | `cot_chain_of_thought.md` | Multi-step problems where showing work matters |
| Zero-Shot CoT | `cot_zero_shot.md` | Activating reasoning with no examples |
| Few-Shot | `few_shot.md` | Tasks where format/style must match examples |
| Plan-and-Solve | `plan_and_solve.md` | Complex problems that benefit from upfront planning |

### Multi-Path / Sampling

| Strategy | File | Best For |
|---|---|---|
| Self-Consistency | `self_consistency.md` | High-accuracy factual/math where errors are unacceptable |
| Tree of Thought | `tree_of_thought.md` | Exploratory problems needing branching and backtracking |
| Graph of Thought | `graph_of_thought.md` | Problems where insights from multiple branches should merge |

### Self-Refinement

| Strategy | File | Best For |
|---|---|---|
| Self-Refine | `self_refine.md` | Writing quality where iteration improves output |
| Reflexion | `reflexion.md` | Agentic tasks where failures provide learning signal |

### Decomposition

| Strategy | File | Best For |
|---|---|---|
| Least-to-Most | `least_to_most.md` | Problems with prerequisite subproblem structure |
| Skeleton-of-Thought | `skeleton_of_thought.md` | Long-form documents needing complete coverage |
| Program-of-Thought | `program_of_thought.md` | Math and algorithmic problems requiring exact computation |

### Retrieval / Tool Use

| Strategy | File | Best For |
|---|---|---|
| ReAct | `react.md` | Agentic tasks with tools; dynamic plan adaptation needed |
| ReWOO | `rewoo.md` | Agentic tasks where full plan is knowable upfront |

### Verification

| Strategy | File | Best For |
|---|---|---|
| Chain-of-Verification | `chain_of_verification.md` | Factual responses where hallucination risk is high |

### Abstraction / Analogy

| Strategy | File | Best For |
|---|---|---|
| Step-Back | `step_back.md` | Complex questions that benefit from general-principle priming |
| Analogical Prompting | `analogical_prompting.md` | Problems where self-generated examples clarify the approach |

---

## Strategy Selection Guide

Use `library/router.md` for the full decision framework. Quick reference:

| Task Type | Recommended Strategy |
|---|---|
| Math / logic with one correct answer | Self-Consistency or Program-of-Thought |
| Multi-step reasoning, show your work | Chain-of-Thought |
| Needs tools / web search | ReAct (dynamic) or ReWOO (upfront plan) |
| Writing quality (essay, docs, code) | Self-Refine |
| Debugging / agentic retries | Reflexion |
| Long document / report | Skeleton-of-Thought |
| Hard exploratory problem | Tree-of-Thought |
| Factual accuracy critical | Chain-of-Verification |
| Problem has natural subproblems | Least-to-Most |
| Unknown approach needed | Analogical Prompting or Step-Back |

---

## Template Structure

Every template follows the same XML structure:

```xml
<OBJECTIVE_AND_PERSONA>    — Who you are applying this strategy
<STRATEGY_OVERVIEW>        — When to use / avoid
<CONTEXT_AND_TONE>         — Key mindset for applying the strategy
<CONSTRAINTS>              — DOS and DONTS
  <DOS>
  <DONTS>
<REASONING_FRAMEWORK>      — The core algorithm / loop
  <STRATEGY_NAME>
<INSTRUCTIONS>             — PromptScript workflow notation
<ITERATIVE_PROCESS>        — Post-solution review steps
<FEW_SHOT_EXAMPLES>        — 2 complete worked examples
<METRICS_AND_EVALUATION>   — Quality checklist
<OUTPUT_FORMAT>            — Exact section/format specification
<RECAP>                    — 2-3 sentence essence summary
```

---

## Combining Strategies

Some problems benefit from combining strategies. Common combinations:

- **Self-Consistency + CoT**: Run multiple CoT paths, take majority vote for high-stakes factual answers
- **Reflexion + ReAct**: Use ReAct for tool-augmented retries, Reflexion for verbal reflection between attempts
- **Skeleton-of-Thought + Self-Refine**: Outline the document first (SoT), then critique and refine each section (SR)
- **Step-Back + CoT**: Use Step-Back to activate general principles, then CoT to apply them to the specific problem
- **ReWOO + Chain-of-Verification**: Plan and execute tool calls (ReWOO), then verify factual claims in the result (CoVe)

See `library/router.md` "Combination Patterns" section for the full decision guide.

---

## Adding New Strategies

### Option A: Slash command (recommended)
```
/build-strategy
```
Runs the full Research → Plan → Build → Validate pipeline interactively.

### Option B: Manual pipeline
1. Use `strategy-researcher` agent to research the strategy
2. Use `strategy-planner` agent to design the template structure
3. Use `strategy-builder` agent to write the template
4. Use `strategy-validator` agent to validate quality
5. Add the new strategy to this README's index table

### Option C: Direct write
Follow the template structure above. Use an existing template (e.g., `reflexion.md` or `tree_of_thought.md`) as a reference. Validate with `strategy-validator`.

---

## File Organization

```
library/
├── README.md                    — This file
├── router.md                    — Strategy selection guide
└── strategies/
    ├── analogical_prompting.md
    ├── chain_of_verification.md
    ├── cot_chain_of_thought.md
    ├── cot_zero_shot.md
    ├── few_shot.md
    ├── graph_of_thought.md
    ├── least_to_most.md
    ├── plan_and_solve.md
    ├── program_of_thought.md
    ├── react.md
    ├── reflexion.md
    ├── rewoo.md
    ├── self_consistency.md
    ├── self_refine.md
    ├── skeleton_of_thought.md
    ├── step_back.md
    └── tree_of_thought.md
```

---

## Reference

- **Strategy source**: `assets/ReasoningStrategies.txt` — ~90KB reference document covering 40+ strategies
- **Agent definitions**: `.claude/agents/` — Research, plan, build, validate, and orchestrate pipeline
- **Build command**: `.claude/commands/build-strategy.md` — `/build-strategy` slash command
- **PRP**: `PRPs/reasoning-strategy-prompt-library.md` — Original feature specification
