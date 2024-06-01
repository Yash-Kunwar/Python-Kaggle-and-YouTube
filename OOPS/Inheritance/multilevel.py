class Person:  # grand father
    country = 'india'

    def takeBreath(self):
        print('i am breathing')


class Employe(Person):  # father
    company = 'Niantic'

    def getSalary(self):
        print(f'salary is {self.salary}')

    def takeBreath(self):
        print('I am an employee so i am breathing')


class Programmer(Employe):  # son
    company = 'David N David'

    def getSalary(self):
        print(f'no salary for programmers')

    def takeBreath(self):
        print('I am a Programmer so i am breathing ++')


p = Person()
p.takeBreath()
# print(p.company) throws an error

e = Employe()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)
