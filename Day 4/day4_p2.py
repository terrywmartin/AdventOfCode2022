import os


input_file = os.path.join('input', 'input.txt')
items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

try:
    reader = open(input_file)
except:
    print('cannot open input file')
    exit(1)

elf_pairs = []


for line in reader:
    elf_pairs.append([line.strip('\n').split(',')[0],line.strip('\n').split(',')[1]])

print(elf_pairs)

total = 0
for elf_pair in elf_pairs:
    #print(elf_pair)
    range1 = elf_pair[0].split('-')
    range2 = elf_pair[1].split('-')
    #print(range1)
    #print(range2)
    # range 1 overlaps range 2
    if int(range2[0]) <= int(range1[0]) <= int(range2[1]):
        total += 1
        #print(range1)
        #print(range2)
    elif int(range1[0]) <= int(range2[0]) <= int(range1[1]):
        # range 2 overlaps range 1
        total += 1
        #print(range1)
        #print(range2)

    
print(total)
