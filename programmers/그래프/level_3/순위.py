from collections import defaultdict, deque


def solution(n, results):
    win = defaultdict(list)
    lose = defaultdict(list)
    for w, l in results:
        win[w].append(l)
        lose[l].append(w)

    def dfs(graph, start, visited):
        cnt = 0
        visited.add(start)
        for v in graph[start]:
            if v not in visited:
                cnt += 1 + dfs(graph, v, visited)
        return cnt

    win_relations = {}
    lose_relations = {}
    answer = 0
    for i in range(1, n + 1):
        win_relations[i] = dfs(win, i, set())
        lose_relations[i] = dfs(lose, i, set())
        if win_relations[i] + lose_relations[i] == n - 1:
            answer += 1
    return answer


if __name__ == '__main__':
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    answer = 2
    solution(n, results)
