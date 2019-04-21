data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print("data.find('@')", atpos)
sppos = data.find(' ', atpos)
print("data.find(' ',atpos)", sppos)
host = data[atpos + 1:sppos]
print("data[atpos+1:sppos]", host)
