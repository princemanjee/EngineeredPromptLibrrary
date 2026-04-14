# Context Engineering Template v2.0

> Upgraded from v1.0 with Self-Refine methodology, dimensional scoring, domain-adaptive critique, and cognitive scaffolding integration.
>
> **Usage**: Copy relevant sections, customize placeholders `[...]`, delete unused optional blocks. Sections marked **(Required)** must be present in every production prompt.

---

## Section 1: Foundation (Core Identity & Setup)

### SYSTEM_INSTRUCTIONS *(Optional)*

Pre-conversation behavioral rules; invisible to typical users.

| Parameter | Value |
|-----------|-------|
| Operating Mode | `[Standard \| Restricted \| Expert]` |
| Knowledge Cutoff Handling | `[Acknowledge \| Redirect \| Proceed with caveat]` |
| Safety Boundaries | `[Define absolute limits — what must never be generated, what topics are off-limits, what behaviors are prohibited]` |

**v2.0: Primary Strategy Declaration**

| Parameter | Value |
|-----------|-------|
| Primary Reasoning Strategy | `[Self-Refine \| Chain-of-Thought \| Tree-of-Thought \| ReAct \| Meta-Cognitive \| Other]` |
| Strategy Justification | `[Why this strategy fits the task — one sentence]` |

**v2.0: Mandatory Phases**

Define non-skippable phases. Example for Self-Refine:

1. **Phase 1**: DRAFT — generate initial output
2. **Phase 2**: CRITIQUE — evaluate draft against quality dimensions
3. **Phase 3**: REVISE — fix every gap the critique identifies
4. **Delivery Rule**: Never deliver a first-draft output as final

---

### OBJECTIVE_AND_PERSONA **(Required)**

#### Objective

| Element | Description |
|---------|-------------|
| Primary Goal | `[One clear, measurable outcome statement]` |
| Success Looks Like | `[Concrete deliverable description — what the user receives, in what format, with what qualities]` |

**v2.0: Multi-deliverable success criteria**

1. **Primary output** — `[the main artifact]`
2. **Process artifact** — `[critique trail, reasoning log, or methodology explanation]`
3. **Learning artifact** — `[explanation of decisions so the user learns the craft]`

#### Persona

| Element | Description |
|---------|-------------|
| Role | `[Specific job title / Expert type, e.g., "Lead Climate Systems Modeler"]` |
| Identity Traits | `[2-4 characteristics, e.g., "analytical, self-critical, educational, precise"]` |
| Anti-Traits | `[What this persona is NOT — e.g., "not generic, not verbose, not deferential"]` |

**v2.0: Expanded Expertise Specification**

- **Domain Expertise**: `[Primary field and specific sub-specializations]`
- **Methodological Expertise**: `[Frameworks, techniques, or approaches mastered]`
- **Cross-Domain Expertise**: `[Adjacent fields that inform the primary domain]`
- **Behavioral Expertise**: `[Understanding of how AI models respond to different prompt structures — if applicable]`

---

### CONTEXT **(Required)**

| Element | Description |
|---------|-------------|
| Background | `[Why this task exists; relevant history; what problem it solves]` |
| Domain | `[Industry/field/subject area — be specific, not just "technology"]` |
| Target Audience | `[Who consumes output; their expertise level; what they need to learn vs. already know]` |
| Inputs Provided | `[Documents, data, or artifacts available — list each with its role]` |

**v2.0: Domain-Adaptive Context (Domain Signals)**

These signals determine how critique and enhancement adapt:

| Domain Type | Critique Focus |
|-------------|----------------|
| Technical/Code | Edge-case coverage, I/O spec, error handling, architecture |
| Creative/Writing | Sensory depth, subtext, stylistic constraints, evocative framing |
| Research/Factual | Source requirements, verification, citation format, bias awareness |
| Teaching/Advisory | Audience calibration, prerequisites, progressive complexity |
| `[Custom]` | `[Custom adaptation rules]` |

---

## Section 2: Execution (Instructions & Reasoning)

### INSTRUCTIONS **(Required)**

#### Phase 1: Understand

1. Parse and confirm understanding of inputs — identify core intent
2. Determine the target domain and applicable domain signals
3. Identify what is missing: persona? context? constraints? output format? reasoning activation? success criteria?
4. If ambiguity would lead to fundamentally different outputs, ask **ONE** clarifying question before proceeding. State assumptions explicitly when proceeding without clarification.

#### Phase 2: Draft *(v2.0)*

5. Generate initial output incorporating all required structural elements
6. Required elements checklist for the draft:
   - [ ] Specialized persona (not generic "expert")
   - [ ] Contextual framing (why this matters; what situation the output serves)
   - [ ] Structural constraints (format, length, required sections)
   - [ ] Reasoning activation (chain-of-thought, step-by-step, analytical framework)
   - [ ] Success criteria (what great looks like vs. adequate)

#### Phase 3: Critique *(v2.0)*

7. Run internal audit against quality dimensions (see [Quality Dimensions](#quality_dimensions-required))
8. Score each dimension 0-100%
9. Document findings explicitly: `[CRITIQUE FINDINGS: ...]`
10. Identify specific gaps with actionable fix descriptions

#### Phase 4: Revise *(v2.0)*

11. Address every critique finding:
    - Replace generic elements with domain-specialized alternatives
    - Add missing structural elements
    - Sharpen vague instructions into specific, actionable directives
    - Remove additions that add length without cognitive value
12. Document revisions: `[REVISIONS APPLIED: ...]`
13. Repeat Critique-Revise cycle until all dimensions >= threshold (max iterations defined in [Iterative Process](#iterative_process-required))

#### Phase 5: Deliver

14. Present the draft with annotations showing what was added and why
15. Present critique findings — specific improvements and engineering types applied
16. Deliver final output — production-ready version
17. Include process summary describing steps and principles applied

---

## Section 3: Reasoning (Cognitive Scaffolding)

### CHAIN_OF_THOUGHT

| Parameter | Value |
|-----------|-------|
| Activation | `[Always \| On complexity threshold \| On request]` |
| Visibility | `[Show reasoning \| Hide reasoning \| Summarize only \| Show critique trail as part of output]` |

**Reasoning Pattern:**

```
-> OBSERVE:  What information is present? What is the core intent?
-> ANALYZE:  What patterns, relationships, gaps, implications exist?
-> DRAFT:    Generate initial output incorporating analysis
-> CRITIQUE: Score against quality dimensions — identify specific gaps
-> REVISE:   Fix each gap with targeted improvements
-> CONCLUDE: Deliver justified, audited answer
```

---

### TREE_OF_THOUGHT *(Optional)*

| Parameter | Value |
|-----------|-------|
| Trigger | `[When multiple valid approaches exist]` |
| Depth | `[Levels of sub-branching allowed: 1-3]` |

**Process:**

```
├─ Branch 1: [Approach A - description]
├─ Branch 2: [Approach B - description]
├─ Branch 3: [Approach C - description]
│
└─ Evaluate: [Criteria: feasibility, quality, efficiency, alignment,
              insight potential, structural completeness]
   └─ Select: [Best branch with justification]
```

---

### SELF_REFINE *(v2.0, Optional)*

Generate-Critique-Revise cycle with dimensional scoring.

| Parameter | Value |
|-----------|-------|
| Trigger | `[Always \| When output quality is critical \| When first draft is likely insufficient]` |
| Max Cycles | `[2-3]` |
| Quality Threshold | `[85% across all dimensions]` |
| Delivery Rule | `[Never deliver output from step 1 as final]` |

**Cycle:**

1. **GENERATE**: Produce initial output using all available context
2. **CRITIQUE**: Evaluate against defined QUALITY_DIMENSIONS
   - Score each dimension 0-100%
   - Document findings as `[CRITIQUE FINDINGS: ...]`
3. **REVISE**: Address every finding scoring below threshold
   - Document changes as `[REVISIONS APPLIED: ...]`
4. **VALIDATE**: Re-score. If all dimensions >= threshold, deliver. If not, repeat from step 2.

---

## Section 4: Integration (Tools & External Resources)

### TOOL_INTEGRATION *(Optional)*

| Tool Name | Purpose | Invocation Syntax |
|-----------|---------|-------------------|
| `[tool_1]` | `[what it does]` | `[how to call it]` |
| `[tool_2]` | `[what it does]` | `[how to call it]` |

**Usage Rules:**

- **Prefer**: `[When to use tools vs. internal knowledge]`
- **Validate**: `[How to verify tool outputs]`
- **Fallback**: `[Behavior when tool fails/unavailable]`

---

## Section 5: Quality (Constraints, Calibration & Dimensions)

### CONSTRAINTS **(Required)**

#### DOs

- `[Required behavior/inclusion 1]`
- `[Required behavior/inclusion 2]`
- `[Mandatory standard to maintain]`
- Follow the generate-critique-revise cycle strictly — never skip the critique phase
- State assumptions explicitly when inputs are ambiguous
- Preserve the user's original intent — enhance, do not redirect

#### DONTs

- `[Prohibited action/content 1]`
- `[Prohibited action/content 2]`
- `[Anti-pattern to avoid]`
- Do not add synonyms, filler phrases, or verbose qualifiers that increase length without adding structural complexity or cognitive depth
- Do not use generic personas without domain specialization
- Do not skip the internal critique phase for any output
- Do not add constraints that conflict with each other

#### Boundaries

| Element | Description |
|---------|-------------|
| Scope | In-scope: `[...]` / Out-of-scope: `[...]` |
| Length | `[Min-Max words/tokens — scale with task complexity]` |
| Time Sensitivity | `[If applicable]` |

**v2.0: Complexity Scaling**

| Complexity | Treatment |
|------------|-----------|
| Simple tasks | Minimal enhancement — highest-impact additions only |
| Standard tasks | Full structural treatment |
| Complex tasks | Comprehensive scaffolding with multiple reasoning strategies |

---

### TONE_AND_STYLE *(Optional)*

| Element | Value |
|---------|-------|
| Voice | `[Formal \| Professional \| Conversational \| Technical \| Friendly]` |
| Register | `[Academic \| Business \| Casual \| Instructional]` |
| Personality | `[e.g., "methodical and precise in analysis, enthusiastic about the craft"]` |

**v2.0: Domain-Adaptive Tone Shifting**

| Condition | Adaptation |
|-----------|------------|
| Technical/code input | Shift to precision-focused, architecture-aware tone |
| Creative/writing input | Shift to evocative, stylistically-aware tone |
| Research/factual input | Shift to rigorous, evidence-focused tone |
| Teaching/advisory input | Shift to scaffolded, progressively complex tone |
| User requests minimal output | Reduce to essential additions only; note omissions |

---

### QUALITY_DIMENSIONS **(Required)** {#quality_dimensions-required}

Scoring rubric for the critique phase. Customize dimensions per task; these are the recommended defaults.

| Dimension | Definition | Threshold |
|-----------|------------|-----------|
| Insight Potential | Does the output force deeper, more specific reasoning than a naive approach? Would it produce meaningfully different results? | >= 85% |
| Persona Specificity | Is the persona a specialized domain role with named expertise, not a generic "expert"? | 100% |
| Structural Completeness | Are all required elements present: persona, context, constraints, output format, reasoning activation? | >= 90% |
| Constraint Clarity | Are all instructions specific enough to be followed unambiguously? No vague qualifiers like "be detailed"? | >= 85% |
| Intent Fidelity | Does the output preserve and deepen the original intent without redirecting to a different task? | >= 95% |
| Tone Engagement | Is the output inspiring and thought-provoking, or merely bureaucratic? Does it serve its audience? | >= 80% |
| Process Integrity | Were all mandatory phases executed? Was the critique phase completed before delivery? | 100% |
| `[Custom Dimension]` | `[Definition]` | `[Target]` |

---

### FEW_SHOT_EXAMPLES

#### Positive Example

**Input**: `[Sample input demonstrating common case]`

**Output**: `[Ideal response matching all requirements — including critique trail and process explanation if Self-Refine is the primary strategy]`

**Why this works**: `[Explicit quality markers — reference specific dimensions from QUALITY_DIMENSIONS that are satisfied]`

#### Edge Case Example *(Optional)*

**Input**: `[Tricky or boundary-testing input]`

**Output**: `[Correct handling of edge case]`

**Why this works**: `[Specific handling demonstrated — e.g., how domain adaptation shifted the critique focus, how ambiguity was resolved]`

#### Anti-Example *(Optional)*

**Input**: `[Input that might cause errors or trigger anti-patterns]`

**Wrong Output**: `[What to avoid — e.g., adjective stacking, skipped critique, generic persona, length without structure]`

**Right Output**: `[Correct alternative with specific improvements noted]`

**Why it's wrong**: `[Which QUALITY_DIMENSIONS the wrong output violates and why]`

---

## Section 6: Refinement (Iteration & Polish)

### ITERATIVE_PROCESS **(Required)** {#iterative_process-required}

Self-improvement loop aligned with QUALITY_DIMENSIONS.

**Cycle:**

1. **DRAFT** -> Generate initial output incorporating all required elements
2. **EVALUATE** -> Score against QUALITY_DIMENSIONS:
   - `[Dimension 1]`: `[0-100%]`
   - `[Dimension 2]`: `[0-100%]`
   - `[Dimension N]`: `[0-100%]`
   - Document as: `[CRITIQUE FINDINGS: ...]`
3. **REFINE** -> Address all dimensions scoring below threshold:
   - Low `[Dimension]`: `[specific fix strategy]`
   - Document as: `[REVISIONS APPLIED: ...]`
4. **VALIDATE** -> Re-score all dimensions. Confirm all >= threshold. Repeat if not.

| Parameter | Value |
|-----------|-------|
| Max Iterations | `[2-3 — enough for quality, not so many the output becomes over-processed]` |
| Quality Threshold | `[85% across all dimensions — customize per task]` |
| User Checkpoints | `[After iteration N, pause for feedback: Yes/No]` |
| Delivery Rule | `[Never deliver the output of step 1 as final without completing step 2+]` |

---

### POLISH_FOR_PUBLICATION

**Pre-Delivery Checklist:**

- [ ] All mandatory phases executed (generate-critique-revise)
- [ ] All QUALITY_DIMENSIONS at or above threshold
- [ ] Output genuinely adds cognitive depth, not just length
- [ ] All required structural elements present
- [ ] Persona is domain-specialized, not generic
- [ ] Original intent preserved — output deepens, not redirects
- [ ] Process documentation included and accurate
- [ ] No conflicting or redundant constraints
- [ ] Factual accuracy verified
- [ ] Format matches specification
- [ ] Tone consistent throughout

**Final Pass Actions:**

- Verify output reads as a coherent instruction set, not a disjointed list
- Remove redundancy (but preserve structural completeness)
- Confirm critique trail accurately reflects changes made
- Ensure domain-specific terminology is used correctly
- Add summary if output length exceeds threshold

---

## Section 7: Output (Format & Delivery)

### RESPONSE_FORMAT **(Required)**

| Element | Value |
|---------|-------|
| Structure | `[Narrative \| Sectioned \| Bullet-list \| Hybrid]` |
| Markup | `[Markdown \| Plain \| HTML \| JSON \| Code \| XML]` |
| Length Target | `[X-Y words — scale with task complexity] \| [Flexible with justification]` |

**v2.0: Process-Inclusive Template**

For Self-Refine tasks, include critique and revision sections in the template:

```markdown
## [Section 1: Draft / Initial Output]
[Content with annotations showing what was added and why]

## [Section 2: Critique]
[Specific issues identified — each with ISSUE and FIX sub-items]

## [Section 3: Final Output]
Iterations: [N]
[Production-ready output]

## [Section 4: Process Summary]
[Numbered list of improvement types applied with domain terminology]
```

**v2.0: Complexity-Scaled Length Guidance**

| Complexity | Output Length | Total Response (with process) |
|------------|-------------|-------------------------------|
| Simple tasks | 50-150 words | 200-400 words |
| Standard tasks | 150-500 words | 400-700 words |
| Complex tasks | 500+ words (justify if exceeding) | 700-1000+ words |

---

## Section 8: Flexibility (Adaptation & Overrides)

### FLEXIBILITY

#### Conditional Logic

| Condition | Action |
|-----------|--------|
| Technical/code input | Shift critique to edge-cases, I/O spec, error handling, architecture |
| Creative/writing input | Shift critique to sensory depth, subtext, stylistic constraints, evocative framing |
| Research/factual input | Shift critique to source requirements, verification, citation format, bias awareness |
| Teaching/advisory input | Shift critique to audience calibration, prerequisites, progressive complexity, success metrics |
| User requests minimal output | Provide only highest-impact additions; note what was intentionally omitted |
| Ambiguity → fundamentally different outputs | Ask ONE clarifying question before proceeding |
| User specifies target model | Note model-specific optimization considerations in process summary |
| User specifies `[Y]` | Override default with `[Y]` |

#### User Overrides

**Adjustable Parameters**: `enhancement-depth` (minimal|standard|comprehensive), `target-domain`, `output-style` (output-only|full-process), `max-length`, `quality-threshold`, `max-iterations`, `formality`, `focus-areas`

**Syntax**: `Override: [parameter]=[value]`

#### Defaults

When unspecified, assume:
- Standard enhancement depth
- Domain inferred from content
- Full-process output (Draft + Critique + Final + Process Summary)
- Quality threshold: 85% across all dimensions
- Max iterations: 3
- No model-specific optimization

---

## Section 9: Measurement & Closure

### METRICS **(Required)**

| Metric | Measurement Method | Target |
|--------|-------------------|--------|
| Insight Potential Gain | Output provokes deeper reasoning than naive approach | >= 85% |
| Persona Specificity | Domain-specialized role, not generic "expert" | 100% |
| Structural Completeness | All required elements present | >= 90% |
| Constraint Clarity | Instructions specific and unambiguous | >= 85% |
| Intent Fidelity | Original intent preserved and deepened | >= 95% |
| Process Integrity | All mandatory phases executed before delivery | 100% |
| Process Transparency | Enhancement process documented with domain terminology | >= 90% |
| User Satisfaction | User can understand and learn from the process | >= 4/5 |
| Iteration Reduction | Drafts needed before threshold met | <= 3 |

**Improvement Target**: >= 20% quality improvement vs. unstructured approach

---

### RECAP **(Required)**

**Primary Objective**: `[Restate in 1 sentence — what must be accomplished]`

**Critical Requirements:**

1. `[Most important must-have — e.g., "Never skip the critique phase"]`
2. `[Second priority — e.g., "Every output must include all five core elements: persona, context, constraints, output format, reasoning activation"]`
3. `[Third priority — e.g., "Explain the types of improvements using domain terminology"]`

**Absolute Avoids:**

1. `[Top anti-pattern — e.g., "Adjective stacking without structural improvement"]`
2. `[Second anti-pattern — e.g., "Generic personas without domain specialization"]`

**Final Reminder**: `[The one thing that must not be forgotten — e.g., "A great output is not a longer output — it is a more structured, more specific, more thought-provoking output. Add cognitive scaffolding, not filler."]`
