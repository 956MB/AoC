#!/usr/bin/env python3

# https://adventofcode.com/2025/day/7

def split(locs, inp):
    for y, x in locs:
        inp[y][x] = '|'
    return inp

def _1(inp):
    ret = 0
    for y in range(1, len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == '.' and inp[y-1][x] in ['S', '|']:
                split([(y, x)], inp); continue
            if inp[y][x] == '^':
                split([(y, x-1), (y, x+1)], inp)
                if inp[y-1][x] == '|':
                    ret += 1
    return ret

def _2(sy, x, inp, memo={}):
    if (sy, x) in memo:
        return memo[(sy, x)]

    y = sy
    while y < len(inp) - 1:
        y += 1
        if inp[y][x] == '^':
            res = _2(y, x-1, inp, memo) + _2(y, x+1, inp, memo)
            memo[(sy, x)] = res
            return res

    memo[(sy, x)] = 1
    return 1

if __name__ == "__main__":
    # inp = [list(i) for i in open("input/7_sample.txt", "r").read().splitlines()]
    inp = [list(i) for i in open("input/7.txt", "r").read().splitlines()]
    print("1:", _1(inp), "2:", _2(1, inp[0].index('S'), inp))