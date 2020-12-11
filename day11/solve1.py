import copy

f = open('input.txt')

grid = [[char for char in line.strip()] for line in f.readlines()]

changed = True

while changed:
    updates = copy.deepcopy(grid)
    changed = False
    for r in range(len(grid)):
        for c in range(len(grid[0])):

            row_vec = [-1, 0, 1, -1, 1, -1, 0, 1]
            col_vec = [-1, -1, -1, 0, 0, 1, 1, 1]

            count = 0
            for i in range(len(row_vec)):
                if 0 <= r+row_vec[i] < len(grid) and 0 <= c+col_vec[i] < len(grid[0]):
                    if grid[r][c] != '.' and grid[r+row_vec[i]][c+col_vec[i]] == '#':
                        count += 1
            
            if count >= 4 and grid[r][c] == '#':
                changed = True
                updates[r][c] = 'L'
            elif count == 0 and grid[r][c] == 'L':
                changed = True
                updates[r][c] = '#'

    grid = updates
    print('iter')

    '''
    print('\n'.join(' '.join(line) for line in grid))
    input()
    '''

res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            res += 1
print(res)
