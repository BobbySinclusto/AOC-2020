f = open('input.txt')

plane = []

for line in f:
    plane.append([c for c in line.strip()])

# During the 6 cycles, the grid can grow by at most 6 in all directions

grid = []

iterations = 6

for r in range(len(plane) + 2 * iterations):
    grid.append([])
    for c in range(len(plane[0]) + 2 * iterations):
        grid[r].append([])
        for d in range(1 + 2 * iterations): 
            if r >= iterations and r < iterations + len(plane) and c >= iterations and c < iterations + len(plane[0]) and d == iterations:
                grid[r][c].append(plane[r - iterations][c - iterations])
            else:
                grid[r][c].append('.')


def copy_vals(grid, updated):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for d in range(len(grid[0][0])):
                grid[r][c][d] = updated[r][c][d]

def count_adjacent(grid, rr, cc, dd):
    count = 0
    for r in range(-1, 2):
        for c in range(-1, 2):
            for d in range(-1, 2):
                if r != 0 or c != 0 or d != 0:
                    if 0 <= r + rr < len(grid) and 0 <= c + cc < len(grid[0]) and 0 <= d + dd < len(grid[0][0]):
                        if grid[r + rr][c + cc][d + dd] == '#':
                            count += 1
    return count

updated = [[[d for d in grid[r][c]] for c in range(len(grid[r]))] for r in range(len(grid))]

for i in range(iterations):
    # for debugging
    print('\n'.join([('   ').join([' '.join([grid[r][c][ii] for c in range(len(grid[0]))]) for ii in range(1 + 2 * iterations)]) for r in range(len(grid))]), '\n')
    #input()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for d in range(len(grid[0][0])):
                count = count_adjacent(grid, r, c, d)
                if grid[r][c][d] == '#':
                    if count != 2 and count != 3:
                        updated[r][c][d] = '.'
                else:
                    if count == 3:
                        updated[r][c][d] = '#'

    copy_vals(grid, updated)

# count final number of active cubes
count = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        for d in range(len(grid[0][0])):
            if grid[r][c][d] == '#':
                count += 1

print(count)
