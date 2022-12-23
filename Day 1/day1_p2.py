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

caloric_sum = 0
max_value = -1
top_elves = []
for item in elves:
    if item == '':
        print("sum: " + str(caloric_sum))
        print(top_elves)
        if len(top_elves) < 3:
            top_elves.append(caloric_sum)
            top_elves.sort(reverse=True)
        else:
            if top_elves[0] < caloric_sum:
                top_elves.insert(0,caloric_sum)
                top_elves.pop()
            elif top_elves[1] < caloric_sum:
                top_elves.insert(1,caloric_sum)
                top_elves.pop()
            elif top_elves[2] < caloric_sum:
                top_elves.insert(2,caloric_sum)
                top_elves.pop()
        caloric_sum = 0
    else:
        caloric_sum += int(item)

print(top_elves)
print("Sum of the top three elves: " + str(sum(top_elves)))

