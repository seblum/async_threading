import asyncio

from common import timeit, async_timeit

from CoffeeShop import CoffeeShop
from PizzaPlace import PizzaPlace
from CocktailBar import CocktailBar



@async_timeit
async def async_main():

    coffeeshop = CoffeeShop
    coffee_task = asyncio.create_task(coffeeshop.brewCoffee())
    bagel_task = asyncio.create_task(coffeeshop.toastBagel())
    result_coffee = await coffee_task
    result_bagel = await bagel_task

    pizzaplace = PizzaPlace
    pizza_task = asyncio.create_task(pizzaplace.bakePizza())
    wine_task = asyncio.create_task(pizzaplace.pourWine())
    result_pizza = await pizza_task
    result_wine = await wine_task

    cocktailbar = CocktailBar
    cocktail_task = asyncio.create_task(cocktailbar.shakeCocktail())
    longdrink_task = asyncio.create_task(cocktailbar.stirLongdrink())
    result_cocktail = await cocktail_task
    result_longdrink = await longdrink_task

if __name__ == '__main__':
    asyncio.run(async_main())

