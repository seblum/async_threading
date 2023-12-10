from common import async_timeit
import asyncio

class CoffeeShop:

    # @async_timeit
    async def brewCoffee():
        print("Start brewCoffee()")
        await asyncio.sleep(3)
        print("End brewCoffee()")
        return "Coffee ready"
    
    # @async_timeit
    async def toastBagel():
        print("Start toastBagel()")
        await asyncio.sleep(2)
        print("End toastBagel()")
        return "Bagel toasted"
