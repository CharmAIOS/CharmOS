### Objective
Showcase how the CharmOS runtime completes a full task workflow from prompt to application-ready output, and demonstrates how to integrate outputs from existing frameworks such as LangChain or Dify into downstream processes.

### Demoflow

```mermaid

graph TD
  A[User Prompt / Task Config] --> B[Unified API Interface]
  B --> C[Routing Engine]
  C --> D[Model Inference]
  D --> E[Output Normalizer]
  E --> F1[Semantic Blocks A<br>(Native Flow)]

  %% External framework output
  L[LangChain Output] --> M[Framework Adapter]
  M --> F2[Semantic Blocks B<br>(From External Framework)]

  %% Interop (Handoff)
  F1 --> H[Semantic Handoff<br>Inject A ➝ Agent B]
  H --> F2

  %% Output
  F2 --> G[Market Format Adapter]
  G --> I[Multi-format Output<br>(Notion / Markdown / JSON)]
  I --> J[Dispatch to App<br>Webhook / API]

```

| Module | Filename                     | Purpose                                                                 |
|--------|------------------------------|-------------------------------------------------------------------------|
| 01     | `01_unified_interface.md`    | Accept user input via CLI or unified API to initiate full task flow.   |
| 02     | `02_routing_and_model_selection.md` | Demonstrate model selection logic and produce a simulated model output. |
| 03     | `03_semantic_abstraction.md` | Transform raw model output into structured semantic blocks (internal format). |
| 04     | `04_interoperability.md`     | Showcase semantic compatibility and handoff across native/external agents. |
| 05     | `05_output_adapter.md`       | Convert structured blocks into output formats. |
| 06     | `06_execution_trace.md`      | Trace full execution path step-by-step across modular functions.        |

### Modules Covered

- **Developer SDK & Interface** (mocked)
- **External Output Adapter** (mocked)
- **Unified API Access**(hardcoded)
- **Routing Criteria Parser** (hardcoded)
- **Routing Engine** (hardcoded)
- **Inference Execution Layer** (hardcoded)
  - Runtime Executor
  - Inference Management
  - Inference Environment Adapter
- **Format & Semantic Abstraction Layer** (mocked)
  - Output Normalization Module
  - Semantic Abstraction Unit
  - Market Format Adapter
- **External IPC & API Adapter Layer** (mocked)
  -  Bi-directional API Adapter
  -  Multi-turn Execution Control

### Core Values Showcased

**Plug-and-Play Compatibility**
- Integrate upstream AI workflow or output
- Normalize inputs into an internal semantic schema
- Maintain a unified pipeline across all task sources
**Semantic Interoperability**
- Unify diverse outputs into a shared internal semantic schema
- Enable collaboration and task handoff across the system
**Output Versatility**
- Convert structured results into multiple output formats
- Deliver output to external applications via API or webhook
- Convert once and enable reuse across diverse applications
**Modular System Architecture**
- Decompose the entire workflow into independent and composable modules
- Accountability and transparency during task execution
