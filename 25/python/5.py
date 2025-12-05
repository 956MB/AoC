#!/usr/bin/env python3

# https://adventofcode.com/2025/day/5

def _1(ranges, ids):
    all = set()
    for r in ranges:
        for id in ids:
            if r[0] <= id <= r[1]:
                all.add(id)
    return len(all)

def _2(ranges):
    sr = sorted(ranges, key=lambda x: x[0])
    ret, p = [sr.pop(0)], 0
    for r in sr:
        if ret[p][0] <= r[0] <= ret[p][1]:
            ret[p][1] = max(ret[p][1], r[1])
        else:
            ret.append(r)
            p += 1
    return sum([(n[1] - n[0] + 1) for n in ret])

if __name__ == "__main__":
    # inp = open("input/5_sample.txt", "r").read().split('\n\n')
    inp = open("input/5.txt", "r").read().split('\n\n')
    ranges, ids = [list(int(x) for x in i.split('-')) for i in inp[0].split('\n')], [int(id) for id in inp[1].split('\n')]
    print("1:", _1(ranges, ids), "2:", _2(ranges))