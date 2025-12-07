#!/usr/bin/env python3

# https://adventofcode.com/2025/day/6

def _1(probs):
    ret = 0
    for i in range(0, len(probs)):
        op = str(probs[i][-1])
        nums = [n for n in probs[i][:-1]]
        expr = op.join(nums)
        # print(f"prob {i}: nums = {nums}, op = {op}, expr = {expr}")
        ret += eval(expr)
    return ret
    # return sum(eval(str(probs[i][-1]).join(n for n in probs[i][:-1])) for i in range(0, len(probs)))

def _2(probs):
    ret = 0
    for p in probs:
        op, d, s = p.pop(), len(str(max([int(i) for i in p]))), []
        # print(op, d, p)
        for x in range(d-1, -1, -1):
            col = ''
            for y in range(0, len(p)):
                v = p[y][x] if x < len(p[y]) else None
                # print("p:", p[y])
                # print("v [x={}]:".format(x), v)
                if v is not None:
                    col += v
            s.append(col)
        cons = str(op).join(s)
        j = eval(cons)
        ret += j
        print(s, cons, j)

    return ret

if __name__ == "__main__":
    # inp = open("input/6_sample.txt", "r").read().splitlines()
    inp = open("input/6.txt", "r").read().splitlines()
    p = list(zip(*[r.split() for r in inp]))
    print(p)
    # print("1:", _1(p), "2:", _2(map(list, p)))