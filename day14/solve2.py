import re
import copy

def write_mem(mem, mask, val, addr):
    addresses = []

    current_addr = ['0' for i in range(36)]

    addr_bin_str = bin(addr)[2:]

    for i in range(len(current_addr) - len(addr_bin_str), len(current_addr)):
        current_addr[i] = addr_bin_str[i - len(current_addr) + len(addr_bin_str)]

    indices = []

    for i in range(len(mask)):
        if mask[i] != '0':
            if mask[i] == '1':
                current_addr[i] = '1'
            elif mask[i] == 'X':
                current_addr[i] = 'X'
                indices.append(i)

    addresses.append(current_addr)

    for i in indices:
        for j in range(len(addresses)):
            addresses[j][i] = '0'
            add1 = copy.deepcopy(addresses[j])
            add1[i] = '1'

            addresses.append(add1)

    for addr in addresses:
        mem[int(''.join(addr), 2)] = val


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

