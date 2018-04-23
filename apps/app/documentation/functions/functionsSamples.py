qqq = "qqq"
print("qqq:", qqq)
print("abs(1.2):", abs(1.2))
# ==============================================================================
print("ascii(qqq):", ascii(qqq))
# ==============================================================================
print("bin(3):", bin(3))
print("bin(-10):", bin(-10))
# ==============================================================================
print("format(14, '#b'), format(14, 'b'):", format(14, '#b'), format(14, 'b'))
print("f'{14:#b}', f'{14:b}'", f'{14:#b}:', f'{14:b}')

# ==============================================================================
"""A class method receives the class as implicit first argument, just like an 
instance method receives the instance."""


class C:
    @classmethod
    def f(cls, arg1, arg2):
        print("hello there")
# ==============================================================================
