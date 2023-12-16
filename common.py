import time
from functools import wraps
import asyncio


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


def async_timeit(func):
    async def process(func, *args, **kwargs):
        if asyncio.iscoroutinefunction(func):
            # print('this function is a coroutine: {}'.format(func.__name__))
            return await func(*args, **kwargs)
        else:
            print('this is not a coroutine')
            return func(*args, **kwargs)

    async def helper(*args, **kwargs):
        # print('{}.time'.format(func.__name__))
        start = time.time()
        result = await process(func, *args, **kwargs)

        # Test normal function route...
        # result = await process(lambda *a, **p: print(*a, **p), *args, **params)

        total_time = time.time() - start
        print(f'AsyncFunction {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')

        # print('>>>', time.time() - start)
        return result

    return helper
