import asyncio
import os
from mcp import stdio_client, StdioServerParameters, ClientSession

server_params = StdioServerParameters(
    command="python3",
    args=[os.path.join(os.path.dirname(__file__), "server.py")],
)


async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Discover what the server offers
            resources = await session.list_resources()
            print("Resources:", [r.uri for r in resources.resources])

            tools = await session.list_tools()
            print("Tools:", [t.name for t in tools.tools])

            # Example: read a resource
            notes = await session.read_resource("notes://list")
            print("\nNotes:", notes)

            # Example: use the study session prompt
            prompt = await session.get_prompt("prepare_study_session", {"course_name": "Python"})
            print("\nPrompt:", prompt)


asyncio.run(main())