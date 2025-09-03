
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"], 
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp", 
                "transport": "streamable_http",
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    print(f"Available tools: {[tool.name for tool in tools]}")
    
    model = ChatGroq(model="llama-3.1-8b-instant")
    agent = create_react_agent(model, tools)

    # Math test (this already works)
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 10?"}]}
    )
    print("Math response:", math_response['messages'][-1].content)

    # Weather test - BE VERY EXPLICIT about tool usage
    weather_response = await agent.ainvoke(
        {"messages": [
            {"role": "system", "content": "You are a helpful assistant. You have exactly these tools available: add, multiply, and get_weather. You must ONLY use these tools. You cannot use any web search tools. When asked about weather, you MUST use the get_weather tool."},
            {"role": "user", "content": "Please use the get_weather tool to find out what the weather is in California. Do not search the web - only use the get_weather tool that is available to you."}
        ]}
    )
    print("Weather response:", weather_response['messages'][-1].content)

if __name__ == "__main__":
    asyncio.run(main())

