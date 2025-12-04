#!/usr/bin/env python3

# https://adventofcode.com/2025/day/2

def _1(ids):
    r = []
    for t in [tuple(int(x) for x in i.split('-')) for i in ids]:
        seq = list(range(t[0], t[1]+1, 1))
        for n in seq:
            sn = str(n)
            if sn[:len(sn)//2] == sn[len(sn)//2:]:
                r.append(n)
    return sum(r)

def _2(ids):
    r = []
    for t in [tuple(int(x) for x in i.split('-')) for i in ids]:
        seq = list(range(t[0], t[1]+1, 1))
        for n in seq:
            sn = str(n)
            for i in range(1, len(sn)//2 + 1):
                if len(sn) % i == 0:
                    chunks = [int(sn[x:x+i]) for x in range(0, len(sn), i)]
                    if len(set(chunks)) == 1:
                        r.append(n)
                        break
    return sum(r)

if __name__ == "__main__":
    # inp = open("input/2_sample.txt", "r").read().split(",")
    inp = open("input/2.txt", "r").read().split(",")
    print("1:", _1(inp), "2:", _2(inp))