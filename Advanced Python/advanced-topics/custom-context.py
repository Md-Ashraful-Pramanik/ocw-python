from time import perf_counter, perf_counter_ns

class Timer:
    def __init__(self, is_second=False):
        self.is_second = is_second

    def __enter__(self):
        print("Entering a context")
        self.start = perf_counter_ns()
    
    def __exit__(self, exc_type, exc_value, exc_error):
        print("Exiting a context")

        if self.is_second: self.end = perf_counter()
        else: self.end = perf_counter_ns()

        if self.is_second: unit = 'second'
        else: unit = 'nano-seconds'

        print(f"Elapsed Time ({unit}): {self.end - self.start}")
        

with Timer(is_second=True) as timer:
    sum = 0 
    for i in range(11):
        sum += i 
    print(sum)

