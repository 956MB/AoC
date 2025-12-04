#!/usr/bin/env python3

# https://adventofcode.com/2025/day/4

def inside(x, y, xl, yl):
    return (x > -1 and x < xl and y > -1 and y < yl)

def roll(p):
    return p == '@'

def _0(floor, _2=False, ret=0):
    rem, xl, yl, dirs = [], len(floor[0]), len(floor), [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    
    for y in range(0, yl):
        for x in range(len(floor[y])):
            if not roll(floor[y][x]):
                continue
            
            count = 0
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if inside(nx, ny, xl, yl) and roll(floor[ny][nx]):
                    count += 1
                    if count >= 4:
                        break
            
            if count < 4:
                ret += 1
                if _2:
                    rem.append((x, y))
    
    if _2 and len(rem) > 0:
        for r in rem:
            floor[r[1]][r[0]] = '.'
        ret = _0(floor, True, ret)

    return ret

if __name__ == "__main__":
    # inp = [list(i) for i in open("input/4_sample.txt", "r").read().splitlines()]
    inp = [list(i) for i in open("input/4.txt", "r").read().splitlines()]
    print("1:", _0(inp), "2:", _0(inp, True))