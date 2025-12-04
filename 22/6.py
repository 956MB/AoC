import time

# https://adventofcode.com/2022/day/6

def _1(inp, mlen):
    for i in range(0, len(inp)-mlen, 1):
        if len(set(inp[i:i+mlen])) >= mlen: return i+mlen

if __name__ == '__main__':
    inp = open('input/6.txt', 'r').read()
    start = time.time()
    print(_1(inp, 14))
    end = time.time()
    print(end - start)