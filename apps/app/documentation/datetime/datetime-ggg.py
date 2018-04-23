from datetime import timedelta
year = timedelta(days=365)
print("\n year:")
print(year)
another_year = timedelta(weeks=40, days=84, hours=23,
                         minutes=50, seconds=600)  # adds up to 365 days
print("\n another_year:")
print(another_year)
year.total_seconds()
print("\n year.total_seconds:")
print(year.total_seconds())
year == another_year

ten_years = 10 * year
ten_years, ten_years.days // 365

nine_years = ten_years - year
nine_years, nine_years.days // 365

three_years = nine_years // 3
three_years, three_years.days // 365

res = abs(three_years - ten_years) == 2 * three_years + year
print("\n res:")
print(res)
