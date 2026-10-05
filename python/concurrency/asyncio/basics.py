import asyncio

#co routine function that simulates a long-running task
async def main():
    print("Start") #This will print first because it is not a co routine function
    await asyncio.sleep(5) #This will not block the execution of the next line because it is a co routine function
    print("End") #This will print after 5 seconds

if __name__ == "__main__":
    asyncio.run(main())
