class Sample:
    a = 'yash'


obj1 = Sample()
obj1.a = 'harsh'
Sample.a = 'harsh'

print(Sample.a)
print(obj1.a)
