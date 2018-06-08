from decimal import *
getcontext().prec = 6
res = Decimal(1) / Decimal(7)
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
getcontext().prec = 28
res = Decimal(1) / Decimal(7)
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
