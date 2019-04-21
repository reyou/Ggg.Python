import os

restFiles = [os.path.join(d[0], f) for d in os.walk(".")
             for f in d[2] if f.endswith(".py")]

print("type(restFiles):", type(restFiles))
for r in restFiles:
    print(r)
