## 01 · Scope & Limitations: MVP Boundaries

### MVP Scope
This MVP begins by receiving outputs from agent frameworks like LangChain or Dify, and ends by converting and delivering structured results to external platforms.

Key boundaries:
- **Input Source**: Supports outputs from one to two agent frameworks (e.g., LangChain, Dify).
- **Execution Type**: Handles only single-turn tasks with no session memory or multi-step context.
- **Output Target**: Supports conversion and delivery to one to two mainstream SaaS platforms (via webhook).
- **Semantic Types**: Limited to a predefined set of semantic block types (e.g., summary, task_list, outline).

### Post-MVP Expansion Plan (TBD)
- Enable multi-turn agent workflows with persistent context
- Add plugin-based API task handling
- Support dynamic routing rules and preference layers
- Extend delivery to other tools or platform
- Enable agent-to-agent chaining with intermediate output coordination
