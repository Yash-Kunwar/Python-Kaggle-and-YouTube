# find 'twinkle' from a file
f = open('another.txt')
t = f.read()
if 'twinkle' in t:
    print('twinkle is present', t.count('twinkle'), 'times')

print('****************************')


# update high-score
def game():
    return 80


score = game()
with open('high_score.txt') as f:
    hiscoreSTR = f.read()


if hiscoreSTR == "":
    with open('high_score.txt', 'w') as f:
        f.write(str(score))

elif int(hiscoreSTR) < score:
    with open('high_score.txt', 'w') as f:
        f.write(str(score))

print('****************************')

# table from 2 to 20 for 13 yr old
for i in range(2, 21):
    with open(f"tables/multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}")
            if j != 10:
                f.write('\n')

print('****************************')

# censor mf
words = ['donkey', 'retard']

with open('another.txt') as f:
    content = f.read()


for word in words:
    content = content.replace(word, '***')

with open('another.txt', 'w') as f:
    f.write(content)

print('****************************')

# find python in log fle and line no.
content = True
i = 1
with open('log.txt',) as f:
    while content:
        content = f.readline()

        if 'python' in content.lower():
            print(content)
            print(True)
            print(i)
        i += 1

print('****************************')

# copy of a file
with open('another.txt') as f:
    cont = f.read()
with open('copy_another.txt', 'w') as f:
    f.write(cont)

print('****************************')

# compare content of two files
file1 = 'another.txt'
file2 = 'copy_another.txt'

with open(file1) as f:
    f1 = f.read()
with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print(True)
else:
    print(False)

print('****************************')

# wipe out content of a file
with open('log.txt', 'w') as f:
    f.write("")

print('****************************')

# rename a file
import os

on = "log.txt"
nn = 'renamedUsingPyhton.txt'
with open(on) as f:
    content = f.read()

with open(nn, 'w') as f:
    f.write(content)

os.remove(on)
