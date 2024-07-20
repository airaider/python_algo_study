from collections import defaultdict

def solution1(tickets):
    visit = [0 for _ in range(len(tickets))]
    tickets.sort(key=lambda x: x[1])
    path = ['ICN']
    answer = []

    def dfs(path, visit):
        if sum(visit) == len(tickets):
            answer.append(path)

        for i, v in enumerate(tickets):
            if visit[i] == 0 and v[0] == path[-1]:
                visit[i] = 1
                dfs(path[:]+[v[1]], visit)
                visit[i] = 0

    dfs(path, visit)
    return answer[0]

def solution(tickets):
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)

    # 각 출발지에서의 도착지를 알파벳 순으로 정렬
    for start in graph:
        graph[start].sort()
    print(graph)

    def dfs(start, path, visit):
        if len(visit) == len(tickets):
            return path
        for i, v in enumerate(graph[start]):
            print(i,v)




    dfs('ICN', ['ICN'], set())


if __name__ == "__main__":
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    answer = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    solution(tickets)
