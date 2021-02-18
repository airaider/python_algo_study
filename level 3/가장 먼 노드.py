import collections


def solution(n, edge):
    answer = 0
    node = collections.defaultdict(list)
    visit = [0 for _ in range(n+1)]
    print(visit)
    for e in edge:
        node[e[0]].append(e[1])
        node[e[1]].append(e[0])
    print(node)

    que = collections.deque([1])
    print(que)
    visit[1]=1
    while que:
        answer=len(que)
        print(que)
        for _ in range(len(que)):
            curr = que.popleft()
            for val in node[curr]:
                if not visit[val]:
                    visit[val]=1
                    que.append(val)
    print(answer)
    return answer


if __name__ == '__main__':
    n = 6
    edge = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    solution(n, edge)