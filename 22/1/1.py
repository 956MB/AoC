import itertools
import time

def _1(inp):
    return max([sum([int(n) for n in l]) for l in [list(y) for x, y in itertools.groupby(inp.split('\n'), lambda z: z == '') if not x]])

def _2(inp):
    c = [sum([int(n) for n in l]) for l in [list(y) for x, y in itertools.groupby(inp.split('\n'), lambda z: z == '') if not x]]
    return sum(sorted(c)[-3:])

if __name__ == '__main__':
    inp = open('inp.txt', 'r').read()
    start = time.time()
    print(_2(inp))
    end = time.time()
    print(end - start)