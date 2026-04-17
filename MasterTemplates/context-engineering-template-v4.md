# Context Engineering Template v4.0

> **Upgraded from v3.0** using the Self-Versioning Protocol (Appendix A).
>
> **Persona used for this revision**: Prompt Engineering Architect specializing in LLM instruction design and meta-cognitive frameworks.
>
> **What changed**: Added a Principles section for mental models, introduced Input Validation and Error Recovery protocols, added multi-turn prompt guidance, consolidated domain signal duplication between Sections 2 and 8, added Prompt Testing framework, made "Why this matters" intros consistent across all sections, added persona behavioral guidance, clarified the unmeasurable convergence rule, and restored Objective/Persona sections to universal template form.
>
> **Usage**: Start with the Quick-Start Checklist if you need a minimal viable prompt. For production prompts, copy relevant sections, customize placeholders `[...]`, and delete unused optional blocks. Sections marked **(Required)** must be present in every production prompt.

---

## Critique Log (v3.0 -> v4.0)

### Dimensional Scores for v3.0

| Dimension | Score | Key Finding |
|-----------|-------|-------------|
| Insight Potential | 82% | Good scaffolding, but no guidance on when reasoning strategies *hurt* output quality. Not every task benefits from Self-Refine (e.g., brainstorming, freeform creative work). Missing failure modes for each strategy. Also missing any bridge between Quick-Start and the full template for medium-complexity tasks. |
| Persona Specificity | 88% | Calibration anchors for persona depth are strong. Gap: no guidance on persona *behavior* under uncertainty, ambiguity, or pushback. A persona is not just what someone knows, it is how they respond when the task is unclear. |
| Structural Completeness | 85% | Domain Signals still appear in both Section 2 (Context) and Section 8 (Flexibility), creating soft redundancy that v3.0 claimed to eliminate. Missing: Input Validation protocol (what should the model do with malformed or insufficient inputs?), multi-turn prompt guidance (template assumes single-shot), and prompt testing framework (how does a user verify their prompt actually works?). |
| Constraint Clarity | 80% | Conflict Resolution Protocol mixes categories (safety is a boundary type, intent is a goal, domain is a context source) without acknowledging that the hierarchy works differently depending on whether the conflict is factual vs. structural. The convergence rule ("less than 5% improvement") is unmeasurable in practice since users have no scoring instrument beyond subjective judgment. |
| Intent Fidelity | 90% | Solid overall. Slight drift toward being a "prompt improvement" tool rather than a "prompt creation" tool. Some sections assume you are enhancing an existing prompt instead of building from scratch. |
| Tone Engagement | 78% | "Why this section matters" intros appear in Sections 1, 2, 3, and partially in Section 5, but are absent from Sections 4, 6, 7, 8, and 9. The inconsistency makes the template feel half-edited. No overarching Principles section to give users mental models for prompt design beyond the mechanics. |
| Process Integrity | 100% | Self-versioning protocol is functional and was followed to produce this version. |

### Revisions Applied

1. **Added Section 0.5: Principles** to provide mental models that inform every other section, reducing dependence on rote checklists.
2. **Added Input Validation protocol** (Section 2) so the model knows how to handle malformed, contradictory, or insufficient inputs.
3. **Added Error Recovery guidance** (Section 3) covering what to do when critique identifies unfixable problems or the model misunderstands the task.
4. **Consolidated Domain Signals** into a single authoritative location (Section 2), with Section 8 referencing rather than duplicating them.
5. **Added multi-turn prompt guidance** (Section 7) for conversational and agentic workflows.
6. **Added Prompt Testing framework** (Section 9) so users can validate their completed prompts.
7. **Made "Why this section matters" intros consistent** across all sections.
8. **Added persona behavioral guidance**: how the persona handles uncertainty and edge cases, not just what it knows.
9. **Clarified the convergence rule** with practical measurement heuristics that do not require a scoring instrument.
10. **Added strategy failure modes** to Section 3 so users know when each reasoning approach can backfire.
11. **Restored Objective and Persona sections** to fully generic/universal template form.
12. **Added a mid-complexity bridge path** between Quick-Start and the full template in the Dependency Map.

---

## Section 0: Quick-Start (Minimal Viable Prompt)

*Why this section matters:* Most prompts do not need the full template. This section gives you a functional prompt in under five minutes. Use the full template only when the Quick-Start produces inadequate results.

A functional prompt needs exactly five elements. Everything else in this template enhances these, but these five alone will outperform an unstructured request:

```
1. ROLE:       Who is the AI acting as? (Specific domain role, not "expert")
2. CONTEXT:    Why does this task exist? Who consumes the output?
3. TASK:       What is the single concrete deliverable?
4. FORMAT:     What does the output look like? (Structure, length, markup)
5. CRITERIA:   What separates great from adequate? (2-3 specific quality markers)
```

**Minimal template:**

```markdown
You are a [specific role with domain expertise].

Context: [Why this task exists. Who will read the output. What they already know.]

Task: [One clear deliverable statement.]

Format: [Structure, markup, length range.]

Quality markers:
- [Specific quality criterion 1]
- [Specific quality criterion 2]
- [Specific quality criterion 3]
```

**When to escalate to the full template:** If your Quick-Start prompt produces output that is structurally right but lacks depth, reasoning quality, or domain specificity, move to the full template. Start with the Required Core sections, then add layers as needed using the Dependency Map below.

---

## Section 0.5: Principles (Mental Models for Prompt Design)

*Why this section matters:* Checklists tell you *what* to include. Principles tell you *why*, which means you can adapt when the checklist does not cover your situation. Internalize these five principles and the rest of the template will feel intuitive rather than mechanical.

**Principle 1: Specificity compounds.**
Every vague instruction forces the model to guess. Each guess has a probability of being wrong. When multiple vague instructions appear together, the probabilities of error multiply. A prompt with five vague instructions is not five times as likely to fail as a prompt with one. It is exponentially more likely to fail. Replace vague instructions with specific ones wherever possible.

**Principle 2: Personas are reasoning lenses, not costumes.**
Setting a persona does not just change vocabulary. It changes what the model attends to, what it treats as relevant, and what it considers a mistake. "You are a security auditor" makes the model notice attack surfaces. "You are a UX designer" makes the same model notice user friction. Choose personas for what they will *notice*, not for how they will *sound*.

**Principle 3: Structure is a form of reasoning.**
Asking the model to organize its output into specific sections is not just formatting. It is a way of requiring the model to think about distinct aspects of the problem separately. A prompt that asks for "analysis, then recommendations, then risks" produces different (and typically better) thinking than a prompt that asks for "your thoughts."

**Principle 4: Constraints liberate.**
Counter-intuitively, adding well-chosen constraints improves output quality. "Write a 200-word summary" produces better summaries than "summarize this." "Explain this to a first-year graduate student" produces clearer explanations than "explain this clearly." Constraints reduce the space the model has to search and increase the probability that it finds a strong answer.

**Principle 5: Critique is not polish.**
The generate-critique-revise cycle is not about making the first draft prettier. It is about finding structural gaps, logical errors, and missing perspectives that the first draft cannot contain because the model had not yet seen its own output when it produced it. If your critique phase only finds surface issues (word choice, tone), your quality dimensions are probably too shallow.

---

## Section Dependency Map

*Why this section matters:* Including unnecessary sections wastes context window tokens and can actually degrade output by overwhelming the model with irrelevant instructions. This map lets you include only what your task requires.

```
REQUIRED CORE (always include):
  Section 1: OBJECTIVE_AND_PERSONA ............. identity + goal
  Section 2: CONTEXT ........................... situation + domain
  Section 5: CONSTRAINTS ....................... rules + boundaries
  Section 7: RESPONSE_FORMAT ................... output specification

REASONING LAYER (add when task requires multi-step thinking):
  Section 3: REASONING ---- depends on ----> Section 1, Section 2

QUALITY LAYER (add when output quality is critical):
  Section 4: QUALITY_DIMENSIONS ---- depends on ----> Section 2 (domain signals)
  Section 6: ITERATIVE_PROCESS ---- depends on ----> Section 4

OPTIONAL ENHANCEMENTS:
  Section 1b: SYSTEM_INSTRUCTIONS .............. standalone, pre-conversation rules
  Section 5b: TONE_AND_STYLE ---- depends on --> Section 2 (domain signals)
  Section 5c: FEW_SHOT_EXAMPLES ---- depends on -> Section 4
  Section 8:  FLEXIBILITY ---- depends on -----> Section 2 (domain signals)
  Section 9:  METRICS & TESTING ---- depends on -> Section 4
```

**Complexity routing:**

| Complexity Level | What to Include | Approximate Token Cost |
|-----------------|-----------------|----------------------|
| **Simple** (single deliverable, clear format) | Required Core only | ~200-400 tokens |
| **Medium** (needs some reasoning or domain depth) | Required Core + Section 3 (Reasoning) | ~400-800 tokens |
| **Standard** (quality matters, iterative refinement needed) | Required Core + Reasoning Layer + Quality Layer | ~800-1200 tokens |
| **Complex** (multi-step, high-stakes, multi-domain) | Full template | ~1200-2000 tokens |

**Rule of thumb:** If your prompt consumes more than 15% of the model's context window, trim optional sections first.

---

## Section 1: Foundation (Identity & Objective)

### SYSTEM_INSTRUCTIONS *(Optional)*

*Why this section matters:* System instructions set behavioral rails that persist across the entire conversation. Use them when you need hard boundaries (safety limits, operating mode) that should never be overridden by user messages.

| Parameter | Value |
|-----------|-------|
| Operating Mode | `[Standard | Restricted | Expert]` |
| Knowledge Cutoff Handling | `[Acknowledge | Redirect | Proceed with caveat]` |
| Safety Boundaries | `[Define absolute limits: what must never be generated, which topics are off-limits, which behaviors are prohibited]` |

**Strategy Declaration**

| Parameter | Value |
|-----------|-------|
| Primary Reasoning Strategy | `[Self-Refine | Chain-of-Thought | Tree-of-Thought | ReAct | Meta-Cognitive | Other]` |
| Strategy Justification | `[Why this strategy fits the task, in one sentence]` |

If using Self-Refine, declare the mandatory phases here:

1. **DRAFT**: Generate initial output
2. **CRITIQUE**: Evaluate draft against quality dimensions
3. **REVISE**: Fix every gap the critique identifies
4. **Delivery Rule**: Never deliver a first-draft output as final

---

### OBJECTIVE_AND_PERSONA **(Required)**

*Why this section matters:* Without a clear objective, the model optimizes for plausibility rather than usefulness. Without a specialized persona, it defaults to a generic voice that lacks domain depth. Together, these two elements determine the direction and character of everything the model produces.

#### Objective

| Element | Description |
|---------|-------------|
| Primary Goal | `[One clear, measurable outcome statement]` |
| Success Looks Like | `[Concrete deliverable description: what the user receives, in what format, with what qualities]` |

**Multi-deliverable success criteria** *(use when the process matters as much as the product)*:

1. **Primary output**: `[The main artifact, e.g., "a production-ready API design document"]`
2. **Process artifact**: `[Critique trail, reasoning log, or methodology explanation]`
3. **Learning artifact**: `[Explanation of decisions so the user learns the craft]`

#### Persona

*The persona is not decoration. It determines vocabulary, reasoning patterns, what the model notices, and what it ignores (see Principle 2). A "Lead Climate Systems Modeler" will flag feedback loops that a generic "scientist" would miss.*

| Element | Description |
|---------|-------------|
| Role | `[Specific job title or expert type, e.g., "Lead Climate Systems Modeler," "Senior Pediatric Oncology Researcher," "Principal Security Architect"]` |
| Identity Traits | `[2-4 characteristics, e.g., "analytical, self-critical, educational, precise"]` |
| Anti-Traits | `[What this persona is NOT, e.g., "not generic, not verbose, not deferential"]` |

**Expanded Expertise Specification** *(use for complex or cross-domain tasks)*:

- **Domain Expertise**: `[Primary field and specific sub-specializations]`
- **Methodological Expertise**: `[Frameworks, techniques, or approaches mastered]`
- **Cross-Domain Expertise**: `[Adjacent fields that inform the primary domain]`
- **Behavioral Expertise**: `[Understanding of how AI models respond to different prompt structures, if applicable]`

**Persona Behavioral Guidance** *(defines how the persona acts under ambiguity, not just what it knows)*:

| Situation | Persona Behavior |
|-----------|-----------------|
| Ambiguous input | `[e.g., "State the ambiguity explicitly, declare the chosen interpretation, proceed, and flag the assumption at the end"]` |
| Insufficient information | `[e.g., "Identify exactly what is missing, explain why it matters, and provide a conditional answer: 'If X, then Y; if Z, then W'"]` |
| Conflicting requirements | `[e.g., "Apply the Conflict Resolution Protocol (Section 5), document the conflict and the resolution in the output"]` |
| Edge case or boundary condition | `[e.g., "Flag it as an edge case, provide the best available answer, and note the confidence level"]` |
| Pushback from user | `[e.g., "Defend the reasoning with evidence, but update the position if the user provides new information that changes the analysis"]` |

---

## Section 2: Context (Situation & Domain)

### CONTEXT **(Required)**

*Why this section matters:* Context determines how the model interprets ambiguity. The same instruction ("make it more concise") means different things in a legal brief vs. a tweet. Without explicit context, the model guesses, and guesses compound (see Principle 1).

| Element | Description |
|---------|-------------|
| Background | `[Why this task exists; relevant history; what problem it solves]` |
| Domain | `[Industry, field, or subject area. Be specific: "pediatric oncology research" not "healthcare"]` |
| Target Audience | `[Who consumes the output; their expertise level; what they need to learn vs. already know]` |
| Inputs Provided | `[Documents, data, or artifacts available. List each with its role in the task.]` |

### Domain Signals (Authoritative Definition)

*This is the single source of truth for domain-adaptive behavior. Section 8 (Flexibility) references these signals but does not redefine them.*

These signals determine how critique, enhancement, and tone adapt to different content types. The model should detect the domain automatically from context, but you can declare it explicitly when the domain is non-obvious or when you want to override the default behavior.

| Domain Type | Critique Focus | Tone Adaptation | Common Failure Modes |
|-------------|----------------|-----------------|---------------------|
| Technical/Code | Edge-case coverage, I/O spec, error handling, architecture, performance | Precision-focused, architecture-aware | Over-abstraction, missing error paths, untested assumptions |
| Creative/Writing | Sensory depth, subtext, stylistic constraints, voice consistency, evocative framing | Evocative, stylistically-aware | Generic descriptions, telling instead of showing, inconsistent voice |
| Research/Factual | Source requirements, verification, citation format, bias awareness, methodological rigor | Rigorous, evidence-focused | Unsupported claims, citation gaps, confirmation bias |
| Teaching/Advisory | Audience calibration, prerequisite assumptions, progressive complexity, success metrics | Scaffolded, progressively complex | Assuming too much prior knowledge, no verification of understanding |
| `[Custom]` | `[Custom critique focus]` | `[Custom tone]` | `[Custom failure modes]` |

### Input Validation Protocol

*What should the model do when the inputs are problematic? Define this upfront so the model does not silently proceed with bad data.*

| Input Condition | Model Behavior |
|----------------|---------------|
| Missing required input | `[e.g., "Name the missing input, explain its importance, and ask for it before proceeding" | "Proceed with stated assumptions"]` |
| Contradictory inputs | `[e.g., "Identify the contradiction, present both interpretations, and ask which to follow" | "Apply Conflict Resolution Protocol"]` |
| Malformed or corrupted input | `[e.g., "Describe what appears to be wrong, attempt to salvage usable content, and flag the uncertainty"]` |
| Input exceeds scope | `[e.g., "Acknowledge the full input, explicitly state which portion falls within scope, and proceed with the in-scope portion only"]` |

---

## Section 3: Reasoning (Cognitive Scaffolding)

*Why this section matters:* Reasoning scaffolding does not just improve output quality. It changes *what kind* of output is possible (see Principle 3). Chain-of-thought enables multi-step logic. Tree-of-thought enables comparison of alternatives. Self-Refine enables quality convergence. Without scaffolding, the model produces its best first-pass guess, which is often adequate but rarely excellent.

### Chain-of-Thought *(Default reasoning pattern)*

| Parameter | Value |
|-----------|-------|
| Activation | `[Always | On complexity threshold | On request]` |
| Visibility | `[Show reasoning | Hide reasoning | Summarize only | Show critique trail as part of output]` |

**Pattern:**

```
-> OBSERVE:  What information is present? What is the core intent?
-> ANALYZE:  What patterns, relationships, gaps, implications exist?
-> DRAFT:    Generate initial output incorporating analysis
-> CRITIQUE: Score against quality dimensions and identify specific gaps
-> REVISE:   Fix each gap with targeted improvements
-> CONCLUDE: Deliver justified, audited answer
```

**When Chain-of-Thought can backfire:** On simple factual lookups or short creative tasks, explicit reasoning steps can make the model overthink, producing hedged or over-qualified output. If the task has one clear answer and no ambiguity, skip the scaffolding.

### Tree-of-Thought *(Optional, use when multiple valid approaches exist)*

| Parameter | Value |
|-----------|-------|
| Trigger | `[When multiple valid approaches exist and the best path is non-obvious]` |
| Depth | `[Levels of sub-branching allowed: 1-3]` |

**Process:**

```
+-- Branch 1: [Approach A with description]
+-- Branch 2: [Approach B with description]
+-- Branch 3: [Approach C with description]
|
+-- Evaluate against: feasibility, quality, efficiency, alignment,
|   insight potential, structural completeness
+-- Select: [Best branch with justification]
```

**When Tree-of-Thought can backfire:** When one approach is clearly superior and alternatives are artificial. Forcing three branches when only one is viable wastes tokens and can cause the model to argue for weak alternatives to fill the structure.

### Self-Refine *(Authoritative definition of the generate-critique-revise cycle)*

*This is the single source of truth for the iterative quality loop. All other sections that reference critique-revise cycles point here.*

| Parameter | Value |
|-----------|-------|
| Trigger | `[Always | When output quality is critical | When first draft is likely insufficient]` |
| Max Cycles | `[2-3]` |
| Quality Threshold | `[See Section 4 for calibrated thresholds]` |
| Delivery Rule | `[Never deliver output from step 1 as final]` |

**The Cycle:**

1. **GENERATE**: Produce initial output using all available context and the persona's expertise.
2. **CRITIQUE**: Evaluate against QUALITY_DIMENSIONS (Section 4).
   - Score each dimension using the calibrated anchors.
   - Document findings: `[CRITIQUE FINDINGS: ...]`
   - For each gap, write a specific, actionable fix (not "improve this" but "replace the generic persona 'data expert' with 'Senior Quantitative Risk Analyst specializing in credit derivatives'").
3. **REVISE**: Address every finding scoring below threshold.
   - Replace generic elements with domain-specialized alternatives.
   - Add missing structural elements.
   - Sharpen vague instructions into specific, actionable directives.
   - Remove additions that add length without cognitive value.
   - Document changes: `[REVISIONS APPLIED: ...]`
4. **VALIDATE**: Re-score all dimensions. If all are at or above threshold, proceed to delivery. Otherwise, repeat from step 2. Do not exceed Max Cycles.

**When Self-Refine can backfire:** On creative/generative tasks where iteration can sand away the distinctive edges that made the first draft interesting. On brainstorming tasks where "wrong" ideas are valuable. On time-sensitive tasks where two good-enough outputs outperform one polished output delivered late. Consider setting the trigger to "When output quality is critical" rather than "Always."

**When to stop early (practical convergence heuristics):**

Since scoring is subjective, use these observable signals instead of trying to measure a precise percentage:

- The revision changes only surface-level wording, not structure or substance.
- The critique identifies no issues that would change the user's experience of the output.
- You find yourself adding hedging language rather than fixing actual gaps.
- The revision introduces new problems at the same rate it fixes old ones.

If any of these signals appear, the output has converged. Further iteration risks over-processing.

### Error Recovery Protocol

*What should the model do when the reasoning process itself breaks down?*

| Failure Mode | Recovery Action |
|-------------|----------------|
| Critique identifies a fundamental misunderstanding of the task | Stop the cycle. Restate your understanding of the task. Ask the user to confirm or correct before continuing. |
| Critique finds a problem that cannot be fixed within the current constraints | Flag the constraint as blocking. Explain what would need to change to fix the problem. Deliver the best possible output with the limitation noted. |
| Revision degrades quality on one dimension while improving another | Document the tradeoff explicitly. Choose the option that best serves the stated Primary Goal (Section 1). Note what was sacrificed and why. |
| The model is uncertain whether the output meets the threshold | Default to delivering with a confidence note rather than iterating further. Over-iteration under uncertainty produces progressively more generic output. |

---

## Section 4: Quality (Dimensions & Calibration)

### QUALITY_DIMENSIONS **(Required when using Self-Refine)**

*Why this section matters:* Without explicit quality dimensions, the critique phase defaults to "does this look good?" which is too vague to produce systematic improvement. Dimensions force the critique to examine specific facets of quality independently, which catches gaps that holistic review misses.

*Why calibration matters:* A score of "85%" is meaningless without anchors. Two people scoring the same output will disagree by 20+ points unless they share concrete reference points. The anchors below make scoring reproducible. When scoring subjectively, use the anchors as comparisons: "Is this output closer to the 60% example or the 95% example?"

| Dimension | Definition | Threshold | Calibration Anchors |
|-----------|------------|-----------|---------------------|
| **Insight Potential** | Does the output force deeper, more specific reasoning than a naive approach? Would it produce meaningfully different results? | >= 85% | **60%**: Output rephrases the request with generic instructions. **80%**: Output adds domain-specific structure that a non-expert would miss. **95%**: Output introduces a reasoning framework or constraint that fundamentally changes the quality of downstream results. |
| **Persona Specificity** | Is the persona a specialized domain role with named expertise, not a generic "expert"? Does it include behavioral guidance? | 100% | **60%**: "You are an expert in data." **80%**: "You are a Senior Data Engineer." **95%**: "You are a Senior Data Engineer specializing in real-time streaming pipelines on Apache Flink, with 8 years of experience debugging backpressure in high-throughput systems. When you encounter ambiguous requirements, you ask clarifying questions before designing." |
| **Structural Completeness** | Are all required elements present: persona, context, constraints, output format, reasoning activation? | >= 90% | **60%**: Has persona and task only. **80%**: Has all five Quick-Start elements but lacks depth. **95%**: All elements present with domain-specific detail, plus reasoning scaffolding and quality criteria. |
| **Constraint Clarity** | Are all instructions specific enough to be followed unambiguously? No vague qualifiers like "be detailed"? | >= 85% | **60%**: "Write a good analysis." **80%**: "Write a 500-word analysis covering causes, impacts, and recommendations." **95%**: "Write a 500-word analysis of Q3 revenue decline. Structure: root cause (with data), downstream impact on three business units, and two actionable recommendations each with estimated ROI." |
| **Intent Fidelity** | Does the output preserve and deepen the original intent without redirecting to a different task? | >= 95% | **60%**: Output addresses a related but different task. **80%**: Output addresses the right task but adds tangential sections. **95%**: Every element directly serves the original intent, and enhancements deepen it rather than broadening it. |
| **Tone Engagement** | Is the output clear, well-suited to its audience, and purposeful? Does it serve the reader or just the structure? | >= 80% | **60%**: Reads like a compliance form. **80%**: Clear and professional, with occasional domain-specific personality. **95%**: Reads like it was written by someone who cares about the craft and wants the reader to succeed. |
| **Process Integrity** | Were all mandatory phases executed? Was the critique phase completed before delivery? | 100% | Binary: either all phases ran, or they did not. |
| `[Custom Dimension]` | `[Definition]` | `[Target]` | `[60% / 80% / 95% anchors]` |

---

## Section 5: Constraints (Rules, Tone & Examples)

*Why this section matters:* Constraints define the boundaries within which the model operates (see Principle 4). Well-chosen constraints reduce the search space and increase output quality. Poorly chosen constraints create contradictions that the model resolves silently and unpredictably.

### CONSTRAINTS **(Required)**

#### DOs

- `[Required behavior or inclusion 1]`
- `[Required behavior or inclusion 2]`
- `[Mandatory standard to maintain]`
- Follow the Self-Refine cycle (Section 3) strictly when activated. Never skip the critique phase.
- State assumptions explicitly when inputs are ambiguous.
- Preserve the user's original intent. Enhance, do not redirect.
- Apply the Input Validation Protocol (Section 2) when inputs are problematic.
- Apply the Error Recovery Protocol (Section 3) when the reasoning process breaks down.

#### DON'Ts

- `[Prohibited action or content 1]`
- `[Prohibited action or content 2]`
- `[Anti-pattern to avoid]`
- Do not add synonyms, filler phrases, or verbose qualifiers that increase length without adding structural complexity or cognitive depth.
- Do not use generic personas without domain specialization.
- Do not skip the internal critique phase for any output.
- Do not add constraints that conflict with each other (see Conflict Resolution below).
- Do not silently resolve ambiguity. Make your interpretation visible.

#### Conflict Resolution Protocol

When constraints contradict each other, resolve using this priority hierarchy. The levels are ordered by scope: broader protective boundaries override narrower operational preferences.

1. **Safety boundaries** (Section 1 SYSTEM_INSTRUCTIONS) override everything. These are non-negotiable limits on what can be generated.
2. **Intent fidelity** (what the user actually asked for) overrides structural rules. The template serves the user's goal, not itself.
3. **Domain conventions** (how the target field actually operates) override generic best practices. A legal brief follows legal conventions even if the template's default formatting differs.
4. **Explicit constraints** (stated directly in the prompt) override inferred ones. What the user wrote takes precedence over what you think they meant.
5. **Specific over general**: when two constraints at the same priority level conflict, the more specific one wins. "Use APA 7th edition citations" overrides "use standard academic citations."

When a conflict cannot be resolved by this hierarchy (e.g., two explicit constraints of equal specificity that contradict each other), flag the conflict in the output and present both options with a recommendation rather than silently choosing one side.

#### Boundaries

| Element | Description |
|---------|-------------|
| Scope | In-scope: `[...]` / Out-of-scope: `[...]` |
| Length | `[Min-Max words/tokens]` |
| Time Sensitivity | `[If applicable]` |

#### Token Budget Guidance

Every section you include consumes context window space. Budget accordingly:

| Template Complexity | Approximate Token Cost | Recommended For |
|--------------------|-----------------------|-----------------|
| Quick-Start only | 100-200 tokens | Simple, well-defined tasks |
| Required Core sections | 300-600 tokens | Standard tasks with clear domains |
| Core + Reasoning layer | 600-1000 tokens | Tasks requiring multi-step thinking |
| Core + Quality layer | 800-1200 tokens | Tasks where output quality is critical |
| Full template | 1200-2000 tokens | Complex, high-stakes, multi-domain tasks |

**How to estimate token count:** As a rough heuristic, 1 token is approximately 4 characters or 0.75 words in English. Most text editors can show word count; multiply by 1.33 for an approximate token count. For precise measurement, use your model provider's tokenizer tool if available.

---

### TONE_AND_STYLE *(Optional)*

*Why this section matters:* Tone is not just about how the output sounds. It affects how the audience receives and trusts the information. A rigorous research tone builds credibility with academics. A conversational tone reduces friction for non-experts. Mismatched tone undermines even correct content.

| Element | Value |
|---------|-------|
| Voice | `[Formal | Professional | Conversational | Technical | Friendly]` |
| Register | `[Academic | Business | Casual | Instructional]` |
| Personality | `[e.g., "methodical and precise in analysis, genuinely enthusiastic about the craft"]` |

**Domain-Adaptive Tone Shifting** *(triggers automatically based on Domain Signals in Section 2)*:

Tone adaptation rules are defined in the Domain Signals table (Section 2). Override them here only if you need behavior that differs from the domain default.

| Override Condition | Custom Adaptation |
|-------------------|-------------------|
| `[Condition]` | `[Custom tone shift]` |
| User requests minimal output | Essential additions only; note what was intentionally omitted |

---

### FEW_SHOT_EXAMPLES *(Optional but high-impact)*

*Why this section matters:* A single good example communicates more about desired output quality than ten lines of abstract instructions. Examples ground abstract quality dimensions in concrete reality. Prioritize one strong positive example over multiple mediocre ones.

#### Positive Example

**Input**: `[Sample input demonstrating a common case]`

**Output**: `[Ideal response matching all requirements. If Self-Refine is active, include the critique trail and process explanation.]`

**Why this works**: `[Reference specific QUALITY_DIMENSIONS that are satisfied and explain how]`

#### Edge Case Example *(Optional)*

**Input**: `[Tricky or boundary-testing input]`

**Output**: `[Correct handling of the edge case]`

**Why this works**: `[How domain adaptation shifted the critique focus, how ambiguity was resolved]`

#### Anti-Example *(Optional)*

**Input**: `[Input that might cause errors or trigger anti-patterns]`

**Wrong Output**: `[What to avoid, e.g., adjective stacking, skipped critique, generic persona, length without structure]`

**Right Output**: `[Correct alternative with specific improvements noted]`

**Why it's wrong**: `[Which QUALITY_DIMENSIONS the wrong output violates and why]`

---

## Section 6: Iteration (Refinement Loop)

### ITERATIVE_PROCESS **(Required when using Self-Refine)**

*Why this section matters:* This section configures the Self-Refine cycle defined in Section 3. It does not redefine the cycle. It sets the operational parameters (how many iterations, when to stop, when to ask for feedback) that govern how the cycle runs for this specific prompt.

| Parameter | Value |
|-----------|-------|
| Max Iterations | `[2-3. Enough for quality convergence, not so many the output becomes over-processed.]` |
| Quality Threshold | `[Default: 85% across all dimensions. Customize per task using the calibration anchors in Section 4.]` |
| Convergence Rule | `[Stop early when observable convergence signals appear. See Section 3 "When to stop early" for specific heuristics.]` |
| User Checkpoints | `[After iteration N, pause for feedback: Yes/No]` |
| Delivery Rule | `[Never deliver the output of step 1 as final without completing step 2+]` |

**Pre-Delivery Checklist:**

- [ ] All mandatory phases executed (generate-critique-revise)
- [ ] All QUALITY_DIMENSIONS at or above threshold
- [ ] Output adds cognitive depth, not just length
- [ ] All required structural elements present
- [ ] Persona is domain-specialized, not generic
- [ ] Persona behavioral guidance was followed for any ambiguity encountered
- [ ] Original intent preserved and deepened, not redirected
- [ ] Process documentation included and accurate
- [ ] No conflicting or redundant constraints (or conflicts are flagged per the Conflict Resolution Protocol)
- [ ] Input Validation Protocol was applied if inputs were problematic
- [ ] Factual accuracy verified
- [ ] Format matches specification
- [ ] Tone consistent throughout

**Final Pass Actions:**

- Verify output reads as a coherent instruction set, not a disjointed list.
- Remove redundancy while preserving structural completeness.
- Confirm critique trail accurately reflects changes made.
- Ensure domain-specific terminology is used correctly.
- Add summary if output length exceeds 800 words.

---

## Section 7: Output (Format & Delivery)

*Why this section matters:* Format is not cosmetic. It determines whether the audience can find, parse, and act on the information you are delivering (see Principle 3). A perfect analysis in the wrong format is a failed deliverable.

### RESPONSE_FORMAT **(Required)**

| Element | Value |
|---------|-------|
| Structure | `[Narrative | Sectioned | Bullet-list | Hybrid]` |
| Markup | `[Markdown | Plain | HTML | JSON | Code | XML]` |
| Length Target | `[X-Y words. See Complexity-Scaled Length Guidance below.]` |

**Process-Inclusive Template** *(use when Self-Refine is active and the process is part of the deliverable)*:

```markdown
## Draft / Initial Output
[Content with annotations showing what was added and why]

## Critique
[Specific issues identified, each with ISSUE and FIX sub-items]

## Final Output
Iterations: [N]
[Production-ready output]

## Process Summary
[Numbered list of improvement types applied with domain terminology]
```

**Complexity-Scaled Length Guidance:**

| Complexity | Output Length | Total Response (with process) |
|------------|-------------|-------------------------------|
| Simple tasks | 50-150 words | 200-400 words |
| Standard tasks | 150-500 words | 400-700 words |
| Complex tasks | 500+ words (justify if exceeding) | 700-1000+ words |

### Multi-Turn Prompt Guidance *(Optional, for conversational and agentic workflows)*

The rest of this template assumes single-shot prompts (one input, one output). If your prompt will be used in a multi-turn conversation or an agentic loop, apply these additional considerations:

**State management:** Decide what the model needs to remember across turns. Include a `[CONVERSATION STATE: ...]` block that specifies which information persists and which resets.

**Turn-level instructions vs. conversation-level instructions:** Instructions in SYSTEM_INSTRUCTIONS persist across all turns. Instructions in CONTEXT or CONSTRAINTS may need to be restated or summarized if the conversation exceeds the model's effective attention span (typically the last ~4000 tokens in long conversations).

**Escalation and handoff:** Define when the model should stop iterating autonomously and return control to the user. Common triggers: confidence drops below a threshold, the task scope changes mid-conversation, or the model encounters information it cannot verify.

**Agentic loops:** If the model is calling tools or executing actions, define the maximum number of autonomous steps before requiring user confirmation. Include rollback instructions for when an action produces unexpected results.

---

## Section 8: Flexibility (Adaptation & Overrides)

*Why this section matters:* No template can anticipate every situation. This section defines how the model should adapt when the task does not fit the default structure. It references Domain Signals (Section 2) for domain-adaptive behavior and adds override mechanisms for user customization.

### FLEXIBILITY *(Optional)*

#### Conditional Logic

*Domain-adaptive critique and tone rules are defined in the Domain Signals table (Section 2). The conditions below cover situations outside domain adaptation.*

| Condition | Action |
|-----------|--------|
| User requests minimal output | Provide only highest-impact additions; note what was intentionally omitted |
| Ambiguity would lead to fundamentally different outputs | Ask ONE clarifying question before proceeding |
| User specifies target model | Note model-specific optimization considerations in process summary |
| Task is simple enough that Self-Refine would over-process it | Use Quick-Start structure; skip the critique cycle |
| Input fails validation (see Section 2) | Apply Input Validation Protocol before proceeding |
| Reasoning process breaks down | Apply Error Recovery Protocol (Section 3) |

#### User Overrides

**Adjustable Parameters**: `enhancement-depth` (minimal|standard|comprehensive), `target-domain`, `output-style` (output-only|full-process), `max-length`, `quality-threshold`, `max-iterations`, `formality`, `focus-areas`

**Syntax**: `Override: [parameter]=[value]`

#### Defaults (when unspecified)

- Standard enhancement depth
- Domain inferred from content via Domain Signals (Section 2)
- Full-process output (Draft + Critique + Final + Process Summary)
- Quality threshold: 85% across all dimensions
- Max iterations: 3
- No model-specific optimization

---

## Section 9: Measurement, Testing & Closure

*Why this section matters:* Metrics tell you whether your prompt is working. Testing tells you whether it works reliably across different inputs, not just the one you had in mind when you wrote it. Without both, you are guessing about prompt quality.

### METRICS **(Required for production prompts)**

| Metric | Measurement Method | Target |
|--------|-------------------|--------|
| Insight Potential Gain | Output provokes deeper reasoning than naive approach | >= 85% |
| Persona Specificity | Domain-specialized role with behavioral guidance, not generic "expert" | 100% |
| Structural Completeness | All required elements present | >= 90% |
| Constraint Clarity | Instructions specific and unambiguous | >= 85% |
| Intent Fidelity | Original intent preserved and deepened | >= 95% |
| Process Integrity | All mandatory phases executed before delivery | 100% |
| Process Transparency | Enhancement process documented with domain terminology | >= 90% |
| User Satisfaction | User can understand and learn from the process | >= 4/5 |
| Iteration Reduction | Drafts needed before threshold met | <= 3 |

**Improvement Target**: >= 20% quality improvement vs. unstructured approach.

### PROMPT_TESTING *(Recommended for production prompts)*

Before deploying a prompt built with this template, test it against these conditions:

**Variation testing:** Run the prompt with 3-5 different inputs that represent the range of expected use cases. Verify the output quality is consistent, not just good for the input you wrote the prompt around.

**Edge case testing:** Run the prompt with at least one input that is at the boundary of scope (e.g., minimal input, maximum complexity, ambiguous phrasing). Verify the model handles it gracefully per the Input Validation Protocol.

**Adversarial testing:** Run the prompt with one input designed to confuse or misdirect (e.g., contradictory instructions, off-topic content embedded in valid input). Verify the model does not silently produce garbage.

**Regression testing:** After modifying any section of the prompt, re-run at least 2 of your original test cases to verify the change did not degrade previously working behavior.

**What to look for in test results:**

- Does the persona hold consistently, or does it drift toward generic?
- Are constraints followed across all test cases, or only the easy ones?
- Does the output format match the specification every time?
- When the model encounters ambiguity, does it follow the behavioral guidance or revert to defaults?

---

### RECAP **(Required)**

**Primary Objective**: `[Restate in 1 sentence: what must be accomplished]`

**Critical Requirements:**

1. `[Most important must-have, e.g., "Never skip the critique phase"]`
2. `[Second priority, e.g., "Every output must include all five core elements: persona, context, constraints, output format, reasoning activation"]`
3. `[Third priority, e.g., "Explain the types of improvements using domain terminology"]`

**Absolute Avoids:**

1. `[Top anti-pattern, e.g., "Adjective stacking without structural improvement"]`
2. `[Second anti-pattern, e.g., "Generic personas without domain specialization"]`

**Final Reminder**: `[The one thing that must not be forgotten, e.g., "A great output is not a longer output. It is a more structured, more specific, more thought-provoking output. Add cognitive scaffolding, not filler."]`

---

## Appendix A: Self-Versioning Protocol

This template is designed to be improved using its own methodology. To produce the next version:

1. **Treat the current template as the input** to the OBJECTIVE_AND_PERSONA + CONTEXT sections.
2. **Set the persona** to "Prompt Engineering Architect specializing in LLM instruction design and meta-cognitive frameworks."
3. **Run the Self-Refine cycle** (Section 3) against the QUALITY_DIMENSIONS (Section 4), scoring the template itself.
4. **Document the critique log** at the top of the new version, following the format established in the "Critique Log" section.
5. **Apply revisions** and increment the version number.
6. **Run at least Variation and Edge Case testing** (Section 9) on the revised template by applying it to two different prompt-building tasks and verifying the output quality.

This ensures each version of the template is an auditable improvement over the last, with explicit reasoning for every change.

## Appendix B: Version History

| Version | Key Changes | Dimensions Improved |
|---------|------------|-------------------|
| v1.0 | Initial template | Baseline |
| v2.0 | Added Self-Refine methodology, dimensional scoring, domain-adaptive critique, cognitive scaffolding | Insight Potential, Process Integrity |
| v3.0 | Consolidated critique-revise redundancy, added Quick-Start, calibrated scoring anchors, added conflict resolution, token budget guidance, self-versioning protocol | Structural Completeness, Constraint Clarity, Process Integrity, Tone Engagement |
| v4.0 | Added Principles section, Input Validation, Error Recovery, multi-turn guidance, Prompt Testing, persona behavioral guidance, strategy failure modes, consolidated domain signal duplication, restored universal template form | Insight Potential, Persona Specificity, Structural Completeness, Constraint Clarity, Tone Engagement |
