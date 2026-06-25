import asyncio
from google.adk.agents.context import Context
from app.agent import root_agent

async def main():
    print("Initializing agent...")
    
    ctx = Context(session_id="local-test")
    user_input = "What should I reorder today?"
    print(f"\nUSER: {user_input}")
    
    async for event in root_agent.run_async(ctx, user_input=user_input):
        if getattr(event, "message", None):
            print("\nAGENT:", event.message.content)

if __name__ == "__main__":
    asyncio.run(main())
