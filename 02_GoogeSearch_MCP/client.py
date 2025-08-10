import os, asyncio
from dotenv import load_dotenv
from mcp_use import MCPClient, MCPAgent
from langchain_openai import AzureChatOpenAI

async def main():
    load_dotenv()
    llm = AzureChatOpenAI(
        azure_deployment=os.getenv("AZURE_OPENAI_CHATGPT_DEPLOYMENT"),
        api_version=os.getenv("API_VERSION"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        temperature=0.0,
        streaming=False,
    )

    client = MCPClient.from_config_file("mcp_search.json")
    agent = MCPAgent(llm=llm, client=client, max_steps=3, verbose=True)

    prompt = (
        "Show me the latest results on Ind vs Eng 5th test at Oval "
        "then summarize the titles and links."
    )
    result = await agent.run(prompt)

    # 4) Show the answer + raw tool calls
    print("\n=== Assistant ===\n", result)

if __name__ == "__main__":
    asyncio.run(main())
