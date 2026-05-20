# Gemini Visual Generation Prompt — Figure 4: Strategy Selection Decision Flowchart

## Instructions for Gemini

Create a professional decision tree flowchart implementing the six-step strategy selection framework.

### Decision Tree Structure

```
START
  |
  v
[Does this task require external tools?]
  |YES --> [Is the full tool-call plan knowable upfront?]
  |            |YES --> {ReWOO}
  |            |NO  --> {ReAct}
  |NO
  v
[Is factual accuracy the primary risk?]
  |YES --> {Add Chain-of-Verification to selected strategy}
  |NO
  v
[Is the task decomposable into subtasks?]
  |YES --> [Are subtasks hierarchical (each depends on prior)?]
  |            |YES --> {Least-to-Most}
  |            |NO  --> [Is it a long document with parallel sections?]
  |                        |YES --> {Skeleton-of-Thought}
  |                        |NO  --> {Plan-and-Solve}
  |NO
  v
[Does exploring multiple paths add value?]
  |YES --> [Is the task creative/strategic with no clear path?]
  |            |YES --> {Tree of Thoughts}
  |            |NO  --> {Self-Consistency}
  |NO
  v
[Is the domain math, code, or formal reasoning?]
  |YES --> [Is code execution available?]
  |            |YES --> {Program-of-Thought}
  |            |NO  --> {CoT + Self-Consistency}
  |NO
  v
[Is the task complex?]
  |YES --> {Chain-of-Thought}
  |NO  --> {Zero-Shot CoT}
```

### Color Coding
- Decision diamonds: Light blue
- Terminal strategy nodes: Color by family
  - Single-path (CoT, Zero-Shot CoT, Plan-and-Solve, PoT): Blue
  - Multi-path (Self-Consistency, ToT): Orange
  - Decomposition (Least-to-Most, Skeleton-of-Thought): Green
  - Tool-use (ReAct, ReWOO): Purple
  - Verification (CoVe): Yellow/Gold — shown as an overlay/modifier, not a terminal

### Style
- Clean flowchart suitable for academic publication
- Diamond shapes for decisions, rounded rectangles for strategy recommendations
- Yes/No labels on all branches
- Flow direction: top to bottom with horizontal branching
- Title: "Figure 4. Strategy Selection Decision Flowchart"
- Sans-serif font

### Output
- PNG at 300 DPI, approximately 8 inches wide by 10 inches tall (portrait orientation for the tall tree)
