from azurefunctions.extensions.mcp import McpApp, MCPToolContext
from typing import Annotated

app = McpApp()

@app.mcp_tool()
def greet(
    name: Annotated[str, "The name of the person to greet."],
    context: MCPToolContext
) -> str:
    """Greet a user by name."""
    return f"Hello, {name}! You called with context: {context}"

@app.mcp_tool()
def add_numbers(
    a: Annotated[int, "The first integer to add."],
    b: Annotated[int, "The second integer to add."]
) -> int:
    """Add two numbers."""
    return int(a + b)

@app.mcp_tool()
def get_weather(
    location: Annotated[str, "The location to get the weather for."]
) -> str:
    """Get the current weather for a location."""
    # Implement your weather fetching logic here
    return f"The current weather in {location} is 21°C."
