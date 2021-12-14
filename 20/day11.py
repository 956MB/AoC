# https://adventofcode.com/2020/day/11

import copy

def _main(p2):
    global _input
    cop = copy.deepcopy(_input)
    co = 5 if p2 else 4
    # _loop(_input)

    while True:
        score = sum([scores[i] for sub in _input for i in sub])
        for y in range(len(_input)):
            for x in range(len(_input[y])):
                c = _input[y][x]
                if c == ".": continue
                _all, ul, ur, u, d, l, r, dl, dr = [], ".", ".", ".", ".", ".", ".", ".", "."
                
                if not p2:
                    if _inside(y-1, x-1): ul = _input[y-1][x-1]
                    if _inside(y-1, x+1): ur = _input[y-1][x+1]
                    if _inside(y-1, x): u = _input[y-1][x]
                    if _inside(y+1, x): d = _input[y+1][x]
                    if _inside(y, x-1): l = _input[y][x-1]
                    if _inside(y, x+1):r = _input[y][x+1]
                    if _inside(y+1, x-1): dl = _input[y+1][x-1]
                    if _inside(y+1, x+1): dr = _input[y+1][x+1]
                else:
                    ul = _traverse(y, x, -1, -1)
                    ur = _traverse(y, x, -1, 1)
                    u = _traverse(y, x, -1, 0)
                    d = _traverse(y, x, 1, 0)
                    l = _traverse(y, x, 0, -1)
                    r = _traverse(y, x, 0, 1)
                    dl = _traverse(y, x, 1, -1)
                    dr = _traverse(y, x, 1, 1)

                _all = [ul, ur, u, d, l, r, dl, dr]

                if c == "L":
                    if _all.count("#") <= 0:
                        cop[y][x] = "#"
                elif c == "#":
                    if _all.count("#") >= co:
                        cop[y][x] = "L"

        newscore = sum([scores[i] for sub in cop for i in sub])
        if score == newscore:
            # _loop(_input)
            return [i for sub in cop for i in sub].count("#")
        _input = copy.deepcopy(cop)

def _loop(l):
    for i in l:
        for x in i:
            print(x, end=" ")
        print()
    print()

def _traverse(starty, startx, plusy, plusx):
    global _input
    y = starty + plusy
    x = startx + plusx
    ret = "."

    while _inside(y, x):
        ret = _input[y][x]
        if ret != ".":
            return ret
        y += plusy
        x += plusx

    return ret

def _inside(y, x):
    if x <= -1: return False
    if x >= len(_input[0]): return False
    if y <= -1: return False
    if y >= len(_input): return False
    return True

if __name__ == '__main__':
    # _input = [
    #     ["L",".","L","L",".","L","L",".","L","L"],
    #     ["L","L","L","L","L","L","L",".","L","L"],
    #     ["L",".","L",".","L",".",".","L",".","."],
    #     ["L","L","L","L",".","L","L",".","L","L"],
    #     ["L",".","L","L",".","L","L",".","L","L"],
    #     ["L",".","L","L","L","L","L",".","L","L"],
    #     [".",".","L",".","L",".",".",".",".","."],
    #     ["L","L","L","L","L","L","L","L","L","L"],
    #     ["L",".","L","L","L","L","L","L",".","L"],
    #     ["L",".","L","L","L","L","L",".","L","L"]
    # ]

    _input = [
        [".","L","L","L","L",".","L",".","L","L","L","L",".","L","L",".","L","L","L",".","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L",".",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L",".","L","L",".","L","L","L","L","L",".","L","L","L","L",".","L",".","L","L","L","L",".","L","L","L","L","L","L",".","L",".","L","L","L",".","L","L",".",".","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L",".","L","L","L"],
        ["L","L",".","L","L","L","L",".","L","L","L","L","L","L","L",".","L",".","L","L","L",".","L","L","L","L","L","L",".","L",".","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L",".","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L",".","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","."],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L",".","L",".","L","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L",".","L","L","L","L"],
        [".",".",".",".","L",".",".","L",".",".",".",".",".","L",".",".",".",".",".",".","L","L",".",".",".","L",".","L","L",".",".",".",".",".",".",".","L",".",".",".","L",".","L",".",".",".",".",".",".","L",".","L",".","L","L","L",".",".",".",".","L",".",".","L",".",".",".",".","L",".","L","L",".",".","L","L","L",".",".",".",".","L","L",".",".","L",".",".","L",".",".",".","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","."],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L",".","L","L","L","L","L",".","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L",".","L","L",".","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L",".","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L",".","L","L","L"],
        ["L","L","L","L","L","L","L",".",".","L","L","L","L","L","L",".","L","L","L","L","L",".",".","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L",".","L","L","L",".",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L"],
        [".",".",".","L",".",".",".","L",".",".","L","L",".",".",".",".","L",".",".",".",".",".",".",".","L",".",".",".","L",".",".",".",".",".",".",".","L","L",".",".",".",".",".",".",".",".","L","L",".",".",".",".",".","L","L",".",".",".",".","L",".",".",".",".",".","L","L",".",".",".",".",".",".",".",".",".",".",".",".","L",".",".","L","L",".",".",".",".","L",".",".",".","."],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".",".","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".","L",".",".","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L",".","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L",".","L","L","L","L","L","L","L","L","L","L",".",".",".","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L",".","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L",".","L",".","L","L","L","L","L"],
        [".",".",".",".",".",".",".",".",".",".",".","L","L",".",".",".",".",".","L",".","L","L",".",".",".",".","L",".",".",".",".","L",".",".","L","L",".",".","L","L",".","L",".","L","L","L","L",".",".",".",".",".",".",".",".","L","L",".","L",".","L","L",".",".","L",".",".",".",".",".",".","L",".",".",".","L","L",".",".",".","L","L",".",".","L",".","L",".",".",".",".",".","."],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L",".","L","L","L","L","L",".",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L",".",".","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L",".",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L",".","L","L",".",".",".","L",".",".",".",".","L","L","L",".","L",".","L",".",".",".",".","L","L",".","L",".",".",".",".",".","L",".",".",".","L","L","L",".",".","L","L",".",".",".",".",".",".",".","L",".",".",".",".",".",".",".","L",".",".",".",".",".",".",".","L",".",".","L",".",".",".",".",".",".","L","L","L",".",".","L",".","L","L",".",".","L","L",".",".","L"],
        ["L","L","L","L",".","L","L",".","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L"],
        ["L","L","L","L","L",".","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".",".",".","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        [".","L",".",".",".",".",".",".","L","L",".",".",".","L",".","L",".",".",".",".","L",".",".",".","L",".",".",".",".",".",".",".",".",".",".",".","L",".","L","L",".",".",".","L",".","L","L","L","L","L",".",".",".",".",".","L","L",".",".",".",".","L",".",".",".",".",".",".","L",".","L","L",".",".","L",".",".","L",".",".",".",".",".","L",".",".",".","L",".","L",".","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L",".","L","L","L",".",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L",".","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L",".","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L",".","L",".","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L",".","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        [".",".","L",".",".",".",".","L",".","L",".","L","L",".","L",".",".",".",".",".",".",".",".",".","L",".",".",".","L","L",".","L",".",".",".",".","L","L",".",".",".",".",".",".","L","L",".",".","L","L",".","L",".","L",".",".",".",".",".","L",".",".","L",".",".","L",".",".","L",".",".","L","L",".","L",".",".",".","L",".",".","L",".",".",".",".","L",".",".",".",".",".","."],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L",".",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L",".","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L","L","L","L","L","L","L",".","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L",".","L","L",".","L","L","L","L","L","L","L","L",".",".","L",".","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        [".","L",".",".",".",".",".",".","L",".",".",".",".","L",".","L",".","L",".",".",".","L","L","L","L",".",".",".",".",".",".","L","L",".",".",".","L","L",".",".",".","L",".",".",".","L",".",".",".",".",".",".","L",".",".","L",".",".",".",".",".",".",".",".",".",".",".","L",".",".",".",".",".",".","L",".",".",".",".",".",".",".","L",".",".",".",".","L",".","L",".",".","."],
        ["L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L",".","L","L","L","L",".","L","L","L","L","L"],
        ["L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L",".","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        [".","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L",".","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L",".","L","L","L","L",".","L","L","L",".","L","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".",".","L","L","L","L"],
        [".","L",".",".",".",".",".","L",".",".",".","L",".",".",".",".","L",".","L","L",".",".",".",".",".",".",".",".",".",".",".",".","L","L",".",".","L",".","L","L",".",".",".",".",".","L","L","L",".",".","L",".",".",".",".",".",".",".",".",".",".",".",".",".","L",".",".",".",".",".",".",".",".",".",".",".","L",".",".",".","L",".","L",".","L",".",".",".",".",".",".",".","."],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L",".","L","L",".","L","L","L",".",".","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L"],
        ["L","L","L",".","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L",".",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L",".","L","L"],
        [".","L","L","L","L","L","L",".","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L",".","L",".","L",".",".",".","L",".",".",".","L",".",".",".","L","L","L",".",".",".",".",".",".",".","L","L","L",".",".","L",".","L",".",".",".","L",".",".",".",".",".",".",".","L",".",".",".",".",".",".","L",".","L","L",".",".",".",".",".",".",".","L",".",".","L","L","L",".","L",".",".","L",".","L",".","L","L",".",".","L",".",".","L",".","L",".","L","L","L","."],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L",".",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L",".","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L",".","L","L","L","L",".",".","L","L","L",".","L","L","L","L","L","L","L","L",".","L",".","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L",".","L","L",".","L","L","L","L","L","L",".","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L",".","L","L","L","L","."],
        ["L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L",".","L","L","L","L",".","L",".","L","L","L","L",".","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L",".","L","L"],
        [".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L",".","L","L","L","L","L"],
        ["L","L",".",".",".",".","L",".",".",".",".","L",".",".","L",".","L",".",".",".",".",".","L",".","L",".",".",".","L",".",".",".","L",".",".",".",".",".","L",".",".",".",".",".","L",".",".",".",".","L","L","L",".",".","L",".","L",".",".","L",".",".","L",".","L","L",".","L",".",".",".","L",".","L","L","L",".",".",".",".",".",".",".","L",".",".",".",".","L",".","L","L","."],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L",".",".","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L",".","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L",".","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L",".","L","L","L","L","L","L",".","L","L",".","L",".","L","L","L",".","L","L","L","L","L","L","L","L","L",".",".","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        [".",".","L",".",".","L",".",".","L",".","L",".",".",".",".",".",".",".","L",".",".","L","L",".",".",".","L",".","L",".",".","L","L",".",".",".","L",".",".",".",".",".",".",".",".",".",".",".",".","L",".","L",".",".",".","L",".",".",".",".",".","L",".",".",".","L","L",".",".","L","L",".",".",".",".",".",".","L",".","L",".",".",".","L",".",".",".",".",".","L",".",".","L"],
        ["L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L",".","L","L","L",".","L","L",".","L","L","L",".","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L",".","L","L","L",".","L","L",".",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L",".",".","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".","L","L"],
        ["L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L",".",".",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".","L",".","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L",".","L","L","."],
        ["L","L",".","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".",".","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L",".","L","L",".","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L",".","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L"],
        ["L",".","L","L","L","L","L",".","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L",".","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L",".","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L",".",".","L","L","L","L"],
        ["L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L",".","L","L","L",".","L","L","L","L","L","L","L","L","L","L",".",".","L","L",".","L","L","L","L","L","L",".","L","L","L","L","L","L","L","L",".","L","L","L","L","L",".","L","L","L","L","L","L","L","L","L","L","L","L","L"]
    ]

    scores = {".":0, "L":1, "#":2}

    res = _main(True)
    print(res)