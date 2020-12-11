import re

def verify_stuff(current):

    expected = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    print(current)

    for key in expected:
        if key not in current.keys():
            return False

    if int(current['byr']) < 1920 or int(current['byr']) > 2002:
        return False
    if int(current['iyr']) < 2010 or int(current['iyr']) > 2020:
        return False
    if int(current['eyr']) < 2020 or int(current['eyr']) > 2030:
        return False
    if current['hgt'][-2:] == 'cm':
        if int(current['hgt'][:-2]) < 150 or int(current['hgt'][:-2]) > 193:
            return False
    elif current['hgt'][-2:] == 'in':
        if int(current['hgt'][:-2]) < 59 or int(current['hgt'][:-2]) > 76:
            return False
    else:
        return False

    if re.match(r'^#[0-9a-f]{6}$', current['hcl']) == None:
        return False
    if current['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if re.match(r'^[0-9]{9}$', current['pid']) == None:
        return False
    
    return True

f = open('input.txt', 'r')

count = 0
current = {}

for line in f.readlines():
    print(line.strip())
    if line != '\n':
        current.update({thing.split(':')[0]:thing.split(':')[1] for thing in line.strip().split(' ')})
    else:
        count += (1 if verify_stuff(current) else 0)
        current = {}

count += (1 if verify_stuff(current) else 0)

print(count)
