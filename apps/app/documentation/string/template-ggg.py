from string import Template

s = Template('$who likes $what')
res4 = s.substitute(who='tim', what='kung pao')

d = dict(who='tim', what='kung pao')
res1 = Template('Give $who $$100').substitute(d)

res2 = Template('$who likes $what').substitute(d)

res3 = Template('$who likes $what').safe_substitute(d)

print("res1:")
print(res1)
print()
print("res2:")
print(res2)
print()
print("res3:")
print(res3)
print()
print("res4:")
print(res4)
print()
