# https://adventofcode.com/2021/day/12

from collections import defaultdict, Counter, deque

def _main(p2):
    p = 0
    start = ("start", set(["start"]), None)
    q = deque([start])

    dd = defaultdict(list)
    for i in _input:
        a,b = i.split('-')
        dd[a].append(b)
        dd[b].append(a)

    while q:
        pos, lc, t = q.popleft()
        # print(pos, lc)
        if pos == "end":
            p += 1
            continue
        for y in dd[pos]:
            if not y in lc:
                ns = set(lc)
                if y.lower() == y:
                    ns.add(y)
                q.append((y, ns, t))
            elif y in lc and t is None and y not in ["start", "end"] and p2:
                q.append((y, lc, y))

    return p

if __name__ == '__main__':
    # _input = [
    #     "start-A",
    #     "start-b",
    #     "A-c",
    #     "A-b",
    #     "b-d",
    #     "A-end",
    #     "b-end"
    # ]

    # _input = [
    #     "dc-end",
    #     "HN-start",
    #     "start-kj",
    #     "dc-start",
    #     "dc-HN",
    #     "LN-dc",
    #     "HN-end",
    #     "kj-sa",
    #     "kj-HN",
    #     "kj-dc"
    # ]

    _input = [
        "yb-start",
        "de-vd",
        "rj-yb",
        "rj-VP",
        "OC-de",
        "MU-de",
        "end-DN",
        "vd-end",
        "WK-vd",
        "rj-de",
        "DN-vd",
        "start-VP",
        "DN-yb",
        "vd-MU",
        "DN-rj",
        "de-VP",
        "yb-OC",
        "start-rj",
        "oa-MU",
        "yb-de",
        "oa-VP",
        "jv-MU",
        "yb-MU",
        "end-OC"
    ]

    # res = _main(False)
    res = _main(True)
    print(res)