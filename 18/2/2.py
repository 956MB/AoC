import time
import collections

# https://adventofcode.com/2018/day/2

def _1(inp):
    t2, t3 = 0, 0
    for n in inp:
        f = collections.Counter(list(n))
        t2, t3 = t2 + int(2 in list(f.values())), t3 + int(3 in list(f.values()))
    return t2*t3

def _2(inp):
    m = []
    for n1 in range(0, len(inp)):
        for n2 in range(n1+1, len(inp)):
            c, w1, w2 = 0, inp[n1], inp[n2]
            for r in range(len(w2)):
                c += 1 if w1[r] != w2[r] else 0
                if c >= 2: break
            if c == 1: m.extend([w1, w2])
    return ''.join([m[0][l] if m[0][l] == m[1][l] else '' for l in range(len(m[0]))])

if __name__ == '__main__':
    inp = open('p2.txt', 'r').read().splitlines()
    start = time.time()
    print(_2(inp))
    end = time.time()
    print(end - start)