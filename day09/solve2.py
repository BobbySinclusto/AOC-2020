from collections import deque

f = open('input.txt')

nums = list(int(line.strip()) for line in f.readlines())

goal = 258585477

current_set = deque(nums[:2])

for i in range(0, len(nums) - 2):
    current_set = deque(nums[i:i+2])
    j = i + 2
    while sum(current_set) <= goal:
        if sum(current_set) == goal:
            print(current_set)
            print(max(current_set) + min(current_set))
            break
        current_set.append(nums[j])
        j += 1
