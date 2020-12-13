import math

f = open('input.txt')

goal = int(f.readline().strip())

times = []

for t in f.readline().strip().split(','):
    if t != 'x':
        times.append(int(t))

min_diff = math.inf
bus_id = 0

for t in times:
    test = (goal // t) * t
    if test < goal:
        test += t

    if test - goal < min_diff:
        min_diff = test - goal
        bus_id = t

print(bus_id, min_diff)
print(bus_id * min_diff)
