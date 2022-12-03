import string
import time

# https://adventofcode.com/2022/day/3

def _1(inp):
    return sum([string.ascii_letters.index(i)+1 for i in [t for group in [list(set(l[:len(l)//2]) & set(l[len(l)//2:])) for l in inp] for t in group]])

def _2(inp):
    return sum([string.ascii_letters.index(i)+1 for i in [t for group in [list(set(g[0]).intersection(g[1], g[2])) for g in [inp[i:i + 3] for i in range(0, len(inp), 3)]] for t in group]])

if __name__ == '__main__':
    inp = open('p2.txt', 'r').read().splitlines()
    start = time.time()
    print(_2(inp))
    end = time.time()
    print(end - start)