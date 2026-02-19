from google.adk import Agent
from tools.report_tools import generate_markdown_report

formatter_agent = Agent(
    name="FormatterAgent",

    model="gemini-2.0-flash",

    description="Formats and saves the report as markdown file.",

    tools=[
        generate_markdown_report
    ],

    instruction="""
    You are a formatter agent.

    Your job is to:
    1. Format the final content properly.
    2. Use generate_markdown_report tool to save the report.
    """
)