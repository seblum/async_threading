import asyncio
import threading
import time
import multiprocessing

from common import timeit, async_timeit
from Shop import CoffeeShop, PizzaPlace, CocktailBar

@async_timeit
async def async_CoffeeShop(table):

    coffeeshop = CoffeeShop(table=table)
    coffee_task = asyncio.create_task(coffeeshop.brewCoffee())
    bagel_task = asyncio.create_task(coffeeshop.toastBagel())
    result_coffee = await coffee_task
    result_bagel = await bagel_task

    # result_coffee, result_bagel = await asyncio.gather(coffee_task, bagel_task)

@async_timeit
async def async_PizzaPlace(table):

    pizzaplace = PizzaPlace(table=table)
    pizza_task = asyncio.create_task(pizzaplace.bakePizza())
    wine_task = asyncio.create_task(pizzaplace.pourWine())

    result_pizza, result_wine = await asyncio.gather(pizza_task, wine_task)

@async_timeit
async def async_CocktailBar(table):

    cocktailbar = CocktailBar(table=table)
    cocktail_task = asyncio.create_task(cocktailbar.shakeCocktail())
    longdrink_task = asyncio.create_task(cocktailbar.stirLongdrink())
    result_cocktail = await cocktail_task
    result_longdrink = await longdrink_task


def visit_CocktailBar():
    asyncio.run(async_CocktailBar())

def visit_CoffeeShop():
    asyncio.run(async_CoffeeShop())

def visit_PizzaPlace():
    asyncio.run(async_PizzaPlace())


def multiple_visit_CocktailBar():
    _thread = threading.Thread(target=asyncio.run,args=(async_CocktailBar(table=1),))
    _thread.start()
    _thread_1 = threading.Thread(target=asyncio.run,args=(async_CocktailBar(table=2),))
    _thread_1.start()
    _thread.join()
    _thread_1.join()

def multiple_visit_CoffeeShop():
    _thread = threading.Thread(target=asyncio.run,args=(async_CoffeeShop(table=1),))
    _thread.start()
    _thread_1 = threading.Thread(target=asyncio.run,args=(async_CoffeeShop(table=2),))
    _thread_1.start()
    _thread.join()
    _thread_1.join()

def multiple_visit_PizzaPlace():
    _thread = threading.Thread(target=asyncio.run,args=(async_PizzaPlace(table=1),))
    _thread.start()
    _thread_1 = threading.Thread(target=asyncio.run,args=(async_PizzaPlace(table=2),))
    _thread_1.start()
    _thread.join()
    _thread_1.join()


if __name__ == '__main__':

    @timeit
    def _main():
        print("> MULTITHREADING")
        _thread = threading.Thread(target=asyncio.run,args=(async_CoffeeShop(),))
        _thread.start()
        _thread_1 = threading.Thread(target=asyncio.run,args=(async_PizzaPlace(),))
        _thread_1.start()
        _thread_2 = threading.Thread(target=asyncio.run,args=(async_CocktailBar(),))
        _thread_2.start()

        _thread.join()
        _thread_1.join()
        _thread_2.join()

    # _main()

    @timeit
    def _main_2():
        # separate coroutine and event-loop for each
        asyncio.run(async_CoffeeShop())
        asyncio.run(async_PizzaPlace())
        asyncio.run(async_CocktailBar())
    
    # _main_2()

    @timeit
    def _main_3():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            # enqueue coroutine onto the loop
            asyncio.ensure_future(async_CoffeeShop())
            asyncio.ensure_future(async_PizzaPlace())
            asyncio.ensure_future(async_CocktailBar())
            loop.run_forever()
            # time.sleep(10)
            # loop.stop()
        except KeyboardInterrupt:
            pass
        finally:
            print("Closing Loop")
            loop.close()
        
    # _main_3()

    @timeit
    def _main_4():
        print("> MULTIPROCESSING")
        _process = multiprocessing.Process(target=visit_CoffeeShop,args=())
        _process.start()
        _process_1 = multiprocessing.Process(target=visit_PizzaPlace,args=())
        _process_1.start()
        _process_2 = multiprocessing.Process(target=visit_CocktailBar,args=())
        _process_2.start()

        _process.join()
        _process_1.join()
        _process_2.join()

    # _main_4()
        
    
    @timeit
    def _main_5():
        _process = multiprocessing.Process(target=multiple_visit_CoffeeShop,args=())
        _process.start()
        _process_1 = multiprocessing.Process(target=multiple_visit_PizzaPlace,args=())
        _process_1.start()
        _process_2 = multiprocessing.Process(target=multiple_visit_CocktailBar,args=())
        _process_2.start()

        _process.join()
        _process_1.join()
        _process_2.join()

    _main_5()