import time
from datetime import date
today = date.today()
today
print("\n today:")
print(today)
today == date.fromtimestamp(time.time())

my_birthday = date(today.year, 6, 24)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
my_birthday
print("\n my_birthday:")
print(my_birthday)
time_to_birthday = abs(my_birthday - today)
time_to_birthday.days
print("\n time_to_birthday:")
print(time_to_birthday)
