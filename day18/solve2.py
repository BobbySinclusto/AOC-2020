f = open('input.txt')

res = 0

for line in f.readlines():
    results = [0]
    operators = ['+']

    prev_loc = {0:0}
    depth = 0
    looking = {0:False}

    modded_line = []
    for c in line.strip('\n'):
        if c == '+':
            if looking[depth]:
                modded_line.append(')')
                looking[depth] = False
            modded_line.insert(prev_loc[depth], '(')
            looking[depth] = True
            modded_line.append(c)
        elif c == '*':
            if looking[depth]:
                modded_line.append(')')
                looking[depth] = False
                prev_loc[depth] = len(modded_line)
            elif not looking[depth]:
                prev_loc[depth] = len(modded_line) + 1
            modded_line.append(c)
        elif c == '(':
            depth += 1
            prev_loc[depth] = len(modded_line)
            looking[depth] = False
            modded_line.append(c)
        elif c == ')':
            depth -= 1
            if looking[depth]:
                modded_line.append(')')
                looking[depth] = False
            modded_line.append(c) 
        elif c != ' ' and looking[depth]:
            modded_line.append(c)
            modded_line.append(')')
            looking[depth] = False
        else:
            modded_line.append(c)

    print(''.join(modded_line))

    results = [0]
    operators = ['+']

    for c in modded_line:
        if c == '+':
            operators[-1] = '+'
        elif c == '*':
            operators[-1] = '*'
        elif c == '(':
            results.append(0)
            operators.append('+')
        elif c == ')':
            operators.pop()
            if operators[-1] == '+':
                results[-2] += results[-1]
            else:
                results[-2] *= results[-1]
            results.pop()
        elif c != ' ':
            if operators[-1] == '+':
                results[-1] += int(c)
            else:
                results[-1] *= int(c) 
    res += results[0]

print(res)
