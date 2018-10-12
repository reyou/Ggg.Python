class EmployeeRecord:
    def __init__(self, n, i, r):
        self.name = n;
        self.id = i;
        self.pay_rate = r;


er = EmployeeRecord(5, 4, 1)
print(er.name)
print(er.id)
print(er.pay_rate)
