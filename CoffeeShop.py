from common import async_timeit
import asyncio
import os
class CoffeeShop:

    # @async_timeit
    async def brewCoffee():
        print("Start brewCoffee()")
        await asyncio.sleep(3)
        print("End brewCoffee()")
        print("ID of process running task 1: {}".format(os.getpid()))
        return "Coffee ready"
    
    # @async_timeit
    async def toastBagel():
        print("Start toastBagel()")
        await asyncio.sleep(2)
        print("End toastBagel()")
        print("ID of process running task 1: {}".format(os.getpid()))
        return "Bagel toasted"
