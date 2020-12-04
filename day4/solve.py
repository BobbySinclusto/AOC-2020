f = open('input.txt')

current = []
count = 0

for line in f.readlines():
    if line != '\n':
        current += line.strip().split(' ')
        print(line.strip())

    if line == '\n':
        # finished current

        stuffs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        actual = []

        for thing in current:
            actual.append(thing.split(':')[0])

        print(sorted(stuffs))
        print(sorted(actual))
        for stuff in stuffs:
            if stuff not in actual:
                count -= 1
                print('invalid')
                break

        count += 1
        print(count)
        current = []

print(count)
