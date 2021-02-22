def solution(S, P, Q):
    # write your code in Python 3.6
    factor = {'A':1, 'C':2, 'G':3, 'T':4}
    answer=[]

    for p,q in zip(P, Q):
        s = S[p:q+1]
        print(s)
        if 'A' in s:
            answer.append(1)
            continue
        if 'C' in s:
            answer.append(2)
            continue
        if 'G' in s:
            answer.append(3)
            continue
        if 'T' in s:
            answer.append(4)
            continue

    print(answer)
    return answer


if __name__ == '__main__':
    S = 'CAGCCTA'
    P = [2,5,0]
    Q = [4,5,6]
    solution(S, P, Q)