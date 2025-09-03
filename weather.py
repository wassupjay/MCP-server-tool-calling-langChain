from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """This if for the weather for location."""
    return "It's always sunny in California"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")