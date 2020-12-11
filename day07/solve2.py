def main():
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

    print(bags['shiny gold'])

    from functools import lru_cache
    @lru_cache(None)
    def search_bags(key):
        if bags[key] == None:
            return 1
        total = 1 # +1 for current bag
        for bag in bags[key]:
            total += bag[1] * search_bags(bag[0])
        return total

    print(search_bags('shiny gold') - 1)

if __name__ == '__main__':
    main()
