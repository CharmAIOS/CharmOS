## 03 · Semantic Abstraction: Normalize Model Output

### This module demonstrates
Transforms raw model output into structured semantic blocks, enabling downstream interoperability and multi-format conversion.

### Implementation reference
- Take a hardcoded mock model output, such as a summary or task list.
- Pass it through a simulated normalization function.
- Output the resulting `semantic_blocks` (in JSON or readable pseudo-structure) to the console or markdown.
- `semantic_block` should include metadata like `type`, `content`, `confidence`, and `source`.

### MVP Relevance
Establishes the foundation for scalable semantic processing in the MVP:
- Define the internal schema structure (`semantic_blocks`)
- Implement a basic normalization interface (`normalizeToSemanticBlocks()`)
- Support selected semantic block types (e.g., summary, action_item, slide_outline) 這樣？
