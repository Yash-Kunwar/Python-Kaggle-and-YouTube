# list of fruits by user
a = input("enter fruit 1 name: ")
b = input("enter fruit 2 name: ")
c = input("enter fruit 3 name: ")
d = input("enter fruit 4 name: ")
e = input("enter fruit 5 name: ")
e = input("enter fruit 6 name: ")
f = input("enter fruit 7 name: ")
fruits = [a, b, c, d, e, f]
print(fruits)

print('****************************')

# students score
num1 = int(input("enter marks of student 1: "))
num2 = int(input("enter marks of student 2: "))
num3 = int(input("enter marks of student 3: "))
num4 = int(input("enter marks of student 4: "))
num5 = int(input("enter marks of student 5: "))
score = [num1, num2, num3, num4, num5]
score.sort()
print(score)

print('****************************')

# sum a list of 4 no.s
a = [1, 2, 3, 4]
print(a[0]+a[1]+a[2]+a[3])
print(sum(a))

print('****************************')

# count 0s in tuple
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
