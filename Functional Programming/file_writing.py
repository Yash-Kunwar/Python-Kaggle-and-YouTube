f=open('sample.txt','a')
f.write("\n4. repetion, repetion, repetion = self confidence")
f=open('sample.txt')
data=f.read()
print(data)
f.close()


# with statement - no need to write f.close() statement 
with open('another.txt', 'r') as f:
    a = f.read()
print(a)
with open('another.txt', 'w') as f:
    a = f.write('hello there!')
