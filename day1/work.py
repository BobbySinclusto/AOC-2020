f = open('in.txt', 'r')

nums = list(int(n) for n in f.readlines())

for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if i != j and j != k and i != k and nums[i] + nums[j] + nums[k] == 2020:
                print(nums[i], '+', nums[j], '+', nums[k], '= 2020')
                print(nums[i], '*', nums[j], '*', nums[k], '=', nums[i] * nums[j] * nums[k])
                exit()

