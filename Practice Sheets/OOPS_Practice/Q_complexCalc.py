class Calculator:

    @staticmethod
    def greet():
        print('hello there!')

    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"the square of {self.num} is {self.num ** 2} ")

    def squareRoot(self):
        print(f"the square root of {self.num} is {self.num ** 0.5} ")

    def cube(self):
        print(f"the cube of {self.num} is {self.num ** 3} ")


a = Calculator(int(input("enter a number: ")))
a.greet()
a.square()
a.cube()
a.squareRoot()
