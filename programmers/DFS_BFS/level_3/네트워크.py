from collections import defaultdict


def solution(n, computers):
    def dfs(node):
        visited[node] = True
        for i in range(n):
            if not visited[i] and computers[node][i]:
                dfs(i)

    visited = [False] * n
    cnt = 0

    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(cnt)
    return cnt


if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    answer = 2
    solution(n, computers)
