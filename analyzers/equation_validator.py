from utils import analyze_text


def validate_equations(equations):
    task = f"Validate the following equations and explain their meaning:\n{
        equations}"
    return analyze_text(equations, task)
