import time
import re

# https://adventofcode.com/2018/day/3

def _1(inp):
    l = [[int(f) for f in re.search(r"#\d+ @ (\d+),(\d+): (\d+)x(\d+)", i).groups()] for i in inp]
    mw, mh = max([g[0] + g[2] for g in l]), max([g[1] + g[3] for g in l])
    m = [[0 for x in range(mw+1)] for _ in range(mh+1)]
    print(mw, mh)
    for i,v in enumerate(l):
        rl, rt, rw, rh = v[0], v[1], v[2], v[3]
        for y in range(rt, rt+rh, 1):
            for x in range(rl, rl+rw, 1):
                m[y][x] += 1
    # pp(m)
    f = [i for s in m for i in s]
    return len([i for i in f if i > 1])

def _2(inp):
    pass

def pp(inp):
    for i in inp:
        print(i, end='\n')
    print()

if __name__ == '__main__':
    inp = open('p2.txt', 'r').read().splitlines()
    start = time.time()
    print(_1(inp))
    end = time.time()
    print(end - start)