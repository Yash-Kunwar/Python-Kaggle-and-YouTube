class Employee:
    company = 'google'

    def showDetails(self):
        print('this is an employee class')


class Programer(Employee):
    language = 'Python'
    company = 'YouTube'

    def getLang(self):
        print(f'the language is {self.language}')

    def showDetails(self):
        print('this is a programer class')


e = Employee()
p = Programer()
e.showDetails()
p.showDetails()
print(p.company)
