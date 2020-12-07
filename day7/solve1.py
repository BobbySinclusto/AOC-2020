f = open('input.txt')

#{color: [(color, quantity)]}
bags = {}
valid = set()

for line in f.readlines():
    s = line.split(' ')
    b = ' '.join(s[0:2])
    inside = ' '.join(s[4:])
    if inside == 'no other bags.\n':
        bags[b] = None
    else:
        stuff = list((' '.join(a[1:3]), int(a[0])) for a in (thing.split(' ') for thing in inside.split(', ')))
        bags[b] = stuff

for i in range(len(bags)):
    for bag in bags.keys():
        if bags[bag] != None:
            these_bags = list(thing[0] for thing in bags[bag])
            for thing in these_bags:
                if 'shiny gold' == thing or thing in valid:
                    valid.add(bag)
                    break

print(valid)
print(len(valid))

