f = open('input.txt')

ids = []

#for line in ['FBFBBFFRLR']:
for line in f.readlines():
    upper = 127
    lower = 0
    for i in range(7):
        if line[i] == 'F':
            upper = (upper-lower) // 2 + lower
        else:
            lower = (upper-lower + 1) // 2 + lower

    row = lower
    
    upper = 8
    lower = 0

    for i in range(7, len(line.strip())):
        if line[i] == 'L':
            upper = (upper-lower) // 2 + lower
        else:
            lower = (upper-lower + 1) // 2 + lower

    col = lower

    seat_id = row * 8 + col

    ids.append(seat_id)

ids = sorted(ids)

for i in range(len(ids)-1):
    if ids[i] == ids[i+1] - 2:
        print(ids[i], ids[i+1])

print(max(ids))
