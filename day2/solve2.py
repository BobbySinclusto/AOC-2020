import re

f = open('input.txt', 'r')

data = []
exp = re.compile(r'(\d*)-(\d*) (.): (.*)')

other_count = 0

for line in f.readlines():
    stuff = exp.search(line).groups()

    if stuff[3][int(stuff[0])-1] == stuff[2] and stuff[3][int(stuff[1])-1] != stuff[2] or stuff[3][int(stuff[0])-1] != stuff[2] and stuff[3][int(stuff[1])-1] == stuff[2]:
        other_count += 1

print(other_count)
