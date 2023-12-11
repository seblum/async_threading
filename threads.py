import threading
import time
from common import timeit
import asyncio
import os

# @async_timeit
def brewCoffee():
    print("Start brewCoffee()")
    time.sleep(3)
    print("End brewCoffee()")
    print("ID of process running task 1: {}".format(os.getpid()))
    return "Coffee ready"

# @async_timeit
def toastBagel():
    print("Start toastBagel()")
    time.sleep(2)
    print("End toastBagel()")
    print("ID of process running task 1: {}".format(os.getpid()))
    return "Bagel toasted"

@timeit
def main():
    t1 = threading.Thread(target=brewCoffee)
    t2 = threading.Thread(target=toastBagel)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

main()