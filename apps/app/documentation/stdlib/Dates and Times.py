# dates are easily constructed and formatted
from datetime import date

now = date.today()
print("now", now)

print("strftime", now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(2016, 8, 6)
age = now - birthday
print("age.days", age.days)
