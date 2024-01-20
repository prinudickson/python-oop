import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task = asyncio.create_task(say_after(1,"abc"))
    await asyncio.sleep(1.1)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("fetch_data was canceled!")

asyncio.run(main())
