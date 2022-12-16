text_file = open('inputday2.txt')
file_content = text_file.read()

li = list(file_content.split("\n"))

total = 0

for i in li:
    if i == 'A X':
        total += 4
    elif i == 'A Y':
        total += 8
    elif i == 'A Z':
        total += 3
    elif i == 'B X':
        total += 1
    elif i == 'B Y':
        total += 5
    elif i == 'B Z':
        total += 9
    elif i == 'C X':
        total += 7
    elif i == 'C Y':
        total += 2
    elif i == 'C Z':
        total += 6

print(total)

#part 2
li = list(file_content.split("\n"))
total = 0

for i in li:
    if i == 'A X':
        total += 3
    elif i == 'A Y':
        total += 4
    elif i == 'A Z':
        total += 8
    elif i == 'B X':
        total += 1
    elif i == 'B Y':
        total += 5
    elif i == 'B Z':
        total += 9
    elif i == 'C X':
        total += 2
    elif i == 'C Y':
        total += 6
    elif i == 'C Z':
        total += 7

print(total)