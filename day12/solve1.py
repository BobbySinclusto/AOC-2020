import math

f = open('input.txt')

dirs = [[line[0], int(line.strip()[1:])] for line in f]

current_heading = 0
east_coord = 0
north_coord = 0

for thing in dirs:
    if thing[0] == 'F':
        east_coord += math.cos(math.pi * current_heading / 180) * thing[1]
        north_coord += math.sin(math.pi * current_heading / 180) * thing[1]
    elif thing[0] == 'L':
        current_heading += thing[1]
    elif thing[0] == 'R':
        current_heading -= thing[1]
    elif thing[0] == 'N':
        north_coord += thing[1]
    elif thing[0] == 'S':
        north_coord -= thing[1]
    elif thing[0] == 'E':
        east_coord += thing[1]
    elif thing[0] == 'W':
        east_coord -= thing[1]

print(abs(east_coord) + abs(north_coord))

