import asyncio
import random
from typing import Any
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from agents import Agent, AgentHooks, RunContextWrapper, Runner, Tool, function_tool
from tools import add_two_numbers, multiply_by_two, random_sport, calculate_years_of_age
from utils import CustomAgentHooks, FinalResult


math_agent = Agent(
    name="Math Agent",
    instructions="You are a math agent. If receive a number, you will multiply it by 2. If two number are given, you will add them.",
    tools=[multiply_by_two, add_two_numbers],
    output_type=FinalResult,
    hooks=CustomAgentHooks(display_name="Math Agent"),
)

physics_agent = Agent(
    name="Physics Agent",
    instructions="You are a physics agent. You will be ask about a theory and you will explain it briefly.",
    output_type=FinalResult,
    hooks=CustomAgentHooks(display_name="Physics Agent"),
)

pe_agent = Agent(
    name="Physical Education Agent",
    instructions="You are a physical education agent. You will give one of a random sport to play.",
    tools=[random_sport],
    output_type=FinalResult,
    hooks=CustomAgentHooks(display_name="Physical Education Agent"),
)

main_agent = Agent(
    name="Main agent",
    instructions="Base on the given task, you determine which agent to use on that task. If the task is about calculating years of age base on birth year, use your own tool",
    tools=[calculate_years_of_age],
    output_type=FinalResult,
    handoffs=[math_agent, physics_agent, pe_agent],
    hooks=CustomAgentHooks(display_name="Main Agent"),
)


async def main() -> None:
    await Runner.run(
        main_agent,
        input=f"{input('Input: ')}",
    )
    print("Done!")


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
