import asyncio
from automation.browser import BrowserManager
from agents.graph import AuditorState

async def navigate_and_capture(state: AuditorState):
    browser = BrowserManager(headless=True)
    screenshot_path = f"data/artifacts/step_{state['current_step']}.png"
    
    # In a real scenario, the agent would decide WHERE to click next based on the goal
    print(f"Navigating to {state['url']} for step {state['current_step']}")
    await browser.capture_screenshot(state['url'], screenshot_path)
    
    return {
        "screenshots": [screenshot_path],
        "current_step": state["current_step"] + 1
    }
