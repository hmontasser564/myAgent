from __future__ import annotations
from google.adk.agents import Agent

root_agent = Agent(
    name="my_assistant",
    model="gemini-3.6-flash",
    description="A helpful AI assistant connected to Google AI Studio.",
    instruction=(
        "You are a helpful AI assistant. Answer the user's questions clearly."
    )
)