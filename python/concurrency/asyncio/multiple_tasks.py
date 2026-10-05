import asyncio
async def api_call(url:str, delay:int=3):
    # Simulate a delay for the API call
    print(f"Fetching data from {url}...")
    await asyncio.sleep(delay)
    return f"Data from {url}"

async def execute_tasks():
    await asyncio.sleep(3)
    print("Executing API call...")

async def transform_data(data:str):
    # Simulate a delay for data transformation
    await asyncio.sleep(2)
    print(f"Transforming data: {data}")
    return f"Transformed {data}"

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
        api_call("https://api.example.com/orders/1", 3),   
        execute_tasks(),
        transform_data("Sample Data"),
        api_call("https://api.example.com/orders/5", 6)
    )
    print("Executing API calls...")
    print(f"API call results: {tasks}")
    # tasks = [api_call(f"https://api.example.com/orders/{i}") for i in range(5)]
    # results = await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
