def dfs(city, path, visit, tickets):
    if sum(visit) == len(tickets):
        return path

    for i, v in enumerate(tickets):
        if not visit[i] and v[0] == city:
            visit[i] = 1
            path.append(v[1])
            ret = dfs(v[1], path, visit, tickets)
            visit[i] = 0
            path.pop()
            if ret:
                return ret


def solution(tickets):
    visit = [0 for _ in range(len(tickets))]
    tickets.sort(key=lambda x: x[1])
    path = ['ICN']
    answer = dfs('ICN', path, visit, tickets)
    return answer



if __name__ == '__main__':
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    solution(tickets)
    print(solution(tickets))
