import numpy as np

text_file = open('input.txt')
file_content = text_file.read()

li = list(file_content.split("\n"))
list2 = []
c = []
d = []
e = []
f = []
g2 = 0
ab = 0
h = []
for i in li:
    if i.isnumeric() == True:
        c.append(i)
    elif i.isnumeric() == False:
        d.append(c)
        c = []

for xd in d:
    a = d[ab]
    ab += 1
    f = [int(x) for x in a]
    h = sum(f)
    print(f)
    print(h)
    e.append(h)


print(f)
print(d)
print(e)
print(len(e))
print(max(e))