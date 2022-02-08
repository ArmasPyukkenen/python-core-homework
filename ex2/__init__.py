from ex2 import fetcher
from time import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        # put your code here
        def inner_wrapper(arg):
            timesum = 0
            for i in range(num):
                start = time()
                func(arg)
                duration = time() - start
                timesum += duration
                print(duration)
            print(timesum / num)
        return inner_wrapper
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
