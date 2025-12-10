import asyncio

async def fetch_data(name: str):
    print(f"Starting {name}")
    await asyncio.sleep(2)  # pretend this is a slow API call
    print(f"Finished {name}")

async def main():
    tasks = [
        fetch_data("task 1"),
        fetch_data("task 2"),
        fetch_data("task 3"),
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())