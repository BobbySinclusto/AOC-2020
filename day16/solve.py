f = open('input.txt')

rules = {}

line = f.readline().strip()

while line != '':
    nums = [[int(num) for num in nums.split('-')] for nums in line.split(': ')[1].split(' or ')]
    rules[line.split(':')[0]] = nums
    line = f.readline().strip()

f.readline()

my_ticket = [int(n) for n in f.readline().strip().split(',')]

f.readline()
f.readline()

nearby_tickets = []
for line in f:
    nearby_tickets.append([int(n) for n in line.strip().split(',')])

#nearby_tickets.append(my_ticket)

# Part 1
error_rate = 0

i = len(nearby_tickets) - 1
while i >= 0:
    bad = False
    for n in nearby_tickets[i]:
        valid = False
        for c in rules:
            for r in rules[c]:
                if r[0] <= n <= r[1]:
                    # valid, go to next field
                    valid = True
                    break
            if valid:
                break
        if not valid:
            bad = True
            error_rate += n

    if bad:
        # remove this ticket
        nearby_tickets.pop(i)
        
    i -= 1

print(error_rate)

# Part 2
# loop through each rule
# loop through each index of rules on ticket
# loop through each ticket
# if one fails the check, break

possible = {}
possible_nums = {}

for i in range(len(nearby_tickets[0])):
    for c in rules:
        good = True
        for t in nearby_tickets:
            if not (rules[c][0][0] <= t[i] <= rules[c][0][1] or rules[c][1][0] <= t[i] <= rules[c][1][1]):
                good = False
                break

        if good:
            if c not in possible:
                possible[c] = [i]
            else:
                possible[c].append(i)
            if c not in possible_nums:
                possible_nums[i] = [c]
            else:
                possible_nums[i].append(c)

actual = {}

# this is so dumb
sorted_dict = {}
for k in sorted(possible, key=lambda x: len(possible[x])):
    sorted_dict[k] = possible[k]

for k in sorted_dict:
    for thing in sorted_dict[k]:
        if thing not in actual:
            actual[thing] = k


actual_useful = {v:k for k,v in actual.items()}
print(actual_useful)

stuffs = ['departure location','departure station','departure platform','departure track','departure date','departure time']

result = 1

for thing in stuffs:
    result *= my_ticket[actual_useful[thing]]

print(result)
