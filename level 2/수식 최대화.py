from itertools import permutations
import re


def solution1(expression):
    answer = []
    expressions = set(re.findall("\D", expression))

    print(expressions)
    prior = permutations(expressions)
    for p in prior:
        print(p)
        temp = re.compile("(\D)").split('' + expression)
        print(temp)
        for exp in p:
            print(exp)
            while exp in temp:
                idx = temp.index(exp)
                temp = temp[:idx-1]+[str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]
        answer.append(abs(int(temp[0])))
    print(answer)

    return max(answer)


def solution(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)',expression)
    print(op)
    print(ex)

    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)

if __name__ == '__main__':
    expression = "100-200*300-500+20"
    solution(expression)