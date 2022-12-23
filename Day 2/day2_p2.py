import os
input_file = os.path.join('input', 'input.txt')

shape_values = { 'R': 1, 'P': 2, 'S': 3}
round_key = {
    'AX': 'S', 'AY': 'R', 'AZ': 'P',
    'BX': 'R', 'BY': 'P', 'BZ': 'S',
    'CX': 'P', 'CY': 'S', 'CZ': 'R'
}
win_key = { "X": 0, "Y": 3, "Z": 6}

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
    win_val = win_key[round[1]]
    shape_val = shape_values[round_key[round[0] + round[1]]]
    total += (win_val + shape_val)
    #print(str(win_val))
    #print(str(shape_val))

print("Total: " + str(total))    
