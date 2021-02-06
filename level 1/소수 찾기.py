def solution(n):
    key = [1]*(n+1)
    print(key)
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if key[i]:
            for j in range(i+i, n+1, i):
                print(j)
                key[j] = 0
    print(key)
    print(sum(key)-2)

    return


if __name__ == '__main__':
    n = 10
    solution(n)