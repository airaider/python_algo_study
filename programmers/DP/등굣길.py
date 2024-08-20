def solution(m,n,puddles):
    path = [[0 for _ in range(m+1)] for _ in range(n+1)]
    path[1][1]= 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j,i] in puddles:
                path[i][j] = 0
            else:
                path[i][j] += path[i - 1][j] + path[i][j - 1]
    return path[n][m] % 1000000007

if __name__ == '__main__':
    m = 4
    n = 3
    puddles = [[2, 2]]
    solution(m,n,puddles)