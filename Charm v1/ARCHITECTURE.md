## Charm Middleware
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

    subgraph ExternalApp["External Application"]
        E1[Webhook / API Call]
    end

    %% Flow
    A1 -->|Parse| C1
    C1 --> C2
    C2 --> C4
    C4 --> C5
    C5 --> E1 -->|Event| C5 --> B1
    B1 -->|Result| C5 --> C4 --> A1

    %% Extra arrow
    FrameworkB <--> ExternalApp
```
### Semantic Adapter
Agent Adapter
- Definition standardization: Parses agent definitions and transforms them into the Unified Agent Contract (Charm UAC)
- Capability Mapping: Aligns declared agent capabilities with the target system’s available tools or plugins, mapping them into Charm’s standardized scopes, while supporting graceful degradation

App Adapter
- Semantic Conversion: Translates app-specific behaviors and events into the Connector Contract (CC)
- API Mapping: Maps these unified actions and events to each app’s concrete API schemas

### Stateful Event Bridge
- Outbound: Streams agent outputs to external system
- Inbound: Subscribes to responses/triggers and reattaches them to the correct task state
- Lifecycle-Aware: Supports pause/wait/resume, retry/backoff, and reactivation

### Transport 
Agent Transport
- Handles low-latency, bidirectional communication with external agent systems
- Support task resumption routing, correlation-aware message delivery, and HTTP/WebSocket connection lifecycle management

App Transport (TBD)

### Edge Governance
- Enforces quotas, rate limits, and concurrency control
- Handles stateless retry/backoff and automated recovery
- Provides a secure outbound API wrapper for agent calls

### Secrets & Credential Vault
- Injects credentials during execution based on metadata mapping
- Ensures tenant isolation, scoped access, encryption at rest/in transit, and full audit trails
