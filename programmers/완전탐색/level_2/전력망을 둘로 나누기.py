def solution(n, wires):
    graph = {i: [] for i in range(1, n + 1)}  # 1부터 n까지의 노드에 대한 빈 리스트 생성

    for v1, v2 in wires:
        graph[v1].append(v2)  # v1에 v2를 연결
        graph[v2].append(v1)

    def dfs(node, parent):
        cnt = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                cnt += dfs(neighbor, node)
        return cnt

    answer = n

    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        cnt = dfs(1, -1)
        graph[v1].append(v2)  # v1에 v2를 연결
        graph[v2].append(v1)
        answer = min(answer, abs(cnt - (n - cnt)))
    return answer


if __name__ == "__main__":
    n = 9
    wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
    result = 3
    solution(n, wires)
