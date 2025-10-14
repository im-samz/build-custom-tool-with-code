import json
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# DEFINE PROPERTIES TO BE USED BY TOOLS
# Tool property class
class ToolProperty:
    def __init__(self, property_name: str, property_type: str, description: str):
        self.propertyName = property_name
        self.propertyType = property_type
        self.description = description

    def to_dict(self):
        return {
            "propertyName": self.propertyName,
            "propertyType": self.propertyType,
            "description": self.description,
        }
# Create tool properties for greet
# Parameters
_NAME = "name"

# Define the tool properties using the ToolProperty class
tool_properties_greet_object = [
    ToolProperty(_NAME, "string", "The name of the person to greet."),
]

# Convert the tool properties to JSON
tool_properties_greet_json = json.dumps([prop.to_dict() for prop in tool_properties_greet_object])

# Create tool properties for add_numbers
# Parameters
_INTEGER_A = "A"
_INTEGER_B = "B"

# Define the tool properties using the ToolProperty class
tool_properties_add_numbers_object = [
    ToolProperty(_INTEGER_A, "integer", "The first integer to add."),
    ToolProperty(_INTEGER_B, "integer", "The second integer to add."),
]

# Convert the tool properties to JSON
tool_properties_add_numbers_json = json.dumps([prop.to_dict() for prop in tool_properties_add_numbers_object])

# Create tool properties for get_weather
# Parameters
_LOCATION = "location"

# Define the tool properties using the ToolProperty class
tool_properties_get_weather_object = [
    ToolProperty(_LOCATION, "string", "The location to get the weather for."),
]

# Convert the tool properties to JSON
tool_properties_get_weather_json = json.dumps([prop.to_dict() for prop in tool_properties_get_weather_object])

# MCP tool to greet a user
@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName="greet",
    description="Greet a user by name.",
    toolProperties=tool_properties_greet_json,
)
def greet(context) -> str:
    """Greet a user by name."""
    content = json.loads(context)
    name = content["arguments"][_NAME]
    return f"Hello, {name}!"

# MCP tool to add two numbers
@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName="add_numbers",
    description="Add two numbers.",
    toolProperties=tool_properties_add_numbers_json,
)
def add_numbers(context) -> int:
    """Add two numbers."""
    content = json.loads(context)
    a = int(content["arguments"][_INTEGER_A])
    b = int(content["arguments"][_INTEGER_B])
    return a + b

# MCP tool to get the current weather for a location
@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName="get_weather",
    description="Get the current weather for a location.",
    toolProperties=tool_properties_get_weather_json
)
def get_weather(context) -> str:
    """Get the current weather for a location."""
    content = json.loads(context)
    location = content["arguments"]["location"]
    # Implement your weather fetching logic here
    return f"The current weather in {location} is 21°C."
