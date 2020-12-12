import math

f = open('input.txt')

dirs = [[line[0], int(line.strip()[1:])] for line in f]

east_coord = 10
north_coord = 1

ship_n = 0
ship_e = 0

for thing in dirs:
    if thing[0] == 'F':
        ship_e += east_coord * thing[1]
        ship_n += north_coord * thing[1]

    elif thing[0] == 'L':
        for i in range(thing[1] // 90):
            tmp = east_coord
            east_coord = -north_coord
            north_coord = tmp

    elif thing[0] == 'R':
        for i in range(thing[1] // 90):
            tmp = east_coord
            east_coord = north_coord
            north_coord = -tmp

    elif thing[0] == 'N':
        north_coord += thing[1]
    elif thing[0] == 'S':
        north_coord -= thing[1]
    elif thing[0] == 'E':
        east_coord += thing[1]
    elif thing[0] == 'W':
        east_coord -= thing[1]

    print(ship_e, ship_n)

print(abs(ship_e) + abs(ship_n))

