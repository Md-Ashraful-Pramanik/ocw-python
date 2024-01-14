class EvenNumbers:
    def __init__(self, start, max):
        self.start = start
        self.max = max
    
    def __iter__(self):
        self.number = self.start - 2
        return self
    
    def __next__(self):
        self.number += 2
        if self.number > self.max:
            raise StopIteration
    
        return self.number

even_numbers = EvenNumbers(50, 60)
iterator = iter(even_numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))