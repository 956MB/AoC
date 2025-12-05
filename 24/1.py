#!/usr/bin/env python3

# https://adventofcode.com/2024/day/1

def _1(left, right):
    return sum(abs(left[i]-right[i]) for i in range(len(left)))

def _2(left, right):
    return sum(n * right.count(n) for n in left)

if __name__ == '__main__':
    # inp = open('./input/1_sample.txt', 'r').read().splitlines()
    inp = open('./input/1.txt', 'r').read().splitlines()
    le, ri = sorted([int(i.split()[0]) for i in inp]), sorted([int(i.split()[1]) for i in inp])
    print("1:", _1(le, ri), "2:", _2(le, ri))