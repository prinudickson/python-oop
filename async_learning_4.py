import asyncio

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    # Schedule the setting of the result
    loop.call_soon(future.set_result, "Future is done!")

    result = await future
    print(result)

asyncio.run(main())
