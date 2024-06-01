def percent(marks):
    return (sum(marks)/400)*100


marks1 = [45, 78, 86, 97]
percentage = percent(marks1)

marks2 = [46, 70, 80, 33]
percentage2 = percent(marks2)

print(percentage, percentage2)


# greeting function
def greet(name):
    print("G'day", name)


def msum(n1, n2):
    q = n1+n2
    return print(q)


greet('yash')
s = msum(12, 40)


# default argument value
def greet(name='stranger'):
    print("G'day", name)


greet('yash')
greet()
