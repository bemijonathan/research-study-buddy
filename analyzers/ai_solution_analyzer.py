from utils import analyze_text


def analyze_ai_solution(text):
    task = """Analyze the given text for an applied AI solution. 
    1. Identify the main AI techniques or algorithms used.
    2. Summarize the key components of the solution.
    3. Outline steps to implement this solution on AWS, including specific AWS services to use.
    4. Provide a high-level pseudocode or architecture diagram for the AWS implementation."""
    return analyze_text(text, task)
