class Employee:
    company = 'Google'

    def getSalary(self, signature):
        print(f"salary is {self.salary} for working in {
              self.company}.\n{signature}")

    @staticmethod
    def greet():
        print("good morning, sir")

    @staticmethod
    def currenTime():
        print('the time is 1am')


yash = Employee()
yash.salary = 100000
yash.greet()  # Employee.greet()
yash.currenTime()
yash.getSalary('Thanks')  # Employee.getSalary(yash)
