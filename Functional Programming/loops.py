# while loop
i = 0
while i <= 0:
    print(str(i))
    i = i+1

# print content of list using loops
fruits = ['mango', 'apple', 'banana', 'watermelon', 'grapes']
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i+1


# for loop
fruits = ['mango', 'apple', 'banana', 'watermelon', 'grapes']
for item in fruits:
    print(item)

# range() in for loop
for i in range(1, 51, 2):
    print(i)

# for loop with else
for i in range(10):
    print(i)
else:
    print('yo yo')

# break statement
for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print('yo yo')


# continue statment
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)


# pass
i = 4
if i > 0:
    pass  # pass means do nothin'. it is NULL statement

while i > 6:
    pass
print('balle balle shava shava')
loo
