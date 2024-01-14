# print
print("Hello", "world", "!!!", sep="**", end='#')
print("Hello", "world", "!!!", sep="**", end='$')
# default value of `sep` is space
# default value of `end` new line

# input
print("This program will take two integer numbers and print their minus")
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
print(f'Minus of {a} and {b}: {a - b}')

# sum, avg, min, max, len
a = [5, 6, 8, 6, 3]

print(len(a))
print(min(a))
print(max(a))
print(sum(a))
print(sum(a)/len(a))  # average using built-in functions
