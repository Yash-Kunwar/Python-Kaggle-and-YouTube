a = "a"
# a='''a'''
# a='a'
b = 44
c = 123.321
d = True
n = None

# Printing the variables
print(a)
print(b)
print(c)
print(d)
print(n)

# printing the type of variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(n))

# Assignment Operators
a = 34
a += 10  # add to original number
a -= 12  # subtract from original number
a *= 12  # multiply to original number
a /= 12  # divide from original number
print(a)

# Logical Operators
bool1 = True
bool2 = False
print("the value of bool 1 and bool2 is", (bool1 and bool2))
print("the value of bool 1 or bool2 is", (bool1 or bool2))
print("the value of bool 1 not bool2 is", (not bool2))

# Type Casting
a="7"
a=int(a)
print(a+a)

# Taking input from user using input()
a= input("enter ur no.: ")
a=int(a) #convert a to integer
print(type(a))
