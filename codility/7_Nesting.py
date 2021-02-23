def solution(S):
    # write your code in Python 3.6
    cnt=0
    for i in S:
        if i =='(':
            cnt+=1
        else:
            if cnt==0:
                return 0
            cnt-=1
    if cnt!=0:
        return 0
    return 1


if __name__ == '__main__':
    S = "(()(())())"
    solution(S)
