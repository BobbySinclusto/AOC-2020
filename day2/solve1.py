import re

f = open('input.txt', 'r')

data = []
exp = re.compile(r'(\d*)-(\d*) (.): (.*)')

other_count = 0

for line in f.readlines():
    stuff = exp.search(line).groups()

    count = 0
    for c in stuff[3]:
        if c == stuff[2]:
            count += 1

    if int(stuff[0]) <= count and int(stuff[1]) >= count:
        other_count += 1

print(other_count)
