## 02 · System Diagram: MVP Data Flow

```mermaid
flowchart TD

subgraph Unified Input
    A[Unified API SDK<br>← Agent Output]
end

subgraph Processing
    B1[Output Normalization<br>→ to semantic_blocks]
    B2[Semantic Abstraction<br>→ metadata tagging]
    B3[Routing Engine<br>→ choose post-processing path]
    B4[Task State Manager<br>→ track task status]
    B5[Fallback / Retry<br>→ handle delivery failures]
end

subgraph Output
    C1A[Notion Formatter<br>→ JSON for platform 01]
    C1B[Slack Formatter<br>→ JSON for platform 02]
    C2[Bi-directional API Adapter<br>→ webhook delivery]
end

A --> B1
B1 --> B2
B2 --> B3
B3 --> C1A
B3 --> C1B
C1A --> C2
C1B --> C2

%% Task tracking side flow
B1 --> B4
B2 --> B4
C2 --> B4
C2 --> B5
B5 --> C2
B5 --> B4
