from collections import defaultdict


def solution(n, computers):
    def dfs(node):
        for i in range(n):
            if not visited[i] and computers[node][i]:
                visited[i] = True
                dfs(i)

    visited = [0] * (n)
    cnt = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            cnt += 1
    return cnt


if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    answer = 2
    solution(n, computers)
