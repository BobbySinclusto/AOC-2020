f = open('input.txt', 'r')

row = 0

counts = [0, 0, 0, 0, 0]
locs = [0, 0, 0, 0, 0]

for line in f.readlines():
    length = len(line.strip())
    
    for i in range(4):
        if line[locs[i]] == '#':
            counts[i] += 1

    locs[0] = (locs[0] + 1) % length
    locs[1] = (locs[1] + 3) % length
    locs[2] = (locs[2] + 5) % length
    locs[3] = (locs[3] + 7) % length
    
    if row % 2 == 0:
        if line[locs[4]] == '#':
            counts[4] += 1
        locs[4] = (locs[4] + 1) % length

    row += 1

print(counts)

result = 1
for n in counts:
    result *= n

print(result)
