# Contributing to Agentic UI Auditor

As an AI Architecture framework, we focus on deterministic outputs from non-deterministic models.

## Architectural Guidelines
1. **State Management:** All agentic workflows must be managed through `LangGraph` state dictionaries. Do not use global variables.
2. **Prompts:** Vision prompts should be version-controlled and evaluated against our baseline dataset before merging.
3. **Browser Context:** Playwright instances must be isolated per session to ensure parallel execution capabilities.

## Pull Requests
- All new Auditor nodes must include unit tests mocking the Vision LLM response.
- Ensure the CI pipeline (`.github/workflows/audit.yml`) passes successfully.
