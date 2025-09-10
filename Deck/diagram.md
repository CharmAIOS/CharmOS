```mermaid
flowchart LR
    subgraph FrameworkA["Source Framework"]
        A1[Role Card / Graph / Profile]
    end

    subgraph Charm["Charm Middleware"]
        C1[Unified Agent Contract]
        C2[Capability Mapping]
        C3[Secrets Broker & Injection]
        C4[Unified Envelope]
        C5[Event Bridge]
    end

    subgraph FrameworkB["Target Framework"]
        B1[Agent Execution]
    end

    subgraph ExternalApp["External Application"]
        E1[Webhook / API Call]
    end

    %% Flow
    A1 -->|Definition Conversion| C1
    C1 --> C2 --> C3
    C2 --> C4
    C4 --> C5
    C5 --> E1 -->|Event| C5 --> B1
    B1 -->|Result| C5 --> C4 --> A1

    %% Extra arrow
    FrameworkB <--> ExternalApp
