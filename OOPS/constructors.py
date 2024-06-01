class Employee:
    company = 'Google'

    def __init__(self, name, salary, subunit):
        print('Employee class is created')
        self.name = name
        self.salary = salary
        self.subunit = subunit

    def getDetails(self):
        print(f"the name is {self.name}, salary is {
            self.salary}, subunit is {self.subunit}")

    def getSalary(self, signature):
        print(f"salary is {self.salary} for working in {
            self.company}.\n{signature}")

    @staticmethod
    def greet():
        print("good morning, sir")

    @staticmethod
    def currenTime():
        print('the time is 1am')


yash = Employee('yash', 500, 'niantic')
# yash=Employee() --> this throws an error: missing 3 required positiona  arguments: 'name', 'salary', and 'subunit
yash.getDetails()
