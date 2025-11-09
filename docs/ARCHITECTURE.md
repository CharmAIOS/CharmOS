## Charm Middleware Architecture

### Flow Visualization
```mermaid
flowchart LR
    subgraph FrameworkA["Source Framework"]
        A1[Role Card / Graph / Profile]
    end

    subgraph Charm["Charm Middleware"]
        C1[Adapter]
        C2[Event Bridge]
        C4[Transport]
        C5[Edge Hook]
    end

    subgraph FrameworkB["Target Framework"]
        B1[Agent Execution]
    end

    %% Flow
    A1 --> C1
    C1 --> C2
    C2 --> C4
    C4 --> C5
    C5 --> B1
    B1 --> C5 --> C4 --> A1
```
### Core Modules
#### Agent Adapter
- Definition standardization: Parses agent definitions and transforms them into the Unified Agent Contract (Charm UAC)
- Capability Mapping: Aligns the agent’s declared capabilities with the target system’s available tools or plugins, registers them into the runtime, and supports graceful degradation

#### Stateful Bridge
- Outbound: Streams agent outputs to external system
- Inbound: Subscribes to responses/triggers and reattaches them to the correct task state
- Lifecycle-Aware: Supports pause/wait/resume, retry/backoff, and reactivation

#### Transport 
- Handles low-latency, bidirectional communication with external agent systems
- Support task resumption routing, correlation-aware message delivery

#### Edge Governance
- Enforces quotas, rate limits, and concurrency control
- Handles stateless retry/backoff and automated recovery
