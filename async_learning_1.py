import asyncio


async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(4)  # Simulating an I/O operation
    print("Done fetching")
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(fetch_data())
    # value = await task1
    # print(value)
    task2 = asyncio.create_task(print_numbers())
    value = await task1
    print(value)


asyncio.run(main())