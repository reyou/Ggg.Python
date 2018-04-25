from string import Template

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
# t.substitute(d)

s = t.safe_substitute(d)
print(s)





