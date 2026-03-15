# 🤖 Agentic UI Auditor Framework

[![Python](https://img.shields.io/badge/Language-Python%203.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Tools-Playwright-2EAD33?style=for-the-badge&logo=playwright)](https://playwright.dev/)
[![LangChain](https://img.shields.io/badge/Framework-LangGraph-1C3C3C?style=for-the-badge)](https://www.langchain.com/langgraph)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

## 🌟 Overview
**Agentic UI Auditor Framework** is an autonomous solution for auditing web interfaces using Multi-modal LLMs. It combines browser automation with vision-language models to detect UX friction, accessibility violations, and design inconsistencies without manual test scripts.

## 🏗️ Architecture & AI Solutions
- **Autonomous Exploration:** Uses `LangGraph` to create stateful agents that navigate websites based on high-level goals (e.g., "Analyze the checkout flow").
- **Visual Intelligence:** Integrates `GPT-4V` or `Claude 3 Vision` to "see" and evaluate UI components like a human UX auditor.
- **Automation Engine:** Powered by `Playwright` for robust, cross-browser interaction.
- **Auditing Logic:** Implements heuristic-based and AI-driven rule sets for heuristic evaluation.

## 🛠️ Technical Stack
- **Core:** Python 3.10+
- **AI Orchestration:** LangGraph, LangChain.
- **Automation:** Playwright (Chromium, Firefox, WebKit).
- **Vision Models:** GPT-4o, Claude 3.5 Sonnet.

## 📂 Repository Structure
```text
├── agents/             # LangGraph agent definitions and state machine
├── automation/         # Playwright wrappers and browser control
├── auditors/           # UX heuristic and accessibility rule sets
├── data/               # Audit reports and visual artifacts (screenshots)
├── core/               # Configuration and model orchestration
├── tests/              # Unit tests for auditor logic
└── README.md
```

## 🚀 Quick Start
```bash
# Install dependencies
pip install -r requirements.txt
playwright install

# Run a sample audit
python main.py --url https://example.com --goal "Evaluate homepage UX"
```

---
**Crafted by [Ka Yeung Ling](https://github.com/KaYeungLing)**  
*AI Solution Architect & UX Engineer*
