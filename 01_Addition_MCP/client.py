# client.py
import os
import sys
import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPClient, MCPAgent

async def main():
    load_dotenv()  # loads GROQ_API_KEY
    client = MCPClient.from_config_file("mcp.json")

    llm = ChatGroq(model="deepseek-r1-distill-llama-70b", temperature=0.0)
    agent = MCPAgent(llm=llm, client=client, max_steps=5, memory_enabled=False, verbose=True)

    print("Asking the agent to compute 7 + 13 via the add tool...")
    result = await agent.run("Please calculate 7 plus 13 using the add tool.")

    # The result usually includes tool calls; print text or full result
    try:
        print("Agent response:", result.text or result)
    except:
        print("Agent response:", result)

if __name__ == "__main__":
    asyncio.run(main())
