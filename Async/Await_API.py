#Normal Synchronous API call simulation
# import time

# def api_call():
#     time.sleep(3)  # Simulate a delay for the API call
#     return "Orders Data"

# def execute_api_call():
#     print("Executing API call...")
#     result = api_call()
#     print(f"API call result: {result}")

# execute_api_call()

#Asynchronous API call simulation using asyncio
import asyncio
async def api_call():
    # Simulate a delay for the API call
    await asyncio.sleep(3)
    return "Orders Data"

async def execute_api_call():
    print("Executing API call...")
    result = await api_call()
    print(f"API call result: {result}")

async def main():
    print("Executing API call...")
    result = await api_call()
    print(f"API call result: {result}")

asyncio.run(main())