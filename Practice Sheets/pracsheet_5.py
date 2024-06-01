# english to हिंदी translator
translateDict = {
    "why": "क्यों(kyon?)",
    "where": "कहाँ(kahan?)",
    "how": "कैसे(kaise?)",
    "here": "यहाँ(yaha?)",
    "ok": "ठीक है(theek hai.)",
    "thank you": "धन्यवाद(dhanyavaad.)",
    "sorry": "क्षमा मांगना(kshama maangna.)"
}
print(translateDict)
t = input("enter a word in english: ")
print(translateDict.get(t))

print('****************************')

# display 8 unique nos. entered by the user
n1 = int(input("enter a no.: "))
n2 = int(input("enter a no.: "))
n3 = int(input("enter a no.: "))
n4 = int(input("enter a no.: "))
n5 = int(input("enter a no.: "))
n6 = int(input("enter a no.: "))
n7 = int(input("enter a no.: "))
n8 = int(input("enter a no.: "))
num = set()
num.add(n1)
num.add(n2)
num.add(n3)
num.add(n4)
num.add(n5)
num.add(n6)
num.add(n7)
num.add(n8)
print(num)

print('****************************')

# set with int 18 and str 18
check = {18, "18"}
print(check)
print('hence proofed that integer 18 and string 18 are possible 2gether in a set')

print('****************************')

# length of the set after given updation
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

print('****************************')

# type of given data
s = {}
print(type(s))

print('****************************')

# dict of friends and lang.
langDict = {}
newlangDict = {
    "mallu": "malayalam",
    "korusuke": "hindi",
    "toshi": "english",
    "orpheus": "german",
    "orpheus": "french",
    "ishat": "hindi"
}
langDict.update(newlangDict)
print(langDict)
