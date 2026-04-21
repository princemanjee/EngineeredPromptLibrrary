# Gemini Visual Generation Prompt — Figure 5: Strategy Cost-Complexity Matrix

## Instructions for Gemini

Create a 2x2 matrix diagram showing which strategy tier is appropriate for different combinations of task complexity and accuracy requirements.

### Matrix Structure

|  | **Low Accuracy Requirements** | **High Accuracy Requirements** |
|---|---|---|
| **Low Task Complexity** | **Quadrant 1** (top-left) | **Quadrant 2** (top-right) |
| **High Task Complexity** | **Quadrant 3** (bottom-left) | **Quadrant 4** (bottom-right) |

### Quadrant Contents

**Quadrant 1: Low Complexity + Low Accuracy Needs**
- Strategy: Zero-Shot CoT or Direct Prompting
- Cost: ~1x
- Color: Light green (low investment needed)
- Example: "Summarize this paragraph"

**Quadrant 2: Low Complexity + High Accuracy Needs**
- Strategy: CoT + Self-Consistency or CoVe
- Cost: 2-5x
- Color: Yellow (moderate investment)
- Example: "What is the boiling point of ethanol?"

**Quadrant 3: High Complexity + Low Accuracy Needs**
- Strategy: Plan-and-Solve, Skeleton-of-Thought, or Tree of Thoughts
- Cost: 1.5-10x
- Color: Orange (significant investment)
- Example: "Write a creative short story"

**Quadrant 4: High Complexity + High Accuracy Needs**
- Strategy: ReAct + CoVe, or ToT + Self-Consistency
- Cost: 5-20x
- Color: Red (maximum investment justified)
- Example: "Research and verify claims about drug interactions"

### Style
- Clean 2x2 grid with clear borders between quadrants
- Each quadrant contains: strategy name(s), approximate cost range, and a one-line example
- Axes labeled clearly:
  - X-axis (bottom): "Accuracy Requirements" with arrow from Low to High
  - Y-axis (left): "Task Complexity" with arrow from Low to High
- Gradient coloring from green (Q1) through yellow/orange to red (Q4)
- Title: "Figure 5. Strategy Selection by Task Complexity and Accuracy Requirements"
- Sans-serif font, professional academic style

### Output
- PNG at 300 DPI, approximately 7 inches wide by 6 inches tall
