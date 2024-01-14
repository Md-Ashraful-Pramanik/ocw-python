# I love Bangladesh => 100 print
# similar types of repeated work

i = 0 # counter variable initialize
while i < 5: # condition checking
    i = i + 1 # counter increment
    print(f"{i} I love Bangladesh")

# n user input 
# 1 + 2 + 3 + ... + n = ?
# Ex- for n=5 , 1+2+3+4+5=15

sum = 0
n = int(input())

i = 0
while i < n:
    i = i + 1
    sum = sum + i

print(f"Summation: {sum}")

# 1*2*3* ... *n = n! = ?

prod = 1
n = int(input())

i = 0
while i < n:
    i = i + 1
    prod = prod * i

print(f"Factorial: {prod}")

# Exercise:
# 1^2 + 2^2 + 3^2 + ... + n^2 = ?
# 1^3 + 2^3 + 3^3 + ... + n^3 = ?
# 1/1 + 1/2 + 1/3 + ... + 1/n = ?
