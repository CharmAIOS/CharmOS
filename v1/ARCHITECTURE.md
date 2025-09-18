### Semantic Adapter
#### Agent Adapter
- Definition standardization: Parses agent definitions and transforms them into the Unified Agent Contract (UAC)
- Capability Mapping: Aligns declared agent capabilities with the target system’s available tools or plugins, mapping them into Charm’s standardized scopes, while supporting graceful degradation

#### App Adapter
- Semantic Conversion: Translates app-specific behaviors and events into the Connector Contract (CC)
- API Mapping: Maps these unified actions and events to each app’s concrete API schemas

### Transport Plugin
#### Agent Transport
#### App Transport
### Unified Envelope
- All cross-framework messages include correlation metadata
- Events transmitted across all frameworks/applications share the same task envelope

### Stateful Event Bridge
- Outbound: Streams agent outputs to external apps/frameworks, while preserving task identity
- Inbound: Subscribes to external responses or triggers and attaches them to the correct task state
- Lifecycle-Aware: supports pause / wait / resume, retry / backoff, and state reactivation

### Edge Governance
- Apply multi-tier governance mechanisms at the ingress/egress layer
- Provide error detection and automated recovery strategies
- Provides a secure API wrapper for outbound agent calls

### Secrets & Credential Vault
- Map metadata to stored credentials during the call process to enable secure credential injection
- Ensures tenant isolation, encryption-at-rest and in-transit, scoped access, and full audit trails

