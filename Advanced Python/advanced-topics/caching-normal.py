from functools import cache, lru_cache
from time import perf_counter, perf_counter_ns
import random

@lru_cache(maxsize=1000)
def get_sum_cache(n):
    sum = 0
    for i in range(n+1):
        sum += i 
    return sum

start_time = perf_counter_ns()
for i in range(10000):
    get_sum_cache(random.randint(1, 1000))
end_time = perf_counter_ns()

print(f"Elapsed Time using caching: {end_time - start_time} ns")
caching_time = end_time - start_time

def get_sum(n):
    sum = 0
    for i in range(n+1):
        sum += i 
    return sum

start_time = perf_counter_ns()
for i in range(10000):
    get_sum(random.randint(1, 1000))
end_time = perf_counter_ns()

print(f"Elapsed Time without caching: {end_time - start_time} ns")
without_cache_time = end_time - start_time

print(f"Ratio: {without_cache_time / caching_time}")
