from time import perf_counter_ns

def timer(func):
    def inner(*args, **kwargs):
        print("Enter in decorator")
        start = perf_counter_ns()
        func(*args, **kwargs)
        end = perf_counter_ns()
        print(f"Elapsed Time: {end - start}")
    
    return inner

@timer
def simple_func(name, email="hello"):
    print(f"Hello {name}, {email}")


simple_func("Ashraful")
