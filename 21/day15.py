# https://adventofcode.com/2020/day/15

import copy
import random
import os
from time import sleep

def _main(p2):
    global _input, cop
    # scores = []
    lowest = 1000
    count = 0

    while True:
        count += 1
        score, y, x = 0, 0, 0
        _input = copy.deepcopy(cop)
        _input[y][x] = -1
        while True:

            if y == len(_input)-1 and x == len(_input[-1])-1:
                # scores.append(score)
                if score <= lowest: lowest = score
                if score == 40: return -1
                break

            ndir = _next(y, x)
            if ndir == -1: break
            y += ndir[0]
            x += ndir[1]

            score += _input[y][x]
            _input[y][x] = -1

            clear()
            print(score, [y, x], ndir)
            # print("scores len:", len(scores))
            print("count:", count)
            print("lowest:", lowest)
            # print(scores)
            print()
            # _loop(_input)
            # sleep(0.05)


def _loop(l):
    for i in l:
        for x in i:
            if x == -1:
                print("\033[96m{} \033[0m".format("X"), end="")
            # if x == -2:
            #     print("\033[96m{} \033[0m".format("X"), end="")
            else:
                print("\033[93m{} \033[0m".format(x), end="")
        print()
    print()

def _next(y, x):
    global _weights
    ret = []

    if y == len(_input)-1:
        if (_inside(y, x+1)) and (not _vis(y, x+1)): ret.append([3, [0,1]])  #right
    elif x == len(_input[-1])-1:
        if (_inside(y+1, x)) and (not _vis(y+1, x)): ret.append([1, [1,0]])  #down
    else:
        # if (_inside(y-1, x)) and (not _vis(y-1, x)): ret.append([0, [-1,0]]) #up
        if (_inside(y+1, x)) and (not _vis(y+1, x)): ret.append([1, [1,0]])  #down
        # if (_inside(y, x-1)) and (not _vis(y, x-1)): ret.append([2, [0,-1]]) #left
        if (_inside(y, x+1)) and (not _vis(y, x+1)): ret.append([3, [0,1]])  #right

    if len(ret) <= 0: return -1
    # return random.choices(ret, weights=[_weights[x[0]] for x in ret], k=1)[0][1]
    return random.choice(ret)[1]

def _vis(y, x):
    # global visited
    return _input[y][x] == -1

def _inside(y, x):
    if x <= -1: return False
    if x >= len(_input[0]): return False
    if y <= -1: return False
    if y >= len(_input): return False
    return True

if __name__ == '__main__':
    _input = [
        [1,1,6,3,7,5,1,7,4,2],
        [1,3,8,1,3,7,3,6,7,2],
        [2,1,3,6,5,1,1,3,2,8],
        [3,6,9,4,9,3,1,5,6,9],
        [7,4,6,3,4,1,7,1,1,1],
        [1,3,1,9,1,2,8,1,3,7],
        [1,3,5,9,9,1,2,4,2,1],
        [3,1,2,5,4,2,1,6,3,9],
        [1,2,9,3,1,3,8,5,2,1],
        [2,3,1,1,9,4,4,5,8,1]
    ]
    _weights = {0: 0.0, 1: 1.0, 2: 0.0, 3: 1.0}
    # _weights = {0: 0.05, 1: 0.95, 2: 0.05, 3: 0.95}
    clear = lambda: os.system('cls')
    cop = copy.deepcopy(_input)

    res = _main(True)
    print(res)