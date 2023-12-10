from common import async_timeit
import asyncio

class CocktailBar:

    # @async_timeit
    async def shakeCocktail():
        print("Start shakeCocktail()")
        await asyncio.sleep(3)
        print("End shakeCocktail()")
        return "Cocktail shaken"
    
    # @async_timeit
    async def stirLongdrink():
        print("Start stirLongdrink()")
        await asyncio.sleep(2)
        print("End stirLongdrink()")
        return "Longdrink stirred"
