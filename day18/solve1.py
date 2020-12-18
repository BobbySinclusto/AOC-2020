f = open('input.txt')

res = 0

for line in f.readlines():
    results = [0]
    operators = ['+']

    for c in line.strip('\n'):
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
