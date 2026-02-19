from google.adk import Agent

writer_agent = Agent(
    name="WriterAgent",

    model="gemini-2.0-flash",

    description="Converts analysis into structured technical content.",

    instruction="""
    You are a technical writer agent.

    Your job is to:
    1. Convert analyzed insights into professional report content.
    2. Use structured formatting.
    3. Make content clear and readable.
    """
)