import asyncio

from common import timeit, async_timeit

from CoffeeShop import CoffeeShop
from PizzaPlace import PizzaPlace
from CocktailBar import CocktailBar
import threading


@async_timeit
async def async_CoffeeShop():

    coffeeshop = CoffeeShop
    coffee_task = asyncio.create_task(coffeeshop.brewCoffee())
    bagel_task = asyncio.create_task(coffeeshop.toastBagel())
    result_coffee = await coffee_task
    result_bagel = await bagel_task

@async_timeit
async def async_PizzaPlace():

    pizzaplace = PizzaPlace
    pizza_task = asyncio.create_task(pizzaplace.bakePizza())
    wine_task = asyncio.create_task(pizzaplace.pourWine())
    result_pizza = await pizza_task
    result_wine = await wine_task

@async_timeit
async def async_CocktailBar():

    cocktailbar = CocktailBar
    cocktail_task = asyncio.create_task(cocktailbar.shakeCocktail())
    longdrink_task = asyncio.create_task(cocktailbar.stirLongdrink())
    result_cocktail = await cocktail_task
    result_longdrink = await longdrink_task



if __name__ == '__main__':

    @timeit
    def _main():
        _thread = threading.Thread(target=asyncio.run,args=(async_CoffeeShop(),))
        _thread.start()
        _thread_1 = threading.Thread(target=asyncio.run,args=(async_PizzaPlace(),))
        _thread_1.start()
        _thread_2 = threading.Thread(target=asyncio.run,args=(async_CocktailBar(),))
        _thread_2.start()

        _thread.join()
        _thread_1.join()
        _thread_2.join()

    _main()


    # @timeit
    # def _main_2():
    #     asyncio.run(async_CoffeeShop())
    #     asyncio.run(async_PizzaPlace())
    #     asyncio.run(async_CocktailBar())
    #
    # _main_2()


