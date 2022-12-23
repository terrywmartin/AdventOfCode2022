import os


input_file = os.path.join('input', 'input.txt')
crates = {
    1: ['D','L','V','T','M','H','F'],
    2: ['H','Q','G','J','C','T','N','P'],
    3: ['R','S','D','M','P','H'],
    4: ['L','B','V','F'],
    5: ['N','H','G','L','Q'],
    6: ['W','B','D','G','R','M','P'],
    7: ['G','M','N','R','C','H','L','Q'],
    8: ['C','L','W'],
    9: ['R','D','L','Q','J','Z','M','T']
}

try:
    reader = open(input_file)
except:
    print('cannot open input file')
    exit(1)

moves = []
from_val = []
dest_val = []


for line in reader:
    moves.append(int(line.strip('\n').split(' ')[1]))
    from_val.append(int(line.strip('\n').split(' ')[3]))
    dest_val.append(int(line.strip('\n').split(' ')[5]))


for i in range(0, len(moves)):
    print("move " + str(moves[i]) + " from " + str(from_val[i]) + " to " + str(dest_val[i]))
    for j in range(0, moves[i]):
        crates[dest_val[i]].append(crates[from_val[i]].pop())
    

top_vals = ''
for crate in crates:
    top_vals += crates[crate].pop()

print(top_vals)


