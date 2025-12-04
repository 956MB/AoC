import itertools
import time

# https://adventofcode.com/2022/day/1

def _1(inp):
    return max([sum([int(n) for n in l]) for l in [list(y) for x, y in itertools.groupby(inp.split('\n'), lambda z: z == '') if not x]])

def _2(inp):
    return sum(sorted([sum([int(n) for n in l]) for l in [list(y) for x, y in itertools.groupby(inp.split('\n'), lambda z: z == '') if not x]])[-3:])

if __name__ == '__main__':
    inp = open('input/1.txt', 'r').read()
    start = time.time()
    print(_2(inp))
    end = time.time()
    print(end - start)