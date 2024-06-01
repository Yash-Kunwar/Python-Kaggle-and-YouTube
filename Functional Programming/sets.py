a = {1, 3, 4, 5, 3}
b = {}

print(a)
print(b)
print(type(a))
print(type(b))

c = set()

c.add(7)
c.add(9)
c.add(9)
c.add(9)  # adding a value repetitively does not change a set
c.add(8)

# can add tuple in set b/c it is not hashable/mutable but not with other
c.add((1, 2, 3))
print(c)
print(len(c))

# removal of an item
c.remove(7)
print(c)

# popping an item
print(c.pop())
