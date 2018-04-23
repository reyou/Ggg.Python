from datetime import date
d = date.fromordinal(730920)  # 730920th day after 1. 1. 0001
d

t = d.timetuple()
for i in t:
    print("www:", i)


ic = d.isocalendar()
for i in ic:
    print("qqq:", i)


d.isoformat()
print("\n d.isoformat():")
print(d.isoformat())
d.strftime("%d/%m/%y")
print("\n strftime %d/%m/%y:")
print(d.strftime("%d/%m/%y"))
d.strftime("%A %d. %B %Y")
print("\n strftime %A %d. %B %Y:")
print(d.strftime("%A %d. %B %Y"))
'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
