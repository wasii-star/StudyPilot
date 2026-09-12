import asyncio
from mcp import stdio_client, StdioServerParameters, ClientSession

server_params = StdioServerParameters(
    command="python3",
    args=["server.py"],
)


async def main():
    print("1. Starting")

    async with stdio_client(server_params) as (read, write):
        print("2. Connected")

        async with ClientSession(read, write) as session:
            print("3. Session created")

            await session.initialize()
            print("4. Initialized")

            resources = await session.list_resources()
            print(resources)

            templates = await session.list_resource_templates()
            print(templates)

            # result = await session.read_resource("notes://python_basics.md")
            # print("5. Resource received")
            # print(result)
            
            result = await session.call_tool("search_notes", {"query": "function"})
            print(result)

asyncio.run(main())
