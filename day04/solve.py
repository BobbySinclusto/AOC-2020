f = open('input.txt', 'r')

count = 0
current = []

for line in f.readlines():
    if line != '\n':
        current += list(thing.split(':')[0] for thing in line.strip().split(' '))
    else:
        expected = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

        for key in expected:
            if key not in current:
                count -= 1
                break

        current = []
        count += 1


expected = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for key in expected:
    if key not in current:
        count -= 1
        break

current = []
count += 1

print(count)
