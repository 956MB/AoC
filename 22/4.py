import time
import collections as cl
import re

# https://adventofcode.com/2022/day/4

def _1(inp):
    c = 0
    for i in inp:
        r = [int(n) for n in re.search(r"(\d+)-(\d+),(\d+)-(\d+)", i).groups()]
        c += 1 if (r[0] >= r[2] and r[1] <= r[3]) or (r[0] <= r[2] and r[1] >= r[3]) else 0
    return c

def _2(inp):
    c = 0
    for i in inp:
        r = [int(n) for n in re.search(r"(\d+)-(\d+),(\d+)-(\d+)", i).groups()]
        c += 1 if any(i >= 2 for i in cl.Counter(list(range(r[0], r[1]+1)) + list(range(r[2], r[3]+1))).values()) else 0
    return c

if __name__ == '__main__':
    inp = open('input/4.txt', 'r').read().splitlines()
    start = time.time()
    print(_2(inp))
    end = time.time()
    print(end - start)