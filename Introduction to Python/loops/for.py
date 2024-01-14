a = [10, 5, 60, 100]

sum = 0
for el in a:
    sum = sum + el

print(sum)

# Use of continue statement
# Let say we want to sum all the elements of a list except the elements which are less than 5
a = [10, 5, 60, 100, 3, 465]

sum = 0
for el in a:
    if el < 5:
        continue
    sum = sum + el

print(sum)

# Use of continue statement
# Let say we want to sum all the elements of a list until we found one element that is less than 5
a = [10, 5, 60, 100, 3, 465]

sum = 0
for el in a:
    if el < 5:
        break
    sum = sum + el

print(sum)


# Else statement
i = 0
sum = 0
while i < len(a):
    if a[i] < 5:
        break
    sum = sum + a[i]
    i = i + 1
else:
    print('Else executed')
    print(f'value of i: {i}')
print(sum)

print(f'value of i: {i}')

# Else with continue statement
sum = 0
for el in a:
    if el < 0:
        continue
    sum = sum + el
else:
    print('Else executed')

print(sum)

# Else with break statement
sum = 0
for el in a:
    if el < 0:
        break
    sum = sum + el
else:
    print('Else executed')

print(sum)


# Summary:
# continue => moves to condition checking
# break => Forcefully break the loop
# else => `while` when condition becomes false it will execute
#      => `for` when all the elements are processed
#      => if `break` executes then else will not be executed 
