import os
input_file = os.path.join('input', 'input.txt')


try:
    reader = open(input_file)
except:
    print('cannot open input file')
    exit(1)

elves = []

for line in reader:
    elves.append(line.strip('\n'))

sum = 0
max_value = -1
elf_count = 1
most_caloric_elf = 1
for elf in elves:
    if elf == '':
        if sum > max_value:
            max_value = sum
            most_caloric_elf = elf_count
        sum = 0
        elf_count += 1
    else:
        sum += int(elf)


print("Largest calorie count is: " + str(max_value) + ", carried by elf number " + str(most_caloric_elf))

