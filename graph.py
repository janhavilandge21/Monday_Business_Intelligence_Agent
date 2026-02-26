from agent.insights import generate_insight

def run_agent(question):
    if "board" in question.lower():
        return generate_insight()
    
    return "I can currently answer board-related business questions."