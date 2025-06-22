## 03 · Module Breakdown: Components & Roles

This document outlines the key modules defined in the [architecture overview](https://github.com/CharmAIOS/CharmOS/blob/main/docs/architecture.md), how they behave in the [Demo](https://github.com/CharmAIOS/CharmOS/tree/main/demo), and what is required for the MVP execution scope.

---

### Module List

### 1. Unified API SDK

- **Role**: The entry point for receiving external payloads.
- **Demo**: Simulated CLI/API payload.
- **MVP**: Expose a real HTTP endpoint or function handler to accept structured results from target frameworks (e.g., LangChain, Dify).

### 2. Output Normalization Module

- **Role**: Converts output into internal semantic_blocks.
- **Demo**: Hardcoded output → mock normalization function.
- **MVP**: Implement a real `normalizeToSemanticBlocks()` function for selected output types (e.g., summary, task list).

### 3. Semantic Abstraction Unit

- **Role**: Applies metadata (e.g., confidence, type, source) and maps input into system-compatible semantic units.
- **Demo**: Static metadata injection.
- **MVP**: Define core schema and inject real metadata fields during normalization.

### 4. Market Format Adapter

- **Role**: Converts internal `semantic_blocks` to formats required by external tools.
- **Demo**: Console or markdown output simulation.
- **MVP**: Convert semantic blocks into platform-specific JSON.

### 5. Bi-directional API Adapter

- **Role**: Sends structured data to external platforms via webhook or API call.
- **Demo**: Simulated outgoing payload log.
- **MVP**: Implement actual webhook integration with at least one target platform.

### 6. Routing Engine

- **Role**: Selects appropriate formatting pipeline based on semantic type.
- **Demo**: Hardcoded routing rule.
- **MVP**: Rule-based dispatcher that routes semantic blocks to the correct formatting modules.

### 7. Task State Manager

- **Role**: Tracks the state of each task through the processing lifecycle.
- **Demo**: Not included.
- **MVP**: Assign and persist states (e.g., `received`, `normalized`, `delivered`, `failed`) to support system observability and debugging.

### 8. Fallback / Retry Manager

- **Role**: Handles processing failures (e.g., delivery error) by retrying or switching to alternate strategies.
- **Demo**: Not included.
- **MVP**: Implement simple retry logic and log all fallback attempts.
