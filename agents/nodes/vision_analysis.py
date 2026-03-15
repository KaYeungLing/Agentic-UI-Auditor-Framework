from agents.graph import AuditorState

def analyze_ui_heuristics(state: AuditorState):
    latest_screenshot = state["screenshots"][-1]
    print(f"Analyzing {latest_screenshot} using Vision LLM...")
    
    # Mocking Vision LLM call (e.g., GPT-4o or Claude 3.5 Sonnet)
    # prompt = "Analyze this UI for accessibility violations and UX friction."
    # response = vision_llm.invoke(prompt, image=latest_screenshot)
    
    mock_issue = {
        "severity": "high",
        "type": "contrast_ratio",
        "description": "The primary call-to-action button lacks sufficient contrast against the background.",
        "element_context": "Header navigation bar"
    }
    
    # Decide if the goal is met
    is_complete = state["current_step"] >= 2
    
    return {
        "issues_found": [mock_issue],
        "is_complete": is_complete
    }
