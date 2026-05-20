# Gemini Visual Generation Prompt — Figure 3: CoT vs. ToT vs. GoT Structural Comparison

## Instructions for Gemini

Create a three-panel diagram showing the structural evolution of reasoning from linear chains to trees to graphs.

### Panel Layout
Three panels side by side, labeled (a), (b), (c).

### Panel (a): Chain-of-Thought — Linear Chain
- A simple linear sequence of 5 nodes connected by arrows: S --> A --> B --> C --> Answer
- All nodes are the same color (blue)
- Label: "(a) Chain-of-Thought: Linear Sequence"
- Emphasize simplicity — one path, no branching

### Panel (b): Tree of Thoughts — Branching Tree
- Starting node S branches into three children: A1, A2, A3
- A1 branches into B1, B2 (B2 is grayed out / crossed, indicating pruning)
- A2 branches into B3, B4 (both grayed out — pruned)
- A3 branches into B5 (continues to C1 --> Answer)
- Active/selected path highlighted in green
- Pruned branches in light gray with small "x" marks
- Label: "(b) Tree of Thoughts: Branching with Pruning"

### Panel (c): Graph of Thoughts — DAG with Merging
- Starting node S branches into A1, A2, A3 (like the tree)
- A1 leads to B1, A2 leads to B2, A3 leads to B3
- B1 and B2 MERGE into a single node C1 (shown with two arrows converging)
- B3 leads to C2
- C1 and C2 merge into final Answer node
- Merge points highlighted with a distinct color (orange)
- Label: "(c) Graph of Thoughts: Branching + Merging (DAG)"

### Style
- Clean academic style on white background
- Nodes as circles with labels inside
- Active paths in bold dark blue or green
- Pruned paths in light gray, dashed lines
- Merge points in orange with slightly larger nodes
- Title: "Figure 3. Structural Evolution from Linear Chains to Trees to Graphs of Reasoning"
- Sans-serif font, 300 DPI

### Output
- PNG at 300 DPI, approximately 9 inches wide by 4 inches tall
