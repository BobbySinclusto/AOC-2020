f = open('input.txt')

nums = [int(line.strip()) for line in f]

nums.sort()

nums.append(max(nums) + 3)

counts = [0, 0, 0, 0]

current_min = 0

for num in nums:
    if num <= current_min + 3:
        counts[num - current_min] += 1
        current_min = num

print(counts[1], counts[3], counts[1] * counts[3])
