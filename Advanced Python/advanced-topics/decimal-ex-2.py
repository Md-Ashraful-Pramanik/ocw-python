import decimal
from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.1')
c = Decimal('0.1')

# scientific
with decimal.localcontext() as localcontext:
    # Local context
    print("Local context")
    localcontext.prec = 100
    localcontext.rounding = decimal.ROUND_HALF_UP
    print(round(Decimal('1.15'), 1))
    print(round(Decimal('1.25'), 1))
    print(round(Decimal('1.35'), 1))
    print(round(Decimal('1.45'), 1))
    print(round(Decimal('1.49'), 1))
    print(round(Decimal('1.41'), 1))


# Global context
print("Global context")
print(round(Decimal('1.15'), 1))
print(round(Decimal('1.25'), 1))
print(round(Decimal('1.35'), 1))
print(round(Decimal('1.45'), 1))
print(round(Decimal('1.49'), 1))
print(round(Decimal('1.41'), 1))