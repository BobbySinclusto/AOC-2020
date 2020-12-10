f = open('input.txt')

nums = [int(line.strip()) for line in f]

nums.append(0)
nums.append(max(nums) + 3)

nums.sort()


from functools import lru_cache
@lru_cache(None)
def countStuff(ci):
    if nums[ci] >= nums[-1] - 3:
        return 1
    elif ci >= len(nums):
        return 0

    cc = 0
    for i in range(ci + 1, len(nums)):
        if nums[i] <= nums[ci] + 3:
            cc += countStuff(i)
        else:
            break

    return cc

print(countStuff(0))
