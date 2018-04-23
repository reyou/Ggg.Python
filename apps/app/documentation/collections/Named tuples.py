# Returns a new subclass of tuple with named fields.
from collections import namedtuple
EmployeeRecord = namedtuple(
    'EmployeeRecord', 'name, age, title, department, paygrade')
print(EmployeeRecord)
"""
map(func, *iterables) --> map object
Make an iterator that computes the function using arguments 
from each of the iterables. Stops when the shortest iterable is exhausted.
"""
import csv
# https://stackoverflow.com/questions/18682695/python-escape-character
# https://stackoverflow.com/questions/10043636/any-reason-not-to-use-to-concatenate-two-strings
# https://stackoverflow.com/questions/8515053/csv-error-iterator-should-return-strings-not-bytes
fileLocation = "".join(
    ["C:\\Github\\Ggg\\Ggg.Python\\apps\\app\\documentation\\collections\\", "employees.csv"])
print("\n fileLocation")
print(fileLocation)
for emp in map(EmployeeRecord._make, csv.reader(open(fileLocation, "r"))):
    print(emp.name, emp.title)

import sqlite3
# this creates file under execution root.
conn = sqlite3.connect('companydata.sqlite')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS employees')
cursor.execute(
    'CREATE TABLE employees (name TEXT, age TEXT, title TEXT, department TEXT, paygrade TEXT)')
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)
