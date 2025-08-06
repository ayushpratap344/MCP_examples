# server_async.py
import asyncio
from fastmcp import FastMCP

mcp = FastMCP("SimpleTools")

@mcp.tool()
def echo(text: str) -> str:
    return text

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    asyncio.run(
        mcp.run_sse_async(host="127.0.0.1", port=8931, log_level="info")
    )
