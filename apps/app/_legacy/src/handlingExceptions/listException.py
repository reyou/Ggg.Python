sum = 0
i = 0
for i in range(10):
    try:
        if i % 2 == 0:
            mid = i / 0
        sum += i
    except ZeroDivisionError:
        pass
print("Sum =", sum)
