import os
import requests
import asyncio
from fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()
mcp = FastMCP("CSESearchTool")

@mcp.tool()
def google_search(query: str, num_results: int = 3) -> list[dict]:
    """
    Perform a Google Custom Search and return the top titles+links.
    Uses the official Google CSE JSON API.
    """
    api_key = os.getenv("SERP_API_KEY")
    cse_id  = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

    resp = requests.get(
        "https://www.googleapis.com/customsearch/v1",
        params={
            "key": api_key,
            "cx": cse_id,
            "q": query,
            "num": num_results
        },
        timeout=10
    )
    resp.raise_for_status()
    items = resp.json().get("items", [])
    return [{"title": it.get("title"), "link": it.get("link")} for it in items]

if __name__ == "__main__":
    asyncio.run(mcp.run_sse_async(host="127.0.0.1", port=9203))
