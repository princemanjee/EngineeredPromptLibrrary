# Gemini Visual Generation Prompt — Figure 1: Cost-Accuracy Tradeoff Curve

## Instructions for Gemini

Create a clean, professional scatter plot / bubble chart for an academic paper with the following specifications:

### Chart Type
Scatter plot with labeled data points (or small bubbles sized by typical usage frequency).

### Axes
- **X-axis**: "Inference Cost (token multiplier vs. direct answer)" — logarithmic scale from 1x to 20x
- **Y-axis**: "Accuracy Improvement Over Baseline (%)" — linear scale from 0% to 40%

### Data Points to Plot

| Strategy | Cost Multiplier | Accuracy Gain | Family Color |
|---|---|---|---|
| Zero-Shot CoT | 1.1x | 10-15% | Blue |
| Chain-of-Thought (few-shot) | 1.3x | 15-25% | Blue |
| Plan-and-Solve | 1.4x | 15-20% | Blue |
| Program-of-Thought | 1.5x | 25-35% | Blue |
| Self-Refine | 2.5x | 10-20% | Green |
| Chain-of-Verification | 3x | 15-25% | Green |
| Self-Consistency (N=5) | 5x | 10-20% | Orange |
| Tree of Thoughts | 8x | 20-35% | Orange |
| ReAct | 10x | 20-30% | Purple |
| Graph of Thoughts | 10x | 15-25% | Orange |

### Color Legend
- Blue: Single-path strategies
- Green: Self-refinement strategies
- Orange: Multi-path / tree / graph strategies
- Purple: Tool-use strategies

### Style
- Clean white background, minimal gridlines
- Professional academic style suitable for a published paper
- Sans-serif font (Helvetica or similar)
- Each data point labeled with strategy name
- Dashed diagonal line from bottom-left to top-right labeled "efficiency frontier"
- Title: "Figure 1. Cost-Accuracy Tradeoff Across Reasoning Strategy Families"
- Note at bottom: "Accuracy gains are approximate ranges from published benchmarks; actual values vary by model and task."

### Output
- PNG at 300 DPI, approximately 8 inches wide by 5 inches tall
- Transparent or white background
