from time import perf_counter_ns

def timer(func):
    def inner():
        print("Enter in decorator")
        start = perf_counter_ns()
        func()
        end = perf_counter_ns()
        print(f"Elapsed Time: {end - start}")
    
    return inner

@timer
def simple_func():
    print("Inside simple func")


simple_func()
