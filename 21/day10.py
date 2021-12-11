# https://adventofcode.com/2021/day/10

def _main():
    scores = []

    for li in _input:
        err = 0
        score = 0
        queue = []
        adds = []
        for c in li:
            if c in lefts:
                queue.append(c)
            elif c in rights:
                if len(queue) >= 1:
                    if c == pairs[queue[-1]]:
                        queue.pop()
                    else:
                        err += errs[c]

        if err <= 0:
            for q in queue[::-1]:
                adds.append(pairs[q])
            for a in adds:
                score *= 5
                score += compscrs[a]

            scores.append(score)

    scores.sort()
    mid = int((len(scores) - 1)/2)
    print(scores)
    return scores[mid]

if __name__ == '__main__':
    lefts = "([{<"
    rights = ")]}>"
    pairs = {"(":")", "[":"]", "{":"}", "<":">"}
    errs = {")":3, "]":57, "}":1197, ">":25137}
    compscrs = {")":1, "]":2, "}":3, ">":4}

    # _input = [
    #     "[({(<(())[]>[[{[]{<()<>>",
    #     "[(()[<>])]({[<{<<[]>>(",
    #     "{([(<{}[<>[]}>{[]{[(<()>",
    #     "(((({<>}<{<{<>}{[]{[]{}",
    #     "[[<[([]))<([[{}[[()]]]",
    #     "[{[{({}]{}}([{[{{{}}([]",
    #     "{<[[]]>}<{[{[{[]{()[[[]",
    #     "[<(<(<(<{}))><([]([]()",
    #     "<{([([[(<>()){}]>(<<{{",
    #     "<{([{{}}[<[[[<>{}]]]>[]]"
    # ]

    _input = [
        "{([[[(<<[{[[[[(){}][()]][({}())]]]<{((<>[]){[]<>})({()()}(<>[]))}<{{{}()}{[]()}}>>})[<(<[[<><>][{}{",
        "([(<(((<[({{({(){}}<{}()>)((<>{})[{}<>})}}[{[(<>())[[]]]{{[][]}(<><>)}}{<<{}()>([]())>([<>][{}])}])](<[{[",
        "{{[[<[<(<<<{((<>[])([]<>))(<{}><()[]>)}[(((){}){<>[]})<{(){}}<<>[]>>]>{[{{<>{}}<()<>>}<<<>[]>([]<>)>][",
        "<[{<(({([[([({{}[]}{<><>})<<[]{}>>]<<<{}{}>((){})><{{}()}<{}[]>>>)](([<([]{})<{}<>>>(<[][]>{()()})",
        "{{<(([<[[{<{({{}<>}({}()))<[<>[]](<>[])>}><[(((){})){[()]<<>[]>}][{{<><>}(<>{})}<<()[]>({}())>]>}<[{[(()<>)",
        "[<{{{({{[<([<{<><>}{<>{}}><<[][]>[{}<>]>]({<[]{}>[[]{}]}{([]())([][])})){<{[[][]]([]())}>([[[",
        "{[<[<<([[<(<<<<>>({})>><({(){}}(<>{}))[{()()}(()[])]>}[<({[]})<[()[]](<>{})>>[<({}{})[()<>]><{(){}}>]]>",
        "[(<({{<[{<(<((<><>)<[]<>>)({<><>}<<>()>)><<<()<>>[()()]>{<<>{}>[()<>]}>){{[([]{})<<><>>]([<",
        "<<{{<{<{([{(<{<><>}>((()[])<<>{}>))({<{}>}<[[]()][<><>]>)}<{([[]()]{<>{}})}{(<<>()>{<>{}})[{<><>}{<><>}]}>]",
        "{(<{<({{([[{<({})[()()]><[{}<>][{}[]]>}<<<[]{}>[<>()]>({{}{}}[{}[]])>]<({[[][]]({}())}[(()[]](<",
        "<[<{[<<[(((<([()()]<()()>]([()[]][{}{}])>)[[[{<>}[<>[]]]][(<()()><<>>)<<{}{}>{<>}>]])([(<({}<>)[()()]>",
        "(<<{{([<[<[<[{[]()}[{}<>]]<(<>[])[{}]>><[{()[]}[()[]]]<([]<>)(()())>>]{{{{()<>}{()()}}[(<><",
        "<[([(<[[[(<[(<{}()>{()()})<<()[]>{(){}}>]><<({[]<>}<{}{}>)[{[][]}{[]{}}]>{<{()()}(()[])>{[<><>",
        "[[([[({{{[[(<<()()>[<>[]]>)<[<<>{}>]([[]()][(){}])>]<(<{()<>}[[][]]>(([]{})[[]()]))[<({}[])",
        "<<{[({<[[[[[{<<>()>{<>{}}}[<()()>]](<<{}<>>{{}<>]><[{}<>]<()<>>>)][((<[]{}>[[]])<{{}()}>)[((<>{}))<<<>{}>(",
        "[[<[[<<(({{<({[]<>}([][]))>{([[]()]{{}<>}){[[]{}][()<>]}}}({{({}()}[[][]]}(((){}){<>})}(<[{}<>]{()()}>",
        "{[{<[[(({<({[{()[]}[[][]]]}(({<><>}<{}[]>)))>}{[{(<{[]{}}{{}[]}>{<<><>>})}<{{[[][]]{<>()>}}<{",
        "{[({<{<{[[([[<()<>}{[]<>}][<<>[]>([])]])]([({{[]()}({}())}([<>()](<><>)))])]{{<[<<[]<>>(()())>(<<>()>{<>",
        "({([<({((<({<<()<>>[(){}]>[(<>{}){<>[]}]}){([{{}[]}])([({}()){<><>}]{[<><>]([]())))}><<[([{}[]])](",
        "<{[{<{<<[<<<[(()<>){[][]}]([()<>]({}{}))>{(<{}{}>[<>{}])[{{}()}[(){}]]}><({<[]<>>[<>{}]}{([]<>)<[]{})})<([{}(",
        "<[<<(({<[{{(<[[]<>]<<>()>>([{}<>]{[]()}))}{<(([]<>)<()<>>)[({}[])<[]{}>]><<<{}[]>{{}<>}>({<>[]}[(){}])>}}<(",
        "[[[[[[(((<{<{(()())<<>{}>}>(<[<><>]({}[])})}{{<[()<>]<[]{}>>[{{}<>}[[]()]]}({<<>[]>}[<{}<>",
        "[(({{<{[<[[(<(()())<<>()>>[<<><>><()()>])(<[{}()]><{[]()}<{}{}>>)][<[({}())<{}<>>][({}[])(()[])]>(((",
        "(([<({{<{{[<<{[]()>(<>{})>[[{}]{{}{}}]>{<<[]{}>>[([][])[<><>]]}]<<[<<>[]>({}<>)]({<>[]}<{}{}>)>[{<{}<>>{[]()}",
        "{(<<[{<<{({(<(<>{})(()())><(<>[]){[]<>}>){[(<>[]){[]()}]{[<>()][{}<>]]}}{([[{}()]]((<><>)))[([{}()]([]()))",
        "[{({[[{{[<<{{[{}<>][<>]}([(){}]{<><>})}><(<[()[]][{}{}]><{[]{}}({})>)(<({}[])<()()>>{<{}{}>{[",
        "([(({{<[<(([({{}<>}[[][]])<({}[]){{}()}>]{[[{}[]]][((){})]})<[{{{}<>}([]{})}{{[]<>}}]>)[{{<([]())({})>",
        "<{{{<<(<{<(<{{<>()}}{({}<>)}>)>}((<{[<{}{}>([]<>)]<<[]()>[{}()]>}<{[<><>]<[]{}>}{{(){}}[[]()]}>>[({(()<>)<{}",
        "((<[{<<{{{([[[[][]](<>[])]]{<({}[])([][])]<{{}{}}{()[]}>})}[[{<{<>[]}{<>{}}>}]]}{<[[((()<>)<()[]>){<()>({}[]",
        "({[[{<{{<<([(<[]<>>{<>{}})<{()[]}(<>())>])<[{[<><>]({}{})}][<({}())><{()<>}(<>())>]>>>{{(([",
        "<((<<(<(<<{{{[{}]<()<>>}{[[]<>]{<><>}}}<[[<>{}]{()()}][<()()>{[][]}]>}{[{[{}()][{}{}]}(<{}()>[{}<>])]}>>",
        "(([<({<[[(<(<([]())({}<>)>([{}()]{<>[]}))<{{{}{}}([]{})}<({}{})<{}<>>>>>[{{<<>[]><<>{}>}({{}<>})}{({[]()}(()<",
        "{[((<({[([(([{(){}}{{}()}][<[]()>{(){}}])[[[{}[]]{{}<>}]<{[]{}}>]){(<[<><>][[][]]>)[{{<>{}}((){})>[([]())[",
        "[[<[<{({[({{([()<>]<()()>)}[<<[]()>>]}((({()()})(<{}>[<>()]))[(({}{}){[]}>(([][])<()()>)]))[{<[<[",
        "[<<([((<<(([[({}{})((){})]<({}[])[{}{}]>]<{{<><>}<[]>}>)[<{{<>()}<()()>}{<<>{}>[[]()]}>[(([][])",
        "{(<(<[[((<([{<[][]><()>}[[<>{}]]]<<((){}){[]())>[<()<>>(<>[])]>)<{<[[]][<>{}]>({<><>}[<>()])}({{{",
        "(<{({({<[[((<<{}<>><<>()>>({{}}<<>[])))[<<{}[]><<><>>>{{[]{}}(())}])[<[([]())<<>{}>]>[[[<><",
        "<[{[[{[({{{([<()()><<>[]>])([([]{})(<>())]{([]<>){()[]}})}<{({{}<>}{[]})([()()])}<[[[]<>><<>{}>]<[()()]<(){}",
        "<<[<[{{({(({(<[]()>({}{}))([{}[]][[]()])}{{(()[]){<><>}}([<><>]{{}})})[{[[{}{}]({}())]{<<>{}",
        "{{{[[[[[<(<<{(()[]){()<>}}<<(){}>(()())>>({(()[])}<<[][]>[<>()]>)>)[{[<(<>())>{<(){}>[{}{}]}]",
        "(([<[[{(([([<<<>{}>((){})>[({}{})<()<>>]]([((){})({}())]])[[{[()()][()[]]}([[][]](<>()))][<{()<",
        "([<{{[[{<{[({<()[]>{[]<>}}([()<>]<[]()>))]}>{[<({({}{})})>{{<[<>{}][()<>]>({[]}{[]<>})}{<[[]{}](<>())",
        "[{<<<{{((<{<<{[]()}<<>{}>>{((){}}{()()}}>}{[((()<>){<>})]({{()()}{(){}}}(<<>()>))}><[<{<{}><(",
        "(((<<<<{((((<{<>[]}{<>()}>)(((<>{})(<><>))))))}><<{<(<<<[]{}><[]>><{[]()}{[]())>>{{<{}<>>}{{",
        "{{[{<(({[[[<[[(){}]]><<[{}{}]({}())>{{[][]}[()()]}>]<{<[<>{}][<>{}]>[(()[])<()[]>]}[{<{}<>>({",
        "{[{{[<[(((([{{{}{}}}({<>{}}[[][]])]){[<([]<>)([][])><{()<>}([]())>](<({}<>)<()>>(<()[]>{{}()}))",
        "{{[(<<[<{<{[[<<><>>[()()]]]<(([]<>))<[[]{}]<[]>>>}>}>{{[<<<[()()]({}())>{<{}()>(<>[])}>([[(){}]<{}[]>]({(",
        "[[[<<(<[{<[[<{<>[]}{{}[]}>]{({<>{}}[<>]]<({}{})[<><>]>}]((([{}{}][{}<>]))[({<>()}(<>{}))])",
        "{{((<<[({<<<{[(){}]({}())}([<>{}]<(){}>)>([(()<>)<{}[]>]<<[]{}><<>{}>>)>[[<{<>}((){})>[{()[]}<{}<>>]](",
        "((<<<<(<[{((<[[]{}](<><>)>{(()<>){()[]}}))}{<({(()())[(){}]}[[[]<>]<{}<>>])<([()[]])[{{}{}}{<><>}]>]}][<[{{",
        "[[({<{{([([<{<<>()><()()>}>((<{}<>>{<>{}})[(()<>)[{}[]]])])[{{(([]())[<><>])({<>[]}(<>{}))}[[<[]><<>[]>]({[",
        "[[(<(<[[(<{(({<>()}(<>[])){<<>[]>{()}}){({<>()}((){}))<<{}[]>[<><>]>}}{({<<>[]>[{}<>]})[[{(",
        "({[<({<{<(<({([]<>){{}[]}}<({}{})[{}{}]>){{([]<>){(){}}}(<[]<>>{<><>})}><[[(<>())]{([]<>)}",
        "{{[[[<{<(<{[(({}[])({}{}))<<()<>>>][<[{}{}]{()[]}>(<[]<>>{<><>})]}<{[<<>()>]<([]())<<>()>>}>>)",
        "(({{{<(([[<(<((){})><[[]{}][{}()]>)<{[{}{}]}<(<>[])>>>]])({{{<[<()<>>{()<>}]>([<<>{}>(()())]<<<>{}>{[]}",
        "{{[[[[({<{[{<[()<>]<<><>>>({<>()}<<>{}>)}(({[]<>}([]))<<<><>>[[]<>]>)]<(<<()()>([]<>>>{({}{}){()()}})[[[<><",
        "[<<{[[([(<{[{{[]()}{[][]}}{{[]()}{(){}}}]{{[{}<>]([]<>)}(<{}()><<>()>)}}<[<{{}<>}<[]<>>><[[]{}]([]{})>][{({",
        "[[[<<(({(<<((<{}<>><(){}>)<([]<>)(()[])>)[((<>())<(){}>){{(){}}{<>[]}}]><<({(){}}{{}<>})>{[<[]{}><[]{}>](<()",
        "({({{<[<<<[{{<{}[]>[(){}]}{(<>[]){{}}}}]{[[{[][]}{[]<>}]{(())([]{})}](<({}{})(()())><{<>()}>)}>>>]([({",
        "<[(((<{<{[<{{{[]<>}{<><>}}{([][])[<>()]}][[[()<>]<{}[]>](({}<>)<[]()>)]>][(<{{{}[]}((){})}{{<>{}}({}()",
        "{<{[({<<(<[<([<>]<[]()>)<({}()){()[]}>>([{()[]}[{}{}]])]>(([{[[]<>][[]<>]}[[<>()]<<>()>]>(((()[]){<>{}}){",
        "<(({<{[(<([(<{[]{}}{[]()}>){{(<><>){[][]}}[{{}()}<[][]>]}])>(<{{{[()<>][()<>]}({{}[]}[[]{}])}}(<{{[]{}",
        "{<[<[{{<<<([[[{}[]]{<>[]}](<<>[]>[()()])][(([]<>)]])>([[<{()}{<><>}>[(<>[])<{}()>]]]{<{<[]{}>[[]",
        "([{[[<<<<{<[({[]{}}(<>()))[<{}<>>[[]{}]]](([{}<>]){{[]()}[<>[]]})>[{(([][])[{}[]]){(<><>)(<>[])}}(<{()<>}",
        "<<(([<{[((<[(<(){}>[<><>])[<<>[]><()())]]{<{()[]}(()<>)>}>)[<<{<(){}><{}()>}{[{}<>]<(){}>}>><[<{<>[]}{[][",
        "(<<[<{<(<<({<([]{}){[][]}>{<[][]>{<>{}}}}[(([]())<<><>>){<{}><<>[]>}])(<{[<>[]]}>{<[{}<>}{<>{}}><{<><>}{()[",
        "[[[[{<[{[<(<[(()())<{}[]>][(()())<()>]><{{()()}[<>{}]}[({}()><[]<>>]>)<{{[[]<>]<[][]>}{[<><>]",
        "{{<(({{<{(<([<[][]>(()[])])<<{<><>}<[]<>>><(<>{})>>><{[[[]{}]{<>[]}](<<>{}>(<>[]))}[[<()<>><()<>>]<{()<",
        "<[({<[[[(<{[(<{}()><(){}>)(<[][]><<>{}>)]<<{{}[]}<{}()>>[(<>())<<><>>]>>{<[([]{})[(){}]]{[(",
        "[{<<<({<[[[<{{<>{}}<()<>>}{[[]()][(){}]}>{(({}[])<[]{}>){<()>(()[])}}]<{<({}<>)<{}[]>>[<{}{}><<><>",
        "{<<[(<<<(<[<<{<><>}>({<>()}(()[]))>[([<><>][[]{}])(([]<>))]]>)>[({[<([[][]]({}))<((){}){[]<>}]>[[",
        "([<{<(<<{({<{<(){}>({}<>)}}{<[{}()][()<>]>{<[]<>>{<>[]}}}}<({[{}{}](<>[])}(<[][]>[{}<>]))<",
        "{([<<<<{[<<[[<{}{}><[][]>]<{{}()}[()[]]>]<[(()[]){<>[]}][[[]()][()<>>]>>(<[{<>()}(<><>)]{<<>{}>{",
        "[[([(([[[<[((<()()>)([[]{}]<[]()>))]><{{[[[]{}]([]{})][(()<>)<{}<>>]}([{()<>}]{[<>()][{}[]]})}",
        "<<{<[<<<({{(<<[]>([])>{<{}<>><<><>>}){<<()<>><()<>>><(<>[])<{}<>>}}}{([{[]<>}{<>{}}](<()()>[{}{}]))<{<[]>",
        "[{{(([{[<{<{{<<><>><{}[]>}}{<(<>{}){[]}>[([]{})[[]{}]]}>(({[{}]<()[]>}))}><<[{(<{}[]><[][]>)",
        "[[[<[<[{{[<[{([]())[()[]]}{<{}<>>[()[]]}]<<{[][]}<()[]>>(<{}<>>{[]{}})>>{<<<{}()>><([]<>)[<>()]>>{{(",
        "{{{([{({[((((([][])[[]()])[(<><>)[()[]]])[[[<>[]]{{}<>}]<[{}[]]([][])>]){[[[[][]]<()<>>](<{}<>><{}{}>",
        "<<<[({{(<((<<{{}()]<()>>(<(){}><<>{}>)>(<{<>()}<[][]>><{<><>}{[]()}>))[(<([][])[<><>]>(<()()>{{}",
        "<[(([[(([[({[[[]()]{()()}](<<>{}>)}){<{{<>[]}{{}{}}}{<[]()>[{}{}]}][(<()[]>[<>[]])((<>{}))]}]{[<<<<>",
        "({{[{<[{([[({[(){}]}[{[]{}}<(){}>])<<({})[[]()]>>]<(({(){}}<[]>)<[<>{}}(<>())>)>])}<<<<[[[[]<>][{}()]]",
        "{{{[[([<{({{{<(){}><{}()>}([()()]<<>[]>)}<<[<>()]{{}<>}><<<><>>>>})([(<(()[])({}<>)>([{}<>](<>[]))){(<<>>",
        "<([([[<{{({{[[<>[]]({}[])]}(<({}())><[<>{}]>)}{[(<{}[]>(<>[]))([[]{}]{[]})]({([][])(<>())})}",
        "[({({{[{<{{(([{}]){<{}[]>([][])})({[[][]]<<>[]>}[<()<>><[]>])}<<<<{}{}>{[]()}>({[][]}[()()])>({([][])[<>{}]}[",
        "({<{(<([<[{<{<<>[]>({}{}>}([()<>]<[]<>>)>({{(){}}<<><>>}[({}{})])}]><<[(<<<>{}>([]())>)[[<[]<>>(",
        "<[{<{<<<({[([({}<>){()()}][<()()>(<><>)]){<{()[]}<<>[]>>{{{}()}[<>[]]}}](((<[]()>{<>()})(({}<>)([]{})))({(",
        "<<{<[[[<[<[[({()()}({}[]))[<()()>[()<>]]]]>][{[<<({}<>)[[][]]>{{{}[]}<()[]>)>]<{{[()[]][[]()]}}{<[",
        "<{<{({({[{<{[{()<>}]<<<><>><[]<>>>}[{<[]><(){}>}<{[]{}}(()<>)>]><{<{{}()}{(){}}>{<()<>>{[]()}}}((([]<>)<<>",
        "{(({[([(((<<([()()]<<>[]>)[<<>()>(<>{})]>[<<<><>><()>>]>[((<()()>((){})))[[<()<>><()()>)({{}[]}",
        "<[<[<{<[{[[([[()()]<{}<>>]){[[{}[]][<>()]]{[[]{}][()<>]}}]]<[{((<>())[[][]]>}([[()<>]<[][]>])](({[",
        "((<<[[{<({[([{<><>}[<>{}]]){(([]{}){(){}})}](<({{}()}<()<>>)({[]()}[[][]))>{{{{}()}[[][]]}<(<>{}){<>[]}>}",
        "<{{{[([({{[(<<[]<>>[{}<>]><<[]{}>(())>)<[[<>{}]<{}<>>]<{()}<{}{}>>>]}{{[<(<>{})<[]()>><[(){}]>][{([]())}[<",
        "[{<[<(<<{({[[<[]<>><()()>]([()()]<<>{}>)]}{(<{[]()}([]<>)><{()[]}>){<<[]()><{}<>>>({()}<<>[]>)}})}{",
        "[{(({[{[{(<[(<[]{}>(<><>))]<[{()}({}())]>><<[({}[]){<><>}](<[][]>[()[]])>[[([][])([]<>)](([]{}])]>)}]<[<[",
        "<({[([(<(((({(<>())<{}[]>}[(<>[]){()[]}]))){[([([]{})(<>()]]([()()][{}<>]))<<{{}}(<>[])>{{()",
        "((({{({<{<({[(<>[]){()()}]([{}[]][{}{}])})(<<{[]{}}>{<[]<>>{()[]}}>)><{{{{{}()}}{[{}[]]<<>[]>}",
        "(<[<<[([[{<[<({}()){()}>(<(){}><<><>>)]>{{([()[]]<<>()>)(<[]<>>)}{[{<>[]}[<>()]](<<>()><()[]",
        "((<<({<((<(<({<><>}({}<>))({{}{}}(<>()))>((([]()){(){}})[(()())(()())]>)>){{<([{<>()}(<><>)]<{<>()",
        "(({(<[({({([<{[]()}<<>()>>{(()<>)[[]()]}]{{[()()]((){})}{[{}<>]{(){}}}})}<<<(<()()>[{}{}])<([]{}){{}[]",
        "{({[[{([[[<((<(){}>{{}()})[(<>{})])([[<>[]]<()[]>][(()())<[]{}>]>>]((({[{}<>]<{}{}>})({<{}[]>}{(<>",
        "[[(({<<{[(<<(([][]){{}<>}){[{}[]]({}[])}>(({<><>})<(()<>)[<>()]})>{({[[]{}]((){})}[([]())])})(({([[][]]",
        "<[<{[<<<{[{(<[<>[]]>{{(){}}[[]()]})}[<{[{}{}]}><(<{}()]{{}{}}){({}[])}>]]}>[({{(<({}[])({}<>)>[{{}<>}])}{"
    ]

    res = _main()
    print(res)