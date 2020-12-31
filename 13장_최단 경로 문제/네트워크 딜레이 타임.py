# https://leetcode.com/problems/network-delay-time/

import collections
import heapq
def solution(times, N, K):
    print(times, N, K)
    graph = collections.defaultdict(list)
    for u,v,w in times:
        graph[u].append([v,w])

    Q = [(0,K)]
    dist = collections.defaultdict(int)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v,w in graph[node]:
                alt = time+w
                heapq.heappush(Q, (alt, v))
    print(dist)
    if len(dist) == N:
        return max(dist.values())
    return -1


if __name__ == '__main__':
    times = [[2,1,1],[2,3,1],[3,4,1]]
    N = 4
    K = 2
    solution(times, N, K)