import argparse
import asyncio
from agents.graph import auditor_agent
from core.reporting import ReportGenerator

async def run_audit(url: str, goal: str):
    print(f"🚀 Starting Agentic UX Audit for: {url}")
    initial_state = {
        "url": url,
        "goal": goal,
        "current_step": 0,
        "screenshots": [],
        "issues_found": [],
        "is_complete": False
    }
    
    final_state = await auditor_agent.ainvoke(initial_state)
    
    print("✅ Audit Complete. Generating Enterprise Report...")
    ReportGenerator.generate_json_report(final_state)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Agentic UI Auditor CLI")
    parser.add_argument("--url", type=str, required=True, help="Target URL to audit")
    parser.add_argument("--goal", type=str, default="General UX Audit", help="Audit objective")
    args = parser.parse_args()
    
    asyncio.run(run_audit(args.url, args.goal))
