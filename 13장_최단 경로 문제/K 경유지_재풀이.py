# https://leetcode.com/problems/cheapest-flights-within-k-stops/

import collections
import heapq
def solution(n, edges, src, dst, K):

    graph = collections.defaultdict(list)
    for u,v,w in edges:
        graph[u].append([v,w])
    print(graph)

    Q = [(0, src, K)]
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            print(price)
            return
        if k>=0:
            for v,w in graph[node]:
                heapq.heappush(Q, (w+price, v, k-1))
    return -1


if __name__ == '__main__':
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    K = 0
    solution(n, edges, src, dst, K)
