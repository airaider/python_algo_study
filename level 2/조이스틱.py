def solution(name):
    answer = 0
    limit = len(name)
    visit=[0]*limit
    for i in range(limit):
        dis = min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
        visit[i]=dis
    print(visit)
    cur = 0
    lc = rc = cur
    answer=visit[0]
    visit[0]=0
    while sum(visit)!=0:
        cnt=0
        print(answer)
        while True:
            cnt+=1
            lc-=1
            if lc<0: lc=limit-1
            rc+=1
            if rc>=limit: rc=0

            if visit[rc]!=0:
                answer+=visit[rc]
                answer+=cnt
                visit[rc]=0
                cur=rc
                break
            if visit[lc]!=0:
                answer+=visit[lc]
                answer+=cnt
                visit[lc]=0
                cur=lc
                break
    print(answer)

    return answer


if __name__ == '__main__':
    name = "BBBBAAAABA"
    solution(name)