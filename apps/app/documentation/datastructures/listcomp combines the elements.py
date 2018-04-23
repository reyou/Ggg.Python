filtered_list = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print("filtered_list", filtered_list)
# and it’s equivalent to:
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print("combs", combs)
