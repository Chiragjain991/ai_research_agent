def extract_key_points(text: str) -> str:
    """
    Extract key insights from research text.
    """

    if not text:
        return "No content available."

    summary = text[:1500]

    return f"""
Key Insights:

{summary}
"""