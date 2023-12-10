from common import async_timeit
import asyncio

class PizzaPlace:

    # @async_timeit
    async def pourWine():
        print("Start pourWine()")
        await asyncio.sleep(3)
        print("End pourWine()")
        return "Wine poured"

    # @async_timeit
    async def bakePizza():
        print("Start bakePizza()")
        await asyncio.sleep(2)
        print("End bakePizza()")
        return "Pizza baked"
