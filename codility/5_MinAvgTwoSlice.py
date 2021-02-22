def solution(A):
    # write your code in Python 3.6
    cnt = sum(A[0:2])/2
    answer=0
    for i in range(3, len(A)+1):
        s = A[i-3:i]
        if sum(s)/3 <cnt:
            cnt=sum(s)/3
            answer=i-3
        s = A[i-2:i]
        if sum(s)/2 < cnt:
            cnt=sum(s)/2
            answer = i-2
    print(cnt)
    print(answer)
    pass


if __name__ == '__main__':
    A = [4,2,2,5,1,5,8]
    solution(A)