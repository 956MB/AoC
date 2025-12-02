import itertools
import time

# 11386 <<<
# 13600

# https://adventofcode.com/2022/day/2

def _0(inp):
    s1 = s2 = 0

    for i, j in map(str.split, inp):
        i, j = ord(i) - ord("A"), ord(j) - ord("X")
        s1 += 1 + j + (j - i + 1) % 3 * 3
        s2 += 1 + j * 3 + (j + i - 1) % 3

    print(s1)
    print(s2)

def _1(inp):
    global mm
    print(inp)
    ret = 0
    for r in [[mm[i] for i in l.split()] for l in inp]:
        if r[0] == r[1]: ret += r[1] + 3; continue
        if r[1] == r[0]-1: ret += r[1] + 0; continue
        if r[1] == r[0]+1: ret += r[1] + 6; continue
        # ad = 3+r[1] if r[0] == r[1] else 6+r[1] if r[1] > r[0] else 0+r[1] if r[1] < r[0] else 0
        # print(r, ret)
    return ret

def _2(inp):
    pass

if __name__ == '__main__':
    mm = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}
    inp = open('inp2.txt', 'r').read().splitlines()
    start = time.time()
    print(_1(inp))
    end = time.time()
    print(end - start)
