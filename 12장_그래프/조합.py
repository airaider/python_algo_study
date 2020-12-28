# https://leetcode.com/problems/combinations/

# Nested function, DFS
def solution(n, k):
    results = []
    visit = [0]*k

    def dfs(idx, cnt):
        if cnt == k:
            results.append(visit[:])
            return
        for i in range(idx, n+1):
            visit[cnt] = i
            dfs(i + 1, cnt + 1)
    dfs(1, 0)
    print(results)

# itertools 내장 함수
import itertools
def combination(n, k):
    answer = list(itertools.combinations(range(1, n+1), k))
    answer2 = list(map(list, itertools.combinations(range(1, n+1), k)))
    print(answer2)


if __name__ == '__main__':
    n = 4
    k = 2
    solution(n, k)
    combination(n, k)
