import collections

def solution(N, road, K):
    dist = {i: float('inf') if i != 1 else 0 for i in range(1, N + 1)}
    nodes = {}
    for v1, v2, d in road:
        nodes[v1] = nodes.get(v1, []) + [(v2, d)]
        nodes[v2] = nodes.get(v2, []) + [(v1, d)]
    que = collections.deque([1])

    print(dist)
    print(nodes)

    while que:
        cur_node = que.popleft()
        for nxt_node, d in nodes[cur_node]:
            if dist[nxt_node] > dist[cur_node]+d:
                dist[nxt_node] = dist[cur_node] + d
                que.append(nxt_node)

    print(que)
    print(dist)
    answer = 0
    print(len([True for d in dist.values() if d<=K]))
    for d in dist.values():
        if d<=K: answer+=1
    return answer


if __name__ == '__main__':
    N = 5
    road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
    K = 3
    solution(N, road, K)
    # N = 6
    # road = 	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
    # K = 4
    # solution(N, road, K)