# Architecture Overview

### System Modules Overview

```
Developer / Framework / Plugin
│
├── Developer SDK & Interface
│   ├── Unified API SDK
│   ├── Module Entry Interface
│   ├── Extension Toolkit
│   └── Developer Docs
│
├── External Output Adapter
│
├── Smart Orchestrator Layer
│   ├── Unified API Access
│   ├── Routing Criteria Parser
│   │   ├── Request Analyzer
│   │   └── Policy Matcher
│   ├── Routing Engine
│   │   ├── Scoring Engine
│   │   ├── Preference Evaluator
│   │   └── Eligibility Filter
│   ├── Routing & Planning Orchestrator
│   │   ├── Workflow Planner
│   │   ├── Task Graph Builder
│   │   └── Execution Trigger & Sync
│   ├── AI Service Adapter
│   └── Task Lifecycle Orchestrator
│       ├── Task State Manager
│       ├── Task Context Manager
│       ├── Fallback / Retry Manager
│       └── IPC / Inter-App Control Layer
│
├── Inference Execution Layer
│   ├── Runtime Executor
│   ├── Inference Environment Adapter
│   ├── Inference Management
│   │   ├── Environment Binding
│   │   ├── Service Invocation Adapter
│   │   └── Model Execution Router
│   └── Execution Runtime
│       ├── Web Inference Engine
│       ├── Local Inference Engine
│       └── Cloud Inference Adapter
│
├── Resource Management Layer
│   └── Compute & Token Orchestration
│       ├── Physical Resource Verifier
│       ├── LLM Token Quota Controller
│       └── Inference Task Queue Manager
│
├── Format & Semantic Abstraction Layer
│   ├── AI Output Normalization Layer
│   │   ├── Output Format Identifier
│   │   ├── Structured Block Parser
│   │   ├── Semantic Data Extractor
│   │   └── Converter to Internal Structured Output Schema
│   ├── AI Output Format Adapter
│   ├── Structured Format Layer
│   ├── Format Conversion Layer
│   │   ├── Conversion Logic, Annotation Rules, Templates
│   │   ├── Multi-format Input Support
│   │   └── Developer Extensibility
│   ├── Semantic Abstraction Layer
│   │   ├── Standard Semantic Unit Definitions
│   │   ├── Semantic Mapping Specifications
│   │   └── Format Bridge
│   └── Market Format Conversion Layer
│
└── External IPC & API Adapter Layer
│       ├── Bi-directional API Adapter
│       ├── Runtime Hook
│       ├── Callback / Webhook
│       └── Multi-turn Execution Control
└── External Output
```
## External Output Adapter
Receives and bridges outputs from external AI tools, frameworks, or webhooks into Charm’s internal orchestration flow.
## Smart Orchestrator Layer
Handles task routing, planning, and lifecycle control within Charm. 
### Routing Criteria Parser

Interprets incoming requests and matches them against routing policies  
to generate structured criteria for downstream routing decisions.

#### Request Analyzer
- Extracts task intent, constraints, and metadata from the incoming request.
- Supports prompt parsing, tool usage hints, and context recognition.

#### Policy Matcher
- Compares request parameters against predefined policies and routing rules.
- Enables enforcement of business logic, access control, or usage constraints.
- Routing Engine
- Routing & Planning Orchestrator
- AI Service Adapter
- Task Lifecycle Orchestrator
## Inference Execution Layer
## Resource Management Layer
## Format & Semantic Abstraction Layer
## External IPC & API Adapter Layer
