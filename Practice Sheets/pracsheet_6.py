# greates of four numbers
num1 = int(input("enter no. 1: "))
num2 = int(input("enter no. 2: "))
num3 = int(input("enter no. 3: "))
num4 = int(input("enter no. 4: "))
if num1 > num4:
    f1 = num1
else:
    f1 = num4

if num2 > num3:
    f2 = num2
else:
    f2 = num3

if f1>f2:
    print(f1, "is greatest")
else:
    print(f2, "is greatest")

print('****************************')

# pass or fail
sub1=int(input("enter marks in maths: "))
sub2=int(input("enter marks in physics: "))
sub3=int(input("enter marks in chemistry: "))
perSub1=(sub1/50)*100
perSub2=(sub2/50)*100
perSub3=(sub3/50)*100
if (perSub1<33 or perSub2<33 or perSub3<33):
    print("u FAILED B/C TOTAL % LESS THAN 33")
elif (perSub1+perSub2+perSub3)/3<40:
    print("u FAILED B/C TOTAL % LESS THAN 40")
else:
    print("congratulation! <3, u PASSED")

print('****************************')

# spam mail detection
mail = input("enter your mail: ")
spam = False
if "make a lot of money" in mail:
    spam = True
elif "buy now" in mail:
    spam = True
elif "subscribe this" in mail:
    spam = True
elif "click this" in mail:
    spam = True
else:
    spam

if spam == True:
    print("the mail is spam")
else:
    print("the mail is not spam")

print('****************************')

# lenth of username is less than 10
name=input("enter your username: ")
if len(name)>10:
    print('username must contain onle 10 charecters')
else:
    print('username regitered successfuly')

print('****************************')

# find in text
comment=input("enter yout text: ")
find=input("what do you want to find: ")

if find in comment:
    print(comment.count(find), find, "found!")
else:
    print(find,"not found")

print('****************************')

# fan(si) or not
marks = int(input('enter the marks: '))
if marks>90 and marks<100:
    print("EX")
elif marks>80 and marks<90:
    print('A')
elif marks>70 and marks<80:
    print('B')
elif marks>60 and marks<70:
    print('C')
elif marks>50 and marks<60:
    print('D')
elif marks<50:
    print('F')

print('****************************')

# yash in post or not
post=input('Enter ur post: ')
if "yash" in post:
    print(True)
else:
    print(False)
