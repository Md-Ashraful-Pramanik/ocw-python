from functools import cache, lru_cache
from time import perf_counter, perf_counter_ns
import random

@lru_cache
def fibo_caching(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_caching(n-1) + fibo_caching(n-2)

start_time = perf_counter_ns()
for i in range(10):
    fibo_caching(random.randint(1, 20))
end_time = perf_counter_ns()

print(f"Elapsed Time using caching: {end_time - start_time} ns")
caching_time = end_time - start_time

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

start_time = perf_counter_ns()
for i in range(10):
    fibo(random.randint(1, 20))
end_time = perf_counter_ns()

print(f"Elapsed Time without caching: {end_time - start_time} ns")
without_cache_time = end_time - start_time

print(f"Ratio: {without_cache_time / caching_time}")
