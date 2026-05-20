# Gemini Visual Generation Prompt — Figure 2: Single-Path Strategy Comparison

## Instructions for Gemini

Create a set of four side-by-side horizontal flowcharts comparing single-path reasoning strategies. Each flowchart should show the information flow from input to output.

### Layout
Four rows, each representing one strategy. Aligned left-to-right with consistent node sizing.

### Flowchart 1: Chain-of-Thought (CoT)
```
[Prompt + Examples] --> [Step 1] --> [Step 2] --> [Step 3] --> [Answer]
```
- Highlight: The "Examples" box is colored blue, indicating few-shot exemplars
- Label the intermediate steps "Reasoning Step 1, 2, 3"

### Flowchart 2: Zero-Shot CoT
```
[Prompt + "Let's think step by step"] --> [Step 1] --> [Step 2] --> [Step 3] --> [Answer]
```
- Highlight: The trigger phrase "Let's think step by step" in a green callout
- Same intermediate steps but no examples box

### Flowchart 3: Plan-and-Solve
```
[Prompt] --> [PLAN: outline steps] --> [Execute Step 1] --> [Execute Step 2] --> [Execute Step 3] --> [Answer]
```
- Highlight: The PLAN node is distinctly colored (orange), showing it is an explicit planning phase before execution

### Flowchart 4: Program-of-Thought
```
[Prompt] --> [Generate Code] --> [Execute Code] --> [Return Result]
```
- Highlight: The "Execute Code" node has a gear/terminal icon and a different shape (rectangle with double borders) indicating external execution
- An arrow from "Execute Code" labeled "runtime environment" pointing to a small box labeled "Python/etc."

### Style
- Clean, professional, suitable for academic publication
- Consistent color scheme: input nodes (light gray), reasoning nodes (light blue), output nodes (light green), special nodes (colored per highlights above)
- Rounded rectangles for all nodes
- Arrows with small labels where noted
- Title: "Figure 2. Information Flow Comparison Across Single-Path Reasoning Strategies"
- Sans-serif font

### Output
- PNG at 300 DPI, approximately 8 inches wide by 6 inches tall
