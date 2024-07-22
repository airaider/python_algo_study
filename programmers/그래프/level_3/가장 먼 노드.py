from collections import defaultdict, deque


def solution(n, vertix):
    graph = defaultdict(list)
    for i, j in vertix:
        graph[i].append(j)
        graph[j].append(i)

    visited = set()
    queue = deque()
    queue.append(1)
    visited.add(1)
    cnt = -1
    while queue:
        cnt = len(queue)
        for _ in range(len(queue)):
            v = queue.popleft()
            for e in graph[v]:
                if e not in visited:
                    queue.append(e)
                    visited.add(e)
    return cnt


if __name__ == '__main__':
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    answer = 3
    solution(n, vertex)
