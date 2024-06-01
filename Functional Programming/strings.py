b = "yash"
print(b)
print(type(b))
greetings = "gu'mornin, "
c = greetings+b # concatenating to strings
print(c)
name = "YashDidIt"
print(name[3])
print(name[-4:-1])
print(len(name))
d=name[1::3]
print(d)

story = '''in order to compare the effect of omissions with situations where the behaviour was performed consistently, we
identified all the occasions when the behaviour was performed for three consecutive days and automaticity scores 
were available for the first and third days'''

# string functions
print(len(story))
print(story.endswith('days'))
print(story.count("the"))
print(story.capitalize())
print(story.find("and"))# first occurance
print(story.replace("and","AND"))
print(story.strip()) # removes extra spaces
