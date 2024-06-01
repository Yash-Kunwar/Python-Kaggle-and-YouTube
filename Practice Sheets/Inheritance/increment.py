class Employee:
    salary = 1000
    increment = 1.5

    @property
    def afterIncrement(self):
        return self.salary*self.increment

    @afterIncrement.setter
    def afterIncrement(self, sai):
        self.increment = sai/self.salary


e = Employee()
print(e.afterIncrement)
print(e.increment)

e.afterIncrement = 2000
print(e.increment)
