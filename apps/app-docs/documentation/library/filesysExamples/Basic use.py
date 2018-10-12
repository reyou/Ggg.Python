from pathlib import Path

p = Path('C:\\')
res = p
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
res = [x for x in p.iterdir() if x.is_dir()]
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
