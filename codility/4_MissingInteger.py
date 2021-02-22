import collections

def solution(A):
    A.sort()
    s=list(set(A))
    print(s)

    cnt = 1
    for i in s:
        if i ==cnt:
            cnt+=1
    return cnt


if __name__ == '__main__':
    A = [1,3,6,4,1,2]
    solution(A)