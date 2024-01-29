from functools import lru_cache
from time import perf_counter
from typing import Callable
import matplotlib.pyplot as plt


times: [float] = []


def timer(func: Callable):
    def wrap(*args, **kwargs):
        t1 = perf_counter()
        result = func(*args, **kwargs)
        t2 = perf_counter()
        runtime = t2 - t1
        print(f"Finished in {runtime}: f({args[0]}) -> {result}")
        times.append(runtime)
        return result

    return wrap


def create_graph():
    numbers = [x for x in range(101)]
    plt.plot(numbers, times)
    plt.xlabel("Fibonacci number")
    plt.ylabel("Time (s)")
    plt.savefig("images/timing_plot.png")


@lru_cache
@timer
def fib(n: int) -> int:
    if n < 1:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    fib(100)
    create_graph()
