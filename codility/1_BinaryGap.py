def solution(N):
    # write your code in Python 3.6

    print(bin(N)[2:])

    cnt=0
    flag=0
    answer=[]
    for i in bin(N)[2:]:
        if i =='1':
            if cnt:
                answer.append(cnt)
            cnt = 0
        else:
            cnt+=1
    print(answer)
    print(max(answer))
    pass


if __name__ == '__main__':
    N = 529
    solution(N)