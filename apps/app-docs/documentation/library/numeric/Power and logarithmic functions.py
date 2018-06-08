from math import exp, expm1
res = exp(1e-5) - 1  # gives result accurate to 11 places
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
res = expm1(1e-5)    # result accurate to full precision
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
