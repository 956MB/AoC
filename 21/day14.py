# https://adventofcode.com/2021/day/14

import os

def _main(steps):
    pat = list(_input[0])
    ptr = 0
    
    for s in range(steps):
        # print(s, len(pat), ptr)
        ptr = 0
        while ptr <= len(pat)-2:
            skip = False
            for t in _input[1]:
                check = f"{pat[ptr]}{pat[ptr+1]}"
                if check == t[0]:
                    pat.insert(ptr+1, t[1])
                    skip = True
                    break

            ptr = ptr+2 if skip else ptr+1
        # if s == 1: return s+1, pat

    ch = []
    for c in set(pat):
        ch.append(pat.count(c))
    ch = sorted(ch)

    return ch[-1] - ch[0]

if __name__ == '__main__':
    _input = [
        "NNCB"
        ,
        [
        ["CH","B"],
        ["HH","N"],
        ["CB","H"],
        ["NH","C"],
        ["HB","C"],
        ["HC","B"],
        ["HN","C"],
        ["NN","C"],
        ["BH","H"],
        ["NC","B"],
        ["NB","B"],
        ["BN","B"],
        ["BB","N"],
        ["BC","B"],
        ["CC","N"],
        ["CN","C"]
        ]
    ]

    # _input = [
    #     "OOFNFCBHCKBBVNHBNVCP"
    #     ,
    #     [
    #     ["PH","V"],
    #     ["OK","S"],
    #     ["KK","O"],
    #     ["BV","K"],
    #     ["CV","S"],
    #     ["SV","C"],
    #     ["CK","O"],
    #     ["PC","F"],
    #     ["SC","O"],
    #     ["KC","S"],
    #     ["KF","N"],
    #     ["SN","C"],
    #     ["SF","P"],
    #     ["OS","O"],
    #     ["OP","N"],
    #     ["FS","P"],
    #     ["FV","N"],
    #     ["CP","S"],
    #     ["VS","P"],
    #     ["PB","P"],
    #     ["HP","P"],
    #     ["PK","S"],
    #     ["FC","F"],
    #     ["SB","K"],
    #     ["NC","V"],
    #     ["PP","B"],
    #     ["PN","N"],
    #     ["VN","C"],
    #     ["NV","O"],
    #     ["OV","O"],
    #     ["BS","K"],
    #     ["FP","V"],
    #     ["NK","K"],
    #     ["PO","B"],
    #     ["HF","H"],
    #     ["VK","S"],
    #     ["ON","C"],
    #     ["KH","F"],
    #     ["HO","P"],
    #     ["OO","H"],
    #     ["BC","V"],
    #     ["CS","O"],
    #     ["OC","B"],
    #     ["VB","N"],
    #     ["OF","P"],
    #     ["FK","H"],
    #     ["OH","H"],
    #     ["CF","K"],
    #     ["CC","V"],
    #     ["BK","O"],
    #     ["BH","F"],
    #     ["VV","N"],
    #     ["KS","V"],
    #     ["FO","F"],
    #     ["SH","F"],
    #     ["OB","O"],
    #     ["VH","F"],
    #     ["HH","P"],
    #     ["PF","C"],
    #     ["NF","V"],
    #     ["VP","S"],
    #     ["CN","V"],
    #     ["SK","O"],
    #     ["FB","S"],
    #     ["FN","S"],
    #     ["BF","H"],
    #     ["FF","V"],
    #     ["CB","P"],
    #     ["NN","O"],
    #     ["VC","F"],
    #     ["HK","F"],
    #     ["BO","H"],
    #     ["KO","C"],
    #     ["CH","N"],
    #     ["KP","C"],
    #     ["HS","P"],
    #     ["NP","O"],
    #     ["NS","V"],
    #     ["NB","H"],
    #     ["HN","O"],
    #     ["BP","C"],
    #     ["VF","S"],
    #     ["KN","P"],
    #     ["HC","C"],
    #     ["PS","K"],
    #     ["BB","O"],
    #     ["NO","N"],
    #     ["NH","F"],
    #     ["BN","F"],
    #     ["KV","V"],
    #     ["SS","K"],
    #     ["CO","H"],
    #     ["KB","P"],
    #     ["FH","C"],
    #     ["SP","C"],
    #     ["SO","V"],
    #     ["PV","S"],
    #     ["VO","O"],
    #     ["HV","N"],
    #     ["HB","V"]
    #     ]
    # ]

    clear = lambda: os.system('cls')

    res = _main(10)
    print()
    print(res)