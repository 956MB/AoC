# https://adventofcode.com/2021/day/11

import os
from time import sleep

def _main():
    _print(0, 0, 0)

    for s in range(steps):
        for y in range(len(_input)):
            for x in range(len(_input[y])):
                _input[y][x] += 1
                if _input[y][x] == 10: _flash(x, y)
                
        _print(s, x, y)

        for y in range(len(_input)):
            for x in range(len(_input[y])):
                if _input[y][x] >= 10: _input[y][x] = 0

        if all(v == 0 for v in [item for sublist in _input for item in sublist]): return s+1

    return flashes

def _change(x, y):
    _input[y][x] += 1
    if _input[y][x] == 10: _flash(x, y)

def _flash(x, y):
    global flashes
    flashes += 1

    if (y-1 >= 0 and x >= 0): _change(x, y-1)                                # up
    if (y+1 <= len(_input)-1 and x >= 0): _change(x, y+1)                    # down
    if (y >= 0 and x-1 >= 0): _change(x-1, y)                                # left
    if (y >= 0 and x+1 <= len(_input[0])-1): _change(x+1, y)                 # right
    if (y-1 >= 0 and x-1 >= 0): _change(x-1, y-1)                            # top left
    if (y-1 >= 0 and x+1 <= len(_input[0])-1): _change(x+1, y-1)             # top right
    if (y+1 <= len(_input)-1 and x-1 >= 0): _change(x-1, y+1)                # bottom left
    if (y+1 <= len(_input)-1 and x+1 <= len(_input[0])-1): _change(x+1, y+1) # bottom right

def _print(step, x, y):
        clear()
        print("step:", step+1, "flashes:", flashes)
        print()
        for py in range(len(_input)):
            for px in range(len(_input[y])):
                if py == y and px == x:
                    print("\033[31m{} \033[0m".format(_input[py][px]), end="")
                else:
                    if _input[py][px] == 0:
                        print("\033[90m{} \033[0m".format(_input[py][px]), end="")
                    elif _input[py][px] >= 10:
                        print("\033[96m{} \033[0m".format("+"), end="")
                    else:
                        print("\033[93m{} \033[0m".format(_input[py][px]), end="")
            print()
        # input()
        # sleep(0.005)

if __name__ == '__main__':
    flashes = 0
    steps = 1000

    # _input = [
    #     [1,1,1,1,1],
    #     [1,9,9,9,1],
    #     [1,9,1,9,1],
    #     [1,9,9,9,1],
    #     [1,1,1,1,1]
    # ]

    # _input = [
    #     [5,4,8,3,1,4,3,2,2,3],
    #     [2,7,4,5,8,5,4,7,1,1],
    #     [5,2,6,4,5,5,6,1,7,3],
    #     [6,1,4,1,3,3,6,1,4,6],
    #     [6,3,5,7,3,8,5,4,7,8],
    #     [4,1,6,7,5,2,4,6,4,5],
    #     [2,1,7,6,8,4,1,7,2,1],
    #     [6,8,8,2,8,8,1,1,3,4],
    #     [4,8,4,6,8,4,8,5,5,4],
    #     [5,2,8,3,7,5,1,5,2,6]
    # ]

    _input = [
        [4,1,1,2,2,5,6,3,7,2],
        [3,1,4,3,2,5,3,7,1,2],
        [4,5,1,6,8,4,8,6,3,1],
        [3,7,8,3,4,7,7,1,3,7],
        [3,7,4,6,7,2,3,5,8,2],
        [5,8,6,1,3,5,8,8,8,4],
        [4,8,4,3,3,5,1,7,7,4],
        [2,3,1,6,4,4,7,6,2,1],
        [6,6,4,3,8,1,7,7,4,5],
        [6,3,6,6,8,1,5,8,6,8]
    ]

    clear = lambda: os.system('cls')

    res = _main()
    print(res)