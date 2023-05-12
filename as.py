import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    return f"{what} - {delay}"

async def main():

    print(f"started at {time.strftime('%X')}")

    ret1 = await asyncio.gather(say_after(1,'hello'), say_after(2,'world'))

    print(ret1)

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

# started at 12:57:20
# ['hello - 1', 'world - 2']
# finished at 12:57:22