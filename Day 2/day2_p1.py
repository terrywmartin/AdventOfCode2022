import os
input_file = os.path.join('input', 'input.txt')

shape_values = { 'X': 1, 'Y': 2, 'Z': 3}
winning_key = {
    'AX': 3, 'AY': 6, 'AZ': 0,
    'BX': 0, 'BY': 3, 'BZ': 6,
    'CX': 6, 'CY': 0, 'CZ': 3
}

try:
    reader = open(input_file)
except:
    print('cannot open input file')
    exit(1)

strategy = []

for line in reader:
    strat = line.strip('\n').split(' ')
    strategy.append([strat[0], strat[1]])

total = 0

for round in strategy:
    #print(winning_key[round[0] + round[1]])
    #print(shape_values[round[1]])
    #print("Total: " + str(total))
    total += (shape_values[round[1]] + winning_key[round[0] + round[1]])
    #print(round)

print("Total: " + str(total))    
