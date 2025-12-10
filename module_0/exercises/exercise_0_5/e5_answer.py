import asyncio

async def run_experiment(name: str, seconds: int):
    print(f"[{name}] starting...")
    await asyncio.sleep(seconds)
    print(f"[{name}] finished after {seconds} seconds")
    return name, seconds

async def main():
    tasks = [
        run_experiment("exp_small", 1),
        run_experiment("exp_medium", 2),
        run_experiment("exp_large", 3),
    ]
    results = await asyncio.gather(*tasks)
    print("All done:", results)

asyncio.run(main())