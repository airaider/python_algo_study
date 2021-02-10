def solution(n):
    answer = 0

    for i in range(1, n//2+1):
        cnt = i
        for j in range(i+1, n+1):
            cnt+=j
            if cnt==n:
                answer+=1
                break
            elif cnt>n:
                break
        print(i)
    print(answer+1)
    return answer+1


if __name__ == '__main__':
    n =15
    solution(n)