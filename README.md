# Welcome to Charm

Charm is an open-source modular AI operating system that enables developers to compose, deploy, and scale AI applications across models, tools, frameworks, and platforms — all through a single unified API and plugin-based architecture.

## Core feature modules

**Execution Routing**:
Intelligently selects and adapts the optimal model and compute backend based on defined needs and policies, with built-in support for resource governance.

**Multi-Agent Management**:
Orchestrates multi-agent workflows with full lifecycle control, inter-agent handoff, and complete execution traceability.

**Semantic & Format adaptation**:
Standardizes diverse inputs into structured semantics & formats.

**Integration Bridge**:
Supporting multi-turn and long-horizon agent workflows through persistent, bidirectional communication with external platforms via APIs, webhooks, and event polling.

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
Unified Ingestion:
Accepts and normalizes inputs from diverse external sources (e.g., agent frameworks, iPaaS, protocol-based triggers) through pluggable adapters.

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
Pluggable Orchestration & Execution:
All tasks flow through a unified orchestration pipeline, where major subsystems expose plugin interfaces that allow you to inject or swap components (e.g., model routers, workflow planners, or SDK bridges) to compose workflows tailored to custom runtime requirements

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
