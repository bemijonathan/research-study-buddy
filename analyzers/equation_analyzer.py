from utils.openai_helper import analyze_text


def extract_equations(text):
    task = "Extract and list all mathematical equations from the given text."
    return analyze_text(text, task)


def validate_equations(equations):
    task = f"Validate the following equations and explain their meaning:\n{
        equations}"
    return analyze_text(equations, task)
