class Person: # grand father
    def __init__(self):
        print('initialising person!\n   ')

    def takeBreath(self):
        print('i am breathing')

class Employe(Person): # father
    company='Niantic'

    def __init__(self):
        super().__init__()
        print('initialising employee!\n')

    def getSalary(self):
        print(f'salary is {self.salary}')

    def takeBreath(self):
        super().takeBreath()
        print('I am an employee so i am breathing')

class Programmer(Employe): # son
    company='David N David'

    def __init__(self):
        super().__init__()
        print('initialising progrmmer!\n')


    def getSalary(self):
        print(f'no salary for programmers')

    def takeBreath(self):
        super().takeBreath()
        print('I am a Programmer so i am breathing ++')

# p=Person()
# p.takeBreath()

# e=Employe()
# e.takeBreath()

pr=Programmer()
# pr.takeBreath()
