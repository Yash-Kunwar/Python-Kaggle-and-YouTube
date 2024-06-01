# class of programmers working in Microsoft
class Programmer:
    company = 'Microsoft'

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {
              self.name} and the product is {self.product}")


emp1 = Programmer('yash', 'skype')  # object
emp2 = Programmer('aish', 'VS Code')  # object
emp1.getInfo()
emp2.getInfo()