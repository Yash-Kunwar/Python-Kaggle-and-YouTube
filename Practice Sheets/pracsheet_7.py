# multiplication table
num = int(input("enter a no.: "))
for i in range(1, 11):
    print(num, 'X', i, '=', num*i)
print(f"{num} X {i} = {num*i}")  # fstrings

print('****************************')


# greet people whose name starts with
l = ['harry', 'soham', 'sachin', 'rahul']
for name in l:
    if name.startswith('s'):
        print("greetings,", name)
    # else:
    #     print('go 2 hell,', name)

print('****************************')

# multipliation table using while
numm = int(input("enter a no.: "))
i = 0
while i < 10:
    i = i+1
    print(f"{numm} X {i} = {numm*i}")

print('****************************')

# prime or not
no = int(input("enter a no.: "))
prime = True
for i in range(2, no):
    if (no % i == 0):
        prime = False
        break
if prime:
    print('prime')
else:
    print("not prime")

print('****************************')

# sum of first 'n' natural no.s.
natnum = int(input("enter a no.: "))
sum = 0
for i in range(1, natnum+1):
    sum += i
print(f"sum of first {natnum} natural no.s is {sum}")

print('****************************')

# factorial of a given no.
factNum = int(input("enter a no. "))
factorial = 1
for i in range(1, factNum+1):
    factorial = factorial*i
print('factorial of', factNum, 'is', factorial)

print('****************************')

# print pattern - 1 [VERY IMPORTANT]
n = 3
for i in range(3):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))

print('****************************')

# print pattern - 2
i = 4
for i in range(4):
    print("*"*(i+1))

print('****************************')

# print pattern - 3 [VERY IMPORTANT]
n = 3
for i in range(n):
    if i == 0 or i == n - 1:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")

print('****************************')

# multiplication table in reverse order
rNum = int(input("enter a no.: "))
for i in range(10, 0, -1):
    print(f"{rNum} X {i} = {rNum*i}")  # fstrings
