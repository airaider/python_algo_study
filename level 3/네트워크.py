def solution(n, computers):
    visit = [0 for _ in range(n)]

    def search(i):
        visit[i]=1
        for j in range(len(computers[0])):
            if computers[i][j] and not visit[j]:
                search(j)

    cnt=0
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] and not visit[j]:
                search(j)
                cnt+=1
    print(cnt)
    return

if __name__ == '__main__':
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    n = 3
    solution(n, computers)