## 01 · Unified Interface: CLI & API Task Entry

### This module demonstrates
All CharmOS tasks begin from a unified interface that accepts standardized inputs including prompts and execution preferences.

### Implementation reference
- Accept task configurations via:
  - A CLI command
  - A simulated API endpoint
- Unified task config includes fields like `prompt`, `preferred_model`, `format`, and `latency_mode`.
- Capture and structure the received task configuration payload for further processing.
- No routing or execution is triggered; this module only confirms and echoes the input.

> Note: In this demo, downstream modules are not invoked. Each module simulates its own input for demonstration purposes.
