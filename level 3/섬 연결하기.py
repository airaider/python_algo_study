def solution(n, costs):
    visit = [i for i in range(n)]
    answer=0
    costs.sort(key=lambda x:x[2])
    print(costs)

    def union(a1, a2):

        def find(a):
            if visit[a]!=a:
                visit[a] = find(visit[a])
            return visit[a]

        r1 = find(a1)
        r2 = find(a2)
        if r1!=r2:
            visit[r2]=r1
            return True
        return False
    cnt=0
    for i in costs:
        if union(i[0], i[1]):
            answer+=i[2]
            cnt+=1
            if cnt==n-1:
                print(answer)
                return answer




if __name__ == '__main__':
    n = 4
    costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    solution(n, costs)