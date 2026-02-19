from google.adk import Agent

from sub_agents.research_agent import research_agent
from sub_agents.analysis_agent import analysis_agent
from sub_agents.writer_agent import writer_agent
from sub_agents.formatter_agent import formatter_agent


root_agent = Agent(

    name="RootOrchestrator",

    model="gemini-2.0-flash",

    description="Main agent that orchestrates all sub agents.",

    sub_agents=[
        research_agent,
        analysis_agent,
        writer_agent,
        formatter_agent
    ],

    instruction="""
    You are the root orchestrator agent.

    Your job is to:

    1. Send topic to ResearchAgent
    2. Send research output to AnalysisAgent
    3. Send analysis to WriterAgent
    4. Send final content to FormatterAgent
    5. Ensure final report is generated
    """
)