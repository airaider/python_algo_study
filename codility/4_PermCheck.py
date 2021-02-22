def solution(A):
    A.sort()
    cnt = 1
    for i in A:
        if i!=cnt:
            return 0
        cnt+=1

    return 1


if __name__ == '__main__':
    A = [4,1,3,2]
    solution(A)