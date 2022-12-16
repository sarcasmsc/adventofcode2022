#part 1
#variable
a = 'caaacbbb'
#find length of variable
b = len(a)
#figuring out where to slice variables, a2 = slice first half, a3 = slice 2nd half
a2 = slice(0, b//2)
a3 = slice(b//2, b)
#assign variables to each half
c = a[a2]
c2 = a[a3]
#find the common characters between each half
commoncharacters = ''.join(set(c).intersection(c2))
#print the common characters
print(commoncharacters)
#get text from file
text_file = open('inputday3.txt')
file_content = text_file.read()
#create list
li = list(file_content.split("\n"))
li2 = []
#split the characters into a new list
for i in li:
    ilen = len(i)
    slice1 = slice(0, ilen//2)
    slice2 = slice(ilen//2, ilen)
    half1 = i[slice1]
    half2 = i[slice2]
    icommoncharacters = ''.join(set(half1).intersection(half2))
    li2.append(icommoncharacters)

#checking to see it split properly
print(li2)
#create total variable
total = 0
#add to total based on its value
for i in li2:
    if i == 'a':
        total += 1
    elif i == 'b':
        total += 2
    elif i == 'c':
        total += 3
    elif i == 'd':
        total += 4
    elif i == 'e':
        total += 5
    elif i == 'f':
        total += 6
    elif i == 'g':
        total += 7
    elif i == 'h':
        total += 8
    elif i == 'i':
        total += 9
    elif i == 'j':
        total += 10
    elif i == 'k':
        total += 11
    elif i == 'l':
        total += 12
    elif i == 'm':
        total += 13
    elif i == 'n':
        total += 14
    elif i == 'o':
        total += 15
    elif i == 'p':
        total += 16
    elif i == 'q':
        total += 17
    elif i == 'r':
        total += 18
    elif i == 's':
        total += 19
    elif i == 't':
        total += 20
    elif i == 'u':
        total += 21
    elif i == 'v':
        total += 22
    elif i == 'w':
        total += 23
    elif i == 'x':
        total += 24
    elif i == 'y':
        total += 25
    elif i == 'z':
        total += 26
    elif i == 'A':
        total += 27
    elif i == 'B':
        total += 28
    elif i == 'C':
        total += 29
    elif i == 'D':
        total += 30
    elif i == 'E':
        total += 31
    elif i == 'F':
        total += 32
    elif i == 'G':
        total += 33
    elif i == 'H':
        total += 34
    elif i == 'I':
        total += 35
    elif i == 'J':
        total += 36
    elif i == 'K':
        total += 37
    elif i == 'L':
        total += 38
    elif i == 'M':
        total += 39
    elif i == 'N':
        total += 40
    elif i == 'O':
        total += 41
    elif i == 'P':
        total += 42
    elif i == 'Q':
        total += 43
    elif i == 'R':
        total += 44
    elif i == 'S':
        total += 45
    elif i == 'T':
        total += 46
    elif i == 'U':
        total += 47
    elif i == 'V':
        total += 48
    elif i == 'W':
        total += 49
    elif i == 'X':
        total += 50
    elif i == 'Y':
        total += 51
    elif i == 'Z':
        total += 52

#print total
print(total)

#part 2
#reset variables
li = list(file_content.split("\n"))
li2 = []
li3 = []
li4 = []
x = 0
#split into 3 groups
for i in li:
    if x < len(li):
        li2.append(li[x])
        x += 1
        if x < len(li):
            li3.append(li[x])
            x += 1
            if x < len(li):
                li4.append(li[x])
                x += 1
            else:
                break
        else:
            break
    else:
        print('done')
#reset and create new variables
x = 0
y = 0
li5 = []
#find common letter between 3 lists (for some reason li2 has 1 extra empty string, so i just used the len(li3) instead of li2
for i in li2:
    if y < len(li3):
        icommoncharacters1 = ''.join(set(li2[y]).intersection(li3[y]))
        icommoncharacters2 = ''.join(set(li3[y]).intersection(li4[y]))
        icommoncharacters3 = ''.join(set(icommoncharacters1).intersection(icommoncharacters2))
        li5.append(icommoncharacters3)
        y += 1
    else:
        print('done')
#reset total
total = 0
#add to total based on its value
for i in li5:
    if i == 'a':
        total += 1
    elif i == 'b':
        total += 2
    elif i == 'c':
        total += 3
    elif i == 'd':
        total += 4
    elif i == 'e':
        total += 5
    elif i == 'f':
        total += 6
    elif i == 'g':
        total += 7
    elif i == 'h':
        total += 8
    elif i == 'i':
        total += 9
    elif i == 'j':
        total += 10
    elif i == 'k':
        total += 11
    elif i == 'l':
        total += 12
    elif i == 'm':
        total += 13
    elif i == 'n':
        total += 14
    elif i == 'o':
        total += 15
    elif i == 'p':
        total += 16
    elif i == 'q':
        total += 17
    elif i == 'r':
        total += 18
    elif i == 's':
        total += 19
    elif i == 't':
        total += 20
    elif i == 'u':
        total += 21
    elif i == 'v':
        total += 22
    elif i == 'w':
        total += 23
    elif i == 'x':
        total += 24
    elif i == 'y':
        total += 25
    elif i == 'z':
        total += 26
    elif i == 'A':
        total += 27
    elif i == 'B':
        total += 28
    elif i == 'C':
        total += 29
    elif i == 'D':
        total += 30
    elif i == 'E':
        total += 31
    elif i == 'F':
        total += 32
    elif i == 'G':
        total += 33
    elif i == 'H':
        total += 34
    elif i == 'I':
        total += 35
    elif i == 'J':
        total += 36
    elif i == 'K':
        total += 37
    elif i == 'L':
        total += 38
    elif i == 'M':
        total += 39
    elif i == 'N':
        total += 40
    elif i == 'O':
        total += 41
    elif i == 'P':
        total += 42
    elif i == 'Q':
        total += 43
    elif i == 'R':
        total += 44
    elif i == 'S':
        total += 45
    elif i == 'T':
        total += 46
    elif i == 'U':
        total += 47
    elif i == 'V':
        total += 48
    elif i == 'W':
        total += 49
    elif i == 'X':
        total += 50
    elif i == 'Y':
        total += 51
    elif i == 'Z':
        total += 52
#print total
print(total)