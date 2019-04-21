"""If you're writing a short throwaway function whose body
fits into a single line (like mod_5 above), Python's lambda
syntax is conveniently compact.
"""
mod_5 = lambda x: x % 5

# Note that we don't use the "return" keyword above (it's implicit)
# (The line below would produce a SyntaxError)
# mod_5 = lambda x: return x % 5

print('101 mod 5 =', mod_5(101))
