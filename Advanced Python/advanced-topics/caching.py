from functools import cache, lru_cache
from time import perf_counter, perf_counter_ns
import random

@lru_cache
def factorial_caching(n):
    if n == 0:
        return 1
    return n * factorial_caching(n-1)

start_time = perf_counter_ns()
for i in range(1000):
    factorial_caching(random.randint(1, 15))
end_time = perf_counter_ns()

print(f"Elapsed Time using caching: {end_time - start_time} ns")


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

start_time = perf_counter_ns()
for i in range(1000):
    factorial(random.randint(1, 15))
end_time = perf_counter_ns()

print(f"Elapsed Time without caching: {end_time - start_time} ns")
