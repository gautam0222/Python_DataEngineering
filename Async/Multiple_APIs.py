import asyncio 

async def api_call(url:str):
    # Simulate a delay for the API call
    print(f"Fetching data from {url}...")
    await asyncio.sleep(3)
    return f"Data from {url}"

async def execute_api_call():
    print("Executing API call...")
    result = await api_call("https://api.example.com/orders")
    print(f"API call result: {result}")

async def main():
    print("Executing API call...")
    result = await api_call("https://api.example.com/orders")
    print(f"API call result: {result}")

    #Create a list of tasks for multiple API calls
    tasks= await asyncio.gather(
        api_call("https://api.example.com/orders/1"),   
        api_call("https://api.example.com/orders/2"),
        api_call("https://api.example.com/orders/3"),
        api_call("https://api.example.com/orders/4"),
        api_call("https://api.example.com/orders/5")
    )
    print("Executing API calls...")
    print(f"API call results: {tasks}")
    # tasks = [api_call(f"https://api.example.com/orders/{i}") for i in range(5)]
    # results = await asyncio.gather(*tasks)


asyncio.run(main())