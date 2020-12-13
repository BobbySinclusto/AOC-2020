import math
from multiprocessing import Pool

def pls_work(start, end, times, stamps):
    while start % times[0] != 0:
        start += 1
    for t in range(start, end, times[0]):
        for i in range(len(times)):
            if (t + stamps[i]) % times[i] != 0:
                break
            elif i == len(times) - 1:
                print(t)
                return t
    return math.inf

def main():
    f = open('input.txt')

    goal = int(f.readline().strip())

    times = []
    stamps = []

    for i, t in enumerate(f.readline().strip().split(',')):
        if t != 'x':
            times.append(int(t))
            stamps.append(i)

    print(times)
    print(stamps)

    search_range = [100000000000000, 200000000000000]
    pool_size = 100

    with Pool(pool_size) as p:
        print(min(p.starmap(pls_work, [(i, i + search_range[1] // pool_size, times, stamps) for i in range(search_range[0], search_range[1], search_range[1] // pool_size)])))

if __name__ == '__main__':
    main()
