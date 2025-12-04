import time

# https://adventofcode.com/2022/day/8

def _1(inp):
    ret = (len(inp)*2) + ((len(inp[0])-2)*2)
    for y in range(1, len(inp)-1, 1):
        for x in range(1, len(inp[y])-1, 1):
            if all(n < int(inp[y][x]) for n in [int(inp[y][n]) for n in range(x+1, x+len(inp[y])-x, 1)]):
                ret += 1; continue
            if all(n < int(inp[y][x]) for n in reversed([int(inp[y][n]) for n in range(0, x, 1)])):
                ret += 1; continue
            if all(n < int(inp[y][x]) for n in reversed([int(inp[n][x]) for n in range(0, y, 1)])):
                ret += 1; continue
            if all(n < int(inp[y][x]) for n in [int(inp[n][x]) for n in range(y+1, y+len(inp)-y, 1)]):
                ret += 1; continue

    return ret

def _2(inp):
    ret = 0
    for y in range(1, len(inp)-1, 1):
        for x in range(1, len(inp[y])-1, 1):
            l, r, t, b = 0, 0, 0, 0

            for rv in [int(inp[y][n]) for n in range(x+1, x+len(inp[y])-x, 1)]:
                r += 1
                if rv >= int(inp[y][x]): break
            for lv in reversed([int(inp[y][n]) for n in range(0, x, 1)]):
                l += 1
                if lv >= int(inp[y][x]): break
            for tv in reversed([int(inp[n][x]) for n in range(0, y, 1)]):
                t += 1
                if tv >= int(inp[y][x]): break
            for bv in [int(inp[n][x]) for n in range(y+1, y+len(inp)-y, 1)]:
                b += 1
                if bv >= int(inp[y][x]): break

            nr = l*r*t*b
            ret = nr if nr > ret else ret
    return ret

if __name__ == '__main__':
    inp = open('input/8.txt', 'r').read().splitlines()
    start = time.time()
    print(_2(inp))
    end = time.time()
    print(end - start)