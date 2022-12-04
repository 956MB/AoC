import time

# https://adventofcode.com/2018/day/1

def _1(inp):
    return sum([int(n) for n in inp])

def _2(inp):
    a, s = 0, set()
    while True:
        for n in inp:
            a += int(n)
            if a in s: return a
            s.add(a)

if __name__ == '__main__':
    inp = open('p2.txt', 'r').read().splitlines()
    start = time.time()
    print(_2(inp))
    end = time.time()
    print(end - start)