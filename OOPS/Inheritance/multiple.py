class Employee:
    company = 'visa'
    eCode = 120


class Freelancer:
    company = 'fiverr'
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1


class Progrmmer(Employee, Freelancer):
    name = 'rohit'


p = Progrmmer()
p.upgradeLevel()
print(p.company)  # priority given to the first class defined in the child class
