# https://adventofcode.com/2020/day/13

import copy

def _p1():
    global _input
    ret = []

    for d in _input[1]:
        if d != "x":
            ret.append([d, _trav(d, d*(_input[0]//d))])

    ret = sorted(ret, key=lambda x: int(x[1]))
    print(ret)
    return (ret[0][1] - _input[0]) * ret[0][0]

def _p2():
    global _input, lar

    for i in range(1, len(_input[1])):
        if _input[1][i] == "x": _input[1][i] = _input[1][i-1]+1
    # _input[1][:] = [x if x != "x" else 1 for x in _input[1]]
    lar = sorted(_input[1])[-1]
    for d in range(len(_input[1])):
        # _input[1][d] = [_input[1][d], _input[1][d]*(_input[0]//_input[1][d])]
        _input[1][d] = [_input[1][d], _input[1][d]]

    print(_input)
    print(lar)
    print()
    # return -1

    for x in range(100000):
        _add()
        if _lin(_input[1]):
            print("linear")
            break

    return _input

def _trav(add, t):
    global _input
    ch = t
    while ch < _input[0]:
        ch += add
    return ch

def _add():
    global _input, lar
    for i in range(len(_input[1])):
        ad = _input[1][i][0]
        _input[1][i] = [ad, _input[1][i][1]+(ad*(lar//ad))]

def _lin(li):
    for i in range(1, len(li)):
        if li[i][1] > li[i-1][1]+1: return False
    return True

if __name__ == '__main__':
    _input = [
        939,
        [7,13,"x","x",59,"x",31,19]
    ]
    lar = 0

    # _input = [
    #     1008832,
    #     [23,"x","x","x","x","x","x","x","x","x","x","x","x",41,"x","x","x","x","x","x","x","x","x",449,"x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x",13,19,"x","x","x","x","x","x","x","x","x",29,"x",991,"x","x","x","x","x",37,"x","x","x","x","x","x","x","x","x","x",17]
    # ]

    # res = _p1()
    res = _p2()
    print(res)