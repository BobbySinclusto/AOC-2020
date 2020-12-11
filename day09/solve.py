from collections import deque

f = open('input.txt')

nums = list(int(line.strip()) for line in f.readlines())

current_25 = deque(nums[:25])

for i in range(25, len(nums)):
    valid = False
    for j in current_25:
        for k in current_25:
            if j != k and j + k == nums[i]:
                valid = True
                break
        if valid:
            break

    if not valid:
        print(nums[i])
        break

    current_25.popleft()
    current_25.append(nums[i])

