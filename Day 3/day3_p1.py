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
for sack in rucksacks:
    sack1 = sack[:len(sack)//2]
    sack2 = sack[len(sack)//2:]
    #print(sack1)
    #print(sack2)

    for char in sack1:
        if sack2.find(char) != -1:
            print(char)
            total += (items.index(char) + 1)
            break
    

print(total)
