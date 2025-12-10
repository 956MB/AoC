#!/usr/bin/env python3

# https://adventofcode.com/2025/day/9

def _1(points):
    ret = 0
    for i, p1 in enumerate(points):
        for p2 in points[i+1:]:
            a = (abs(p1[1] - p2[1]) + 1) * (abs(p1[0] - p2[0]) + 1)
            if a > ret:
                ret = a
    return ret

if __name__ == "__main__":
    # inp = open("input/9_sample.txt", "r").read().splitlines()
    inp = open("input/9.txt", "r").read().splitlines()
    points = [tuple(int(x) for x in line.split(',')) for line in inp]
    print("1:", _1(points))