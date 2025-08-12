# Welcome to Charm

Charm is an open-source modular AI operating system that enables developers to compose, deploy, and scale AI applications across models, tools, frameworks, and SaaS platforms — all through a single unified API and plugin-based architecture.

## Core feature modules

**Execution & Model Routing**:
Intelligently selects and adapts the optimal model and compute backend based on routing policies, with built-in support for fallback strategies, token quota enforcement, and dynamic resource allocation.

**Orchestrator & Lifecycle Manager**:
Orchestrates multi-agent workflows with complete task lifecycle control—including planning, execution, error recovery, and inter-agent handoff—with full traceability and execution observability.

**Semantic Middleware & Format Adapter**:
Standardizes and transforms diverse inputs into structured semantic formats, enabling seamless routing, validation, and cross-platform compatibility.

**Integration & Event Bridge**:
Facilitates bidirectional communication with external platforms via APIs, webhooks, or event polling—supporting asynchronous triggers, state-based reactivation, and real-time task continuation.


## Architecture

```mermaid
graph LR
        A1[Natural Language] --> UI[Unified Interface]
        A2[Structured Flow] --> UI
        A3[External Trigger] --> UI
        A4[UI or CLI Event] --> UI

    UI --> SM

    subgraph Charm Core
        SM[Semantic Middleware &<br/>Format Adapter] --> ORCH[Task Lifecycle<br/>Orchestration & Planning]
        ORCH --> EXE[Execution &<br/>Model Routing]
        EXE --> IEB[Integration &<br/>Event Bridge]
end
```
Modular & Plugin-Based Design

1. Unified Ingestion:
Accepts and normalizes inputs from diverse external sources—agent frameworks (e.g., LangChain, AG2), automation platforms (e.g., Zapier, Notion), and protocol-based triggers (e.g., MCP)—through pluggable adapters.

```mermaid
flowchart LR
    UI[Unified Interface]

    PL1[Flow Compiler]
    PL2[SaaS SDK Wrapper / API Adapter]
    PL3[UI / CLI Bridge]
    PL4[Prompt Interpreter]

    PL1 --> UI
    PL2 --> UI
    PL3 --> UI
    PL4 --> UI
```
2. Pluggable Execution Layers:
All major subsystems—model selection, orchestration engine, semantic formatting, and event handling—expose plugin interfaces. Developers can inject or swap components (e.g., LLM backends, flow planners, SDK bridges, monitoring hooks) to meet custom runtime requirements without altering core system logic.

```mermaid
flowchart LR
    subgraph SYSTEM_INTERNAL [Modular Runtime]
        SM[Semantic Middleware & Format Adapter]
        ORCH[Task Lifecycle Orchestration & Planning]
        EXE[Execution & Model Routing]
        IEB[Integration & Event Bridge]
    end

    SM --> ORCH --> EXE --> IEB

    %% Plugin injection points
    PL_SM[Semantic Parsers, Format Adapters] --> SM
    PL_ORCH[Routing Policies, Task Planner] --> ORCH
    PL_EXE[Model Selector, Compute Strategy] --> EXE
    PL_IEB[SaaS Connector, Output Renderers] --> IEB
```

3. Cross-Platform Integration:
A decoupled, modular design enables deep interoperability with external tools and systems, allowing developers to orchestrate workflows that span internal and third-party services. This supports shared execution, bidirectional state synchronization, and seamless task handoffs.

```mermaid
flowchart LR
    subgraph External Systems
        Z1[Notion Trigger]
        Z2[Zapier Event]
    end

    subgraph Charm Core
        A1[Task Orchestrator]
        A2[Planning Engine]
        A3[Execution Engine]
        A4[Event Dispatcher]
    end

    subgraph Third-Party Services
        B1[LangChain Agent]
        B2[OpenRouter Model]
        B3[Slack API Call]
    end

    Z1 --> A1
    Z2 --> A1
    A1 --> A2
    A2 --> B1
    B1 --> A3
    A3 <--> B2
    A3 --> A4
    A4 --> B3
```
[Architecture Breakdown](https://github.com/CharmAIOS/CharmOS/blob/main/docs/architecture.md)
