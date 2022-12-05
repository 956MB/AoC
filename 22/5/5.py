import time
import re

# https://adventofcode.com/2022/day/5

def _1(inp, _2=False):
    c, ms = inp[0].split('\n'), inp[1].split('\n')
    nx = max([int(i) for i in list(c.pop().replace(' ', ''))])
    crates = [[] for _ in range(nx)]

    for l in range(len(c)-1, -1, -1):
        gs = re.search(f"{'(.{3}) ' * nx}"[:-1], c[l]).groups()
        for i,g in enumerate(gs):
            if g != '   ': crates[i].append(g)

    for m in ms:
        ss = [int(n) for n in re.search(r"move (\d+) from (\d+) to (\d+)", m).groups()]
        if _2:
            crates[ss[2]-1].extend(reversed([crates[ss[1]-1].pop() for _ in range(ss[0])]))
        else:
            for i in range(ss[0]):
                crates[ss[2]-1].append(crates[ss[1]-1].pop())

    return ''.join([l[-1] for l in crates]).replace('[', '').replace(']', '')

if __name__ == '__main__':
    inp = open('p2.txt', 'r').read().split('\n\n')
    start = time.time()
    print(_1(inp, True))
    end = time.time()
    print(end - start)