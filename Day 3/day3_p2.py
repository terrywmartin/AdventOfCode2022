import os


input_file = os.path.join('input', 'input.txt')
items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

try:
    reader = open(input_file)
except:
    print('cannot open input file')
    exit(1)

rucksacks = []


for line in reader:
    rucksacks.append(line.strip('\n'))

total = 0
for i in range(0, len(rucksacks)):
    if (i+1) % 3 == 0:
        #print("Group")
        sack1 = rucksacks[i-2]
        sack2 = rucksacks[i-1]
        sack3 = rucksacks[i]
        #print(sack1)
        #print(sack2)
        #print(sack3)

        for char in sack1:
            if sack2.find(char) != -1 and sack3.find(char) != -1:
                print(char)
                total += (items.index(char) + 1)
                break

print(total)
