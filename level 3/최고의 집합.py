def solution(n, s):
    answer = []
    if n>s:
        return [-1]
    start = s//n
    answer = [start for _ in range(n)]

    left = s - start*n
    print(left)

    print(answer)
    idx = 0
    while left:
        answer[idx]+=1
        idx+=1
        left-=1

    if not answer:
        return [-1]
    answer.sort()

    return answer


if __name__ == '__main__':
    n = 2
    s = 9
    solution(n, s)