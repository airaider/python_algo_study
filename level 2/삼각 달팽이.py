def solution(n):
    answer = []
    snail = [[0] * n for _ in range(n)]
    def see():
        for s in snail:
            print(s)
        print("============")

    i = -1
    j = 0
    idx = 1
    cnt = 0
    check = 0

    def dirr(check):
        if check % 3 == 0:
            return i + 1, j
        elif check % 3 == 1:
            return i, j + 1
        else:
            return i - 1, j - 1

    while n:

        i, j = dirr(check)
        print(i, j)
        snail[i][j] = idx
        see()
        idx += 1
        cnt += 1
        if cnt / n == 1:
            check += 1
            cnt = 0
            n -= 1

    for line in snail:
        for i in line:
            if i != 0:
                answer.append(i)
            else: continue
    print(answer)

    return answer


if __name__ == '__main__':
    n = 5
    solution(n)
