from google.adk import Agent
from tools.text_tools import extract_key_points

analysis_agent = Agent(
    name="AnalysisAgent",

    model="gemini-2.0-flash",

    description="Analyzes research content and extracts key insights.",

    tools=[
        extract_key_points
    ],

    instruction="""
    You are an analysis agent.

    Your job is to:
    1. Analyze the research content.
    2. Use extract_key_points tool to extract important insights.
    3. Provide clear summarized output.
    """
)
