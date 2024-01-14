from time import perf_counter_ns, perf_counter

def timer(is_second=False):
    def inner_timer(func):
        def inner(*args, **kwargs):
            print("Enter in decorator")
            if is_second: start = perf_counter()
            else: start = perf_counter_ns()

            return_value = func(*args, **kwargs)
            
            if is_second: end = perf_counter()
            else: end = perf_counter_ns()
            
            if is_second: unit = 'second'
            else: unit = 'nano-seconds'

            print(f"Elapsed Time ({unit}): {end - start}")
            
            return return_value
        
        return inner
    return inner_timer

@timer(is_second=True)
def simple_func(name, email="hello"):
    print(f"Hello {name}, {email}")
    return 10


x = simple_func("Ashraful")
print(x)
