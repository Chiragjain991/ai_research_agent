def generate_markdown_report(topic: str, content: str) -> str:
    """
    Generate and save research report as markdown file.
    """

    if not topic:
        topic = "research_report"

    filename = topic.replace(" ", "_") + ".md"

    report = f"""
# Research Report: {topic}

## Overview

{content}

## Conclusion

This report was generated using a Multi-Agent System built with Google ADK.
"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)

    return f"Report saved successfully as {filename}"