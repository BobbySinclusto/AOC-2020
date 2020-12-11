f = open('input.txt')

accumulator = 0

lines = []

for line in f.readlines():

    stuff = line.strip().split(' ')

    instruction = stuff[0]
    try:
        val = int(stuff[1])
    except:
        val = 0

    lines.append([instruction, val])

for i in range(len(lines)):
    print('before', lines[i])
    j = True
    terminated = True

    if lines[i][0] == 'jmp':
        lines[i][0] = 'nop'
        j = False
    elif lines[i][0] == 'nop':
        lines[i][0] = 'jmp'
    else:
        continue

    accumulator = 0
    ip = 0
    visited = set()

    while ip < len(lines):
        instruction, val = lines[ip]

        if ip in visited:
            print('nope')
            terminated = False
            break
        visited.add(ip)

        if instruction == 'acc':
            accumulator += val
            ip += 1
        elif instruction == 'jmp':
            ip += val
        else:
            ip += 1

    if terminated:
        # yay we're done!
        if ip == len(lines):
            print('instruction to change: line', i, '\n', lines[i])
            print('accumulator:', accumulator)
            break
    
    lines[i][0] = 'nop' if j else 'jmp'
    print('after', lines[i])

print(accumulator)

