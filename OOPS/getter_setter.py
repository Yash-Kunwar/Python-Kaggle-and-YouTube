class Employee:
    company = 'DOMS'
    salary = 1500
    salaryBonus = 500

    @property  # also called getter() method
    def totalSalary(self):
        return self.salary+self.salaryBonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val-self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 3000
print(e.salary)
print(e.salaryBonus)
