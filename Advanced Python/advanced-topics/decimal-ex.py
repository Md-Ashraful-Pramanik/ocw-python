import decimal
from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.1')
c = Decimal('0.1')

print(a+b+c)

context = decimal.getcontext()
context.prec = 100

# ROUND_HALF_UP
context.rounding = decimal.ROUND_HALF_UP
print("ROUND_HALF_UP")
print(round(Decimal('1.15'), 1))
print(round(Decimal('1.25'), 1))
print(round(Decimal('1.35'), 1))
print(round(Decimal('1.45'), 1))
print(round(Decimal('1.49'), 1))
print(round(Decimal('1.41'), 1))

# ROUND_HALF_DOWN
context.rounding = decimal.ROUND_HALF_DOWN
print("ROUND_HALF_DOWN")
print(round(Decimal('1.15'), 1))
print(round(Decimal('1.25'), 1))
print(round(Decimal('1.35'), 1))
print(round(Decimal('1.45'), 1))
print(round(Decimal('1.49'), 1))
print(round(Decimal('1.41'), 1))

# ROUND_HALF_EVEN
context.rounding = decimal.ROUND_HALF_EVEN
print('ROUND_HALF_EVEN')
print(round(Decimal('1.15'), 1))
print(round(Decimal('1.25'), 1))
print(round(Decimal('1.35'), 1))
print(round(Decimal('1.45'), 1))
print(round(Decimal('1.49'), 1))
print(round(Decimal('1.41'), 1))


