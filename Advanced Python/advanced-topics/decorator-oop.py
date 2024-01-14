from time import perf_counter_ns, perf_counter


class Timer:
    def __init__(
            self, 
            func, 
            is_second=False, 
            param_test=True,
            msg="",
        ):
        self.func = func 
        self.is_second = is_second
        self.param_test = param_test
        self.msg = msg
    
    def __call__(self, *args, **kwargs):
        print("Enter in decorator")
        if self.is_second: start = perf_counter()
        else: start = perf_counter_ns()

        return_value = self.func(*args, **kwargs)
        
        if self.is_second: end = perf_counter()
        else: end = perf_counter_ns()
        
        if self.is_second: unit = 'second'
        else: unit = 'nano-seconds'

        print(f"Elapsed Time ({unit}): {end - start}")
        
        print(self.param_test)
        print(self.msg)
        return return_value


def timer(func=None, *args, **kwargs):
    if func:
        return Timer(func, *args, **kwargs)
    else:
        def inner(inner_func):
            return Timer(inner_func, *args, **kwargs)
        return inner

@timer(is_second=True, msg="heello!!")
def simple_func(name, email="hello"):
    print(f"Hello {name}, {email}")
    return 10

x = simple_func("Ashraful")
print(x)
