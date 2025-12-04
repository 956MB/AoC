#!/usr/bin/env python3

# https://adventofcode.com/2025/day/3

def _0(banks, count, r=0):
    for bank in banks:
        group, start = [], 0
        for d in range(0, count):
            end = len(bank) - (count - d) + 1
            num = max(bank[start:end])
            start = bank.find(num, start) + 1
            group.append(num)
        r += int(''.join(group))
    return r

if __name__ == "__main__":
    # inp = open("input/3_sample.txt", "r").read().splitlines()
    inp = open("input/3.txt", "r").read().splitlines()
    print("1:", _0(inp, 2), "2:", _0(inp, 12))