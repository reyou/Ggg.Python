try:
    result = 5 / (10 - 10)
except ZeroDivisionError:
    print("Cannot divide by zero exception.")

try:
    result = int("five")
except ValueError:
    print("Cannot parse string as int.")
