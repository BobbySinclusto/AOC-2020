import re

def write_mem(mem, mask, val, addr):
    result = [0 for i in range(36)]

    val_bin_str = bin(val)[2:]

    for i in range(len(result) - len(val_bin_str), len(result)):
        result[i] = val_bin_str[i - len(result) + len(val_bin_str)]

    for i in range(len(mask)):
        if mask[i] != 'X':
            result[i] = mask[i]

    value = int(''.join([str(n) for n in result]), 2)

    mem[addr] = value

f = open('input.txt')


mem = {}

expr = re.compile(r'mem\[(\d*)\] = (\d*)')

for line in f:
    if line[:3] != 'mem':
        mask = [c for c in line.strip().split(' = ')[1]]
    else:
        addr, val = expr.search(line).groups()

        write_mem(mem, mask, int(val), int(addr))

print(mem)

res = 0

for addr in mem:
    res += mem[addr]

print(res)

