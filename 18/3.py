import time
import re
import collections as cl

# https://adventofcode.com/2018/day/3

def _1(inp):
    l = [[int(f) for f in re.search(r"#\d+ @ (\d+),(\d+): (\d+)x(\d+)", i).groups()] for i in inp]
    mw, mh = max([g[0] + g[2] for g in l]), max([g[1] + g[3] for g in l])
    m = [[0 for x in range(mw+1)] for _ in range(mh+1)]
    for i,v in enumerate(l):
        rl, rt, rw, rh = v[0], v[1], v[2], v[3]
        for y in range(rt, rt+rh, 1):
            for x in range(rl, rl+rw, 1):
                m[y][x] += 1
    f = [i for s in m for i in s]
    return len([i for i in f if i > 1])

def _2(inp):
    l = [[int(f) for f in re.search(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", i).groups()] for i in inp]
    mw, mh = max([g[1] + g[3] for g in l]), max([g[2] + g[4] for g in l])
    m = [[0 for x in range(mw+1)] for _ in range(mh+1)]
    for i,v in enumerate(l):
        c, rl, rt, rw, rh = v[0], v[1], v[2], v[3], v[4]
        for y in range(rt, rt+rh, 1):
            for x in range(rl, rl+rw, 1):
                m[y][x] = i+1 if m[y][x] == 0 else -1
    f = cl.Counter([i for s in m for i in s])
    for cs in l:
        if f[cs[0]] == (cs[3]*cs[4]): return cs[0]

def pp(inp):
    for i in inp:
        print(i, end='\n')
    print()

if __name__ == '__main__':
    inp = open('input/3.txt', 'r').read().splitlines()
    start = time.time()
    print(_2(inp))
    end = time.time()
    print(end - start)