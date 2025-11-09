## Agent Portability Pipeline

Conceptually, Charm’s portability pipeline looks like this:

SDK  
→ Source Agent Input  
→ **Parser** → UAC  
→ **Renderer** → Target Profile  
→ **Loader** → Runnable StateGraph  
→ **Attacher** → Runtime hooks / bridges


### 1st Reference Route: CrewAI → LangGraph

The pipeline is designed to support multiple source/target frameworks.

For v0.1.0, we are focusing on a single reference route:

**CrewAI → (Parser) → UAC → (Renderer) → LangGraph Profile  
→ (Loader) → runnable LangGraph StateGraph → (Attacher) → runtime hook**

This is the first end-to-end route we will implement.  
Additional routes (other sources and targets) will be added incrementally once this path is stable.
