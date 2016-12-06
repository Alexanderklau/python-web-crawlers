import uvloop
import asyncio

loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)


async def compute(a, b):
    print("Computing {} + {}...".format(a, b))
    await asyncio.sleep(a + b)
    return a + b


tasks = []
for i, j in zip(range(3), range(3)):
    print(i, j)
    tasks.append(compute(i, j))
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()