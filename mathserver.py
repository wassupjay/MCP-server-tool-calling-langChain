from mcp.server.fastmcp import FastMCP

mcp=FastMCP("math")

@mcp.tool()
def add(a:int, b:int)->int:
    """_summary_
    Add two numbers"""
    return a+b

@mcp.tool()
def multiply(a:int, b:int)->int:
    """Mulitply two numbers"""
    return a*b

#transport="stdio") tell server to standard ip op to recive and print at the command prompt itself
if __name__ == "__main__":
    mcp.run(transport="stdio") 