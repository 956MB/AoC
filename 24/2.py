#!/usr/bin/env python3

# https://adventofcode.com/2024/day/2

def safe(r, dir=-1):
    for i in range(len(r)-1):
        c, n = r[i], r[i+1]
        diff = c - n
        if dir == -1: dir = int(diff > 0)
        if (diff > 0 and dir == 0): return False
        if (diff < 0 and dir == 1): return False
        if abs(diff) not in (1, 2, 3): return False
    return True

def _0(reports, _2=False):
    ret = 0
    for r in reports:
        ok = safe(r)
        if _2 and not ok:
            for i in range(len(r)):
                if safe(r[:i] + r[i+1:]):
                    ok = True
                    break
        if ok: ret += 1
    return ret

if __name__ == '__main__':
    # inp = [[int(x) for x in i.split()] for i in open('./input/2_sample.txt', 'r').read().splitlines()]
    inp = [[int(x) for x in i.split()] for i in open('./input/2.txt', 'r').read().splitlines()]
    print("1:", _0(inp), "2:", _0(inp, True))