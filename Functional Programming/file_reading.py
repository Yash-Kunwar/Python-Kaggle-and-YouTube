# use open function to read the content of the file

# f = open('sample.txt', 'r')
f = open('sample.txt')  # default mode is r
data = f.read(10)  # read first 10 charecters
# data = f.read()
print(data)
f.close()


# using readline function
f = open('sample.txt')

data = f.readline()  # read first line
print(data, end="")

data = f.readline()  # read second line
print(data, end="")

data = f.readline()  # read third line
print(data, end="")
# and so on...
