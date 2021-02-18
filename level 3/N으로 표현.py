def solution(N, number):
    S = [0, {N}]
    print(S)
    if number in S[1]:
        return 1
    for i in range(2,9):
        case_set = {int(str(N)*i)}
        for i_half in range(1, i//2+1):
            for x in S[i_half]:
                for y in S[i-i_half]:
                    print(x,y)
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x)
                    case_set.add(y*x)
                    if x!=0:
                        case_set.add(y//x)
                    if y!=0:
                        case_set.add(x//y)
        if number in case_set:
            print(S)
            print(i)
            return i
        S.append(case_set)
    print(S)

    return -1

if __name__ == '__main__':
    N = 5
    number = 12
    solution(N, number)