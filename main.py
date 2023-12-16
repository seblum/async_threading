import asyncio
import threading
import time
import multiprocessing

from common import timeit, async_timeit
from Shop import CoffeeShop, PizzaPlace, CocktailBar

@async_timeit
async def order_at_CoffeeShop(table):

    coffeeshop = CoffeeShop(table=table)
    coffee_task = asyncio.create_task(coffeeshop.brewCoffee())
    bagel_task = asyncio.create_task(coffeeshop.toastBagel())
    result_coffee = await coffee_task
    result_bagel = await bagel_task

    # result_coffee, result_bagel = await asyncio.gather(coffee_task, bagel_task)

@async_timeit
async def order_at_PizzaPlace(table):

    pizzaplace = PizzaPlace(table=table)
    pizza_task = asyncio.create_task(pizzaplace.bakePizza())
    water_task = asyncio.create_task(pizzaplace.pourWater())

    result_pizza, result_water = await asyncio.gather(pizza_task, water_task)

@async_timeit
async def order_at_CocktailBar(table):

    cocktailbar = CocktailBar(table=table)
    cocktail_task = asyncio.create_task(cocktailbar.shakeCocktail())
    longdrink_task = asyncio.create_task(cocktailbar.stirLongdrink())
    result_cocktail = await cocktail_task
    result_longdrink = await longdrink_task


@timeit
def multiple_visit_CocktailBar():
    _thread = threading.Thread(target=asyncio.run,args=(order_at_CocktailBar(table=1),))
    _thread.start()
    _thread_1 = threading.Thread(target=asyncio.run,args=(order_at_CocktailBar(table=2),))
    _thread_1.start()
    _thread.join()
    _thread_1.join()

@timeit
def multiple_visit_CoffeeShop():
    _thread = threading.Thread(target=asyncio.run,args=(order_at_CoffeeShop(table=1),))
    _thread.start()
    _thread_1 = threading.Thread(target=asyncio.run,args=(order_at_CoffeeShop(table=2),))
    _thread_1.start()
    _thread.join()
    _thread_1.join()

@timeit
def multiple_visit_PizzaPlace():
    _thread = threading.Thread(target=asyncio.run,args=(order_at_PizzaPlace(table=1),))
    _thread.start()
    _thread_1 = threading.Thread(target=asyncio.run,args=(order_at_PizzaPlace(table=2),))
    _thread_1.start()
    _thread.join()
    _thread_1.join()


if __name__ == '__main__':
    
    @timeit
    def go_out():
        _process = multiprocessing.Process(target=multiple_visit_CoffeeShop,args=())
        _process.start()
        _process_1 = multiprocessing.Process(target=multiple_visit_PizzaPlace,args=())
        _process_1.start()
        _process_2 = multiprocessing.Process(target=multiple_visit_CocktailBar,args=())
        _process_2.start()

        _process.join()
        _process_1.join()
        _process_2.join()

    go_out()