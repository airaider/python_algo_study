# https://leetcode.com/problems/reconstruct-itinerary/

import collections
def solution(tickets):
    print(tickets)
    graph = collections.defaultdict(list)

    for start, arive in sorted(tickets, reverse=True):
        graph[start].append(arive)
    print(graph)

    def dfs(town):
        while graph[town]:
          dfs(graph[town].pop())
        path.append(town)

    path=[]
    dfs('JFK')
    print(path[::-1])



if __name__ == '__main__':
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    solution(tickets)