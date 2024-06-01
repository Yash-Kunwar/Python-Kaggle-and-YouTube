class Employee:
    company = 'dell'
    salary = 1000
    location = 'delhi'

    # def changeSalary(self,sal):
    #     self.__class__. salary=sal #__<methods>__ are called dunder methods

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal


e = Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)
print(Employee.salary)
