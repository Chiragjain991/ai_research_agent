from google.adk import Agent
from google.adk.tools import google_search
from tools.search_tools import clean_search_results

research_agent = Agent(
    name="ResearchAgent",

    model="gemini-2.0-flash",

    description="Performs research using google_search tool.",

    tools=[
        google_search,
        clean_search_results
    ],

    instruction="""
    You are a research agent.

    Your job is to:
    1. Use google_search to find information about the topic.
    2. Use clean_search_results tool to format the output.
    3. Provide structured research content.
    """
)