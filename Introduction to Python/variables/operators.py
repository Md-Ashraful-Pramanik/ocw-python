# Arithmatic Operator

a, b = 50, 3

print(f"Addition:       {a} + {b} = {a+b}")
print(f"Subtraction:    {a} - {b} = {a-b}")
print(f"Multiplication: {a} * {b} = {a*b}")
print(f"Division:       {a} / {b} = {a/b}")
print(f"Int Division:   {a} // {b} = {a//b}")
print(f"Remainder:      {a} % {b} = {a%b}")
print(f"Power:          {a} ** {b} = {a**b}")


# assignment operator
a = 10
print(a)

a, b, c = 50, 60, 5
print(a)
print(b)
print(c)


# Comparison operator
a, b = 50, 3
print(f"Greater Than:      {a} > {b} = {a > b}")
print(f"Greater or Equal:  {a} >= {b} = {a >= b}")
print(f"Less Than:         {a} < {b} = {a < b}")
print(f"Less or Equal:     {a} <= {b} = {a <= b}")
print(f"Whether Equal:     {a} == {b} = {a == b}")
print(f"Whether Not Equal: {a} != {b} = {a != b}")


# Logical Operator (Operates on boolean operands)
a, b = False, True

print(a and b) # If all of them is True then True
print(a or b)  # If at least one is True then True
print(not b)   # toggle True and False



# Bitwise operator
a, b = 10, 2

print(bin(a))
print(bin(b))

print(bin(a & b)) # AND
print(bin(a | b)) # OR
print(bin(a ^ b)) # XOR

# number system conversion
print(bin(50))
print(hex(50))
print(oct(50))


a = 0x32
print(a)

a = 0b1010
print(a)

a = 7e-2 # 7 X 10^-2
print(a)


# Operator precedence
a = 10 * 5 + 3 
# multiplication first: 50 + 3 = 53
# addition first:       10 * 8 = 80

print(a)

print((5*10)/(15*5)) 
# multiplication first: 50 / 15 * 5 = 50 / 15*5 = 3.333 * 5 = 16..
# 5*10/15*5 = 50 / 75 = 0.666

# Short hand operator
x = 500
# x = x + 50
x **= 7
print(x)
b = 5 * 10 / 15 * 5
print(b)