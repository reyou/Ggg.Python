"""The locale module accesses a database of culture specific
data formats. The grouping attribute of locale’s format function
provides a direct way of formatting numbers with group
separators:"""
import locale

locale.setlocale(locale.LC_ALL, 'English_United States.1252')

# get a mapping of conventions
conv = locale.localeconv()
print(type(conv))
print('conv', conv)
x = 1234567.8
qqq = locale.format("%d", x, grouping=True)
print('qqq', qqq)

www = locale.format_string("%s%.*f", (conv['currency_symbol'],
                                      conv['frac_digits'], x), grouping=True)
print('www', www)
