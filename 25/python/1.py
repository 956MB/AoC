#!/usr/bin/env python3

# https://adventofcode.com/2025/day/1

def _1(input, start):
    r = 0
    for line in input:
        num = int(line[1:])
        start = (start + (-num if line[0] == 'L' else num)) % 100
        r += 1 if start == 0 else 0
    return r

def _2(input, start):
    r = 0
    for line in input:
        num = int(line[1:])
        seq = [(start + i * (-1 if line[0] == 'L' else 1)) % 100 for i in range(1, num + 1)]
        r += seq.count(0)
        start = seq[-1]
    return r

if __name__ == "__main__":
    # inp = open("input/1_sample.txt", "r").read().splitlines()
    inp = open("input/1.txt", "r").read().splitlines()
    print("1:", _1(inp, 50), "2:", _2(inp, 50))