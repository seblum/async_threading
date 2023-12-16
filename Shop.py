from common import async_timeit
import asyncio
import os
import threading
import multiprocessing


class PizzaPlace:

    def __init__(self, table:int):
        self.table = table

    # @async_timeit
    async def pourWater(self):
        print(f"Start pourWater(table={self.table}) - Thread: {threading.get_native_id()} | Process: {multiprocessing.current_process()}, {os.getpid()}")
        await asyncio.sleep(3)
        print(f"End pourWater(table={self.table})")
        return "Water poured"

    # @async_timeit
    async def bakePizza(self):
        print(f"Start bakePizza(table={self.table}) - Thread: {threading.get_native_id()} | Process: {multiprocessing.current_process()}, {os.getpid()}")
        await asyncio.sleep(2)
        print(f"End bakePizza(table={self.table})")
        return "Pizza baked"



class CocktailBar:

    def __init__(self, table:int):
        self.table = table
        

    # @async_timeit
    async def shakeCocktail(self):
        print(f"Start shakeCocktail(table={self.table}) - Thread: {threading.get_native_id()} | Process: {multiprocessing.current_process()}, {os.getpid()}")
        await asyncio.sleep(3)
        print(f"End shakeCocktail(table={self.table})")
        return "Cocktail shaken"
    
    # @async_timeit
    async def stirLongdrink(self):
        print(f"Start stirLongdrink(table={self.table}) - Thread: {threading.get_native_id()} | Process: {multiprocessing.current_process()}, {os.getpid()}")
        await asyncio.sleep(2)
        print(f"End stirLongdrink(table={self.table})")
        return "Longdrink stirred"



class CoffeeShop:

    def __init__(self, table:int):
        self.table = table
        

    # @async_timeit
    async def brewCoffee(self):
        print(f"Start brewCoffee(table={self.table}) - Thread: {threading.get_native_id()} | Process: {multiprocessing.current_process()}, {os.getpid()}")
        await asyncio.sleep(3)
        print(f"End brewCoffee(table={self.table})")
        return "Coffee ready"
    
    # @async_timeit
    async def toastBagel(self):
        print(f"Start toastBagel(table={self.table}) - Thread: {threading.get_native_id()} | Process: {multiprocessing.current_process()}, {os.getpid()}")
        await asyncio.sleep(2)
        print(f"End toastBagel(table={self.table})")
        return "Bagel toasted"
