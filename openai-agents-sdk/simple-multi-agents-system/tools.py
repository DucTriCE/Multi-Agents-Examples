import asyncio
import random
import os
from agents import Agent, AgentHooks, RunContextWrapper, Runner, Tool, function_tool

@function_tool
def calculate_years_of_age(birth_year: int) -> int:
    """Calculate the number of years since birth."""
    return 2025 - birth_year

@function_tool
def add_two_numbers(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y

@function_tool
def multiply_by_two(x: int) -> int:
    """Simple multiplication by two."""
    return x * 2

@function_tool
def random_sport() -> str:
    """Generate a random sport."""
    sports = ["soccer", "basketball", "tennis"]
    return random.choice(sports)

