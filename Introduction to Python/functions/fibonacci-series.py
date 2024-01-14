"""
fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
fibonacci(0) = 0
fibonacci(1) = 1

Example-
0 => 0
1 => 1
2 => 1
3 => 2
4 => 3
5 => 5
6 => 8
"""

def fibo(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    
    return fibo(n-1)  + fibo(n-2)

print(fibo(4))
print(fibo(5))

