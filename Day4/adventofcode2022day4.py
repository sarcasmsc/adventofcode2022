import re
#open text file
text_file = open('inputday4.txt')
file_content = text_file.read()
#put into a list
li = list(file_content.split("\n"))
#create variables to store data
li2 = []
a = 0
ab = 0
li3 = []
total = 0
numbers1 = []
numbers2 = []
#create list with values
for x in li:
    li2.append(x)

#find all numbers
for x in li2:
    if a < len(li2):
        y = li2[a]
        numbers = re.findall('\d+', y)
        numbers1.append(numbers)
        a += 1

#reset a and turn into ints
a = 0
for x in numbers1:
    a = numbers1[ab]
    ab += 1
    f = [int(x) for x in a]
    numbers2.append(f)

#create counter and check if numbers are within eachothers range
counter = 0
for x in numbers2:
    if counter < 1000:
        firstnum = numbers2[counter][0]
        secondnum = numbers2[counter][1]
        thirdnum = numbers2[counter][2]
        fourthnum = numbers2[counter][3]
        counter += 1
        if firstnum >= thirdnum and secondnum <= fourthnum: #checking if first set is fully inside second set
            total += 1
        elif firstnum <= thirdnum and secondnum >= fourthnum: #checking if second set is fully inside first set
            total += 1
        else:
            pass
    else:
        print('part 1 total')
        print(total)

# part 2
counter = 0
totalpart2 = 0
for x in numbers2:
    if counter < 1000:
        firstnum = numbers2[counter][0]
        secondnum = numbers2[counter][1]
        thirdnum = numbers2[counter][2]
        fourthnum = numbers2[counter][3]
        counter += 1
        if firstnum >= thirdnum and secondnum <= fourthnum:
            totalpart2 += 1
        elif firstnum <= thirdnum and secondnum >= fourthnum:
            totalpart2 += 1
        elif firstnum <= thirdnum <= secondnum:#check if third number is inside first set
            totalpart2 += 1
        elif firstnum <= fourthnum <= secondnum:#check if fourth number is inside first set
            totalpart2 += 1
        else:
            pass
    else:
        print('part 2 total')
        print(totalpart2)