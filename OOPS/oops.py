class Number:
    def sum(self):
        return self.a + self.b


num = Number()
num.a = 12
num.b = 34
s = num.sum()
print(s)


class RailwayForm:
    formType = 'RailwayForm'

    def printData(self):
        print(f'Name is {self.name}')
        print(f'train is {self.train}')


yashApplication = RailwayForm()
yashApplication.name = 'Yash'
yashApplication.train = 'Taj'
yashApplication.printData()

# instance class attrinbute


class Employee:
    company = 'Google'
    salary = 100


yash = Employee()
aish = Employee()

yash.salary = 500
# aish.salary = 800

print(yash.company)
print(aish.company)

print(yash.salary)
print(aish.salary)
# print(aish.address) # throws an error as address is not present in class
