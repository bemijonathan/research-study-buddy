from utils import analyze_text


def reproduce_results(methodology):
    task = f"Based on the following methodology, describe how to reproduce the results:\n{
        methodology}"
    return analyze_text(methodology, task)
