# Agentic Loop Architecture

## State Management
We use a **Persistent State Graph** to manage the auditor's journey. Unlike linear scripts, the agent can loop back to a previous state if the Vision LLM determines a "dead-end" or if a UI modal blocks progress.

## Node Definitions
1.  **Navigate:** Uses Playwright to interact with DOM elements.
2.  **Analyze:** Calls GPT-4o with encoded screenshots and heuristic prompts.
3.  **Remediate:** (Experimental) Proposes CSS/HTML fixes based on findings.

## Convergence Criteria
The agent stops when:
- The `goal` has been fulfilled with >90% confidence.
- Maximum `current_step` threshold is reached.
- An unrecoverable visual error is detected.
