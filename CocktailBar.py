from common import async_timeit
import asyncio
import os

class CocktailBar:

    # @async_timeit
    async def shakeCocktail():
        print("Start shakeCocktail()")
        await asyncio.sleep(3)
        print("End shakeCocktail()")
        print("ID of process running task 1: {}".format(os.getpid()))
        return "Cocktail shaken"
    
    # @async_timeit
    async def stirLongdrink():
        print("Start stirLongdrink()")
        await asyncio.sleep(2)
        print("End stirLongdrink()")
        print("ID of process running task 1: {}".format(os.getpid()))
        return "Longdrink stirred"
