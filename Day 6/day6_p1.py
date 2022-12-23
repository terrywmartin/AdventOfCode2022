import os


input_file = os.path.join('input', 'input.txt')

try:
    reader = open(input_file)
except:
    print('cannot open input file')
    exit(1)

input_string = ""

for line in reader:
    input_string = line.strip('\n')

print(input_string)

marker = ""
index = -1
repeated = False
for i in range(0, len(input_string)):
    if len(marker) < 14:
        marker += input_string[i]
        if len(set(marker)) != len(marker):
            repeated = True
        #print(marker)
    else:
        #print(input_string[i])
        marker = marker[1:]
        marker += input_string[i]
        if len(set(marker)) == len(marker):
            print(marker)
            index = i + 1
            break
        
print(index)