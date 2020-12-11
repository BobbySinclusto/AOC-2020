import copy
from time import perf_counter

f = open('input.txt')

grid = [[char for char in line.strip()] for line in f.readlines()]

changed = True

iteration = 0

start = perf_counter()
while changed:
    updates = copy.deepcopy(grid)
    changed = False
    for r in range(len(grid)):
        for c in range(len(grid[0])):

            row_vec = [-1, 0, 1, -1, 1, -1, 0, 1]
            col_vec = [-1, -1, -1, 0, 0, 1, 1, 1]

            count = 0
            radius = 1
            while len(row_vec) > 0 and radius < max(len(grid), len(grid[0])):
                i = 0
                while i < len(row_vec):
                    if 0 <= r+row_vec[i]*radius < len(grid) and 0 <= c+col_vec[i]*radius < len(grid[0]):
                        if (row_vec[i] != 0 or col_vec[i] != 0) and grid[r][c] != '.':
                            if grid[r+row_vec[i]*radius][c+col_vec[i]*radius] == '#':
                                count += 1
                                row_vec.pop(i)
                                col_vec.pop(i)
                                i -= 1
                            elif grid[r+row_vec[i]*radius][c+col_vec[i]*radius] == 'L': 
                                row_vec.pop(i)
                                col_vec.pop(i)
                                i -= 1
                    i += 1
                radius += 1
                
            if count >= 5 and grid[r][c] == '#':
                changed = True
                updates[r][c] = 'L'
            elif count == 0 and grid[r][c] == 'L':
                changed = True
                updates[r][c] = '#'

    grid = updates

    iteration += 1
    print(iteration)
    '''
    print('\n'.join(' '.join(line) for line in grid))
    input()
    '''

end = perf_counter()

print(end - start)
res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            res += 1
print(res)
