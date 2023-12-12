from common import async_timeit
import asyncio
import os

class PizzaPlace:

    # @async_timeit
    async def pourWine():
        print("Start pourWine()")
        await asyncio.sleep(3)
        print("End pourWine()")
        print("ID of process running task 1: {}".format(os.getpid()))
        return "Wine poured"

    # @async_timeit
    async def bakePizza():
        print("Start bakePizza()")
        await asyncio.sleep(2)
        print("End bakePizza()")
        print("ID of process running task 1: {}".format(os.getpid()))
        return "Pizza baked"
