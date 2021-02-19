def solution(tickets):
    visit = [0 for _ in range(len(tickets))]
    tickets.sort(key=lambda x: x[1])
    path = ['ICN']
    hh=[]
    def dfs(city, path, visit):
        if sum(visit) == len(tickets):
            print(path)
            hh.append(path)
            return

        for i, v in enumerate(tickets):
            if not visit[i] and v[0] == city:
                visit[i] = 1
                path.append(v[1])
                dfs(v[1], path[:], visit)
                visit[i] = 0
                path.pop()

    dfs('ICN', path, visit)
    print(hh)
    return hh



if __name__ == '__main__':
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    solution(tickets)
