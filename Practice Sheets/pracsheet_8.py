# function to find the greatest of 3 numbers
def maximum(num1, num2, num3):
    if (num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    else:
        if (num2 > num3):
            return num2
        else:
            return num3


m = maximum(4, 8, 12)
print(m)

print('****************************')

# celsius to farheneit


def far(cel):
    return (cel*(9/5)) + 32


c = 32
print(far(c))

print('****************************')

# prevent print() to print new line @the end
print("hello ", end="")
print("how ", end="")
print("are ", end="")
print("you? ", end="")

print('****************************')


# recursive f() sum of first n natural numbers
def fact_recur(n):
    if n == 1 or n == 0:
        return 1
    return n+fact_recur(n-1)


print(fact_recur(10))

print('****************************')

# print pattern for n lines
n = 6
for i in range(n):
    print("x" * (n-i))

print('****************************')

# inches to centimeters(cm)


def convert(inch):
    return inch*2.54


len = 5.5
print(convert(len))

print('****************************')

# remove a word and strip(remove extra spaces) at the same time


def rem_n_str(string, word):
    newStr = string.replace(word, "     ")
    return newStr.strip()


this = "    gotta chatch'em all     "
print(rem_n_str(this, "all"))

print('****************************')

# f() to print multipliation table of any number


def table(n):
    for i in range(1, 11):
        m = print(f"{n} x {i} = {n*i}")
    return m


num = int(input("enter a no.: "))
table(num)
