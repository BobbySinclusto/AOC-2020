stuff = {15:1, 5:2, 1:3, 4:4, 7:5}

last_num = 0

# start at turn after last turn
for i in range(len(stuff) + 1, 30000000):
    if last_num in stuff:
        tmp = stuff[last_num]
        stuff[last_num] = i
        last_num = i - tmp
    else:
        stuff[last_num] = i
        last_num = 0

print(last_num)
