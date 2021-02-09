import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    print(scoville)
    cnt=0
    while len(scoville)>=1:
        first = heapq.heappop(scoville)
        print(first)
        if first >= K:
            print(cnt)
            return cnt
        if len(scoville)==0: return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first+(second*2))
        cnt+=1
    return -1


if __name__ == '__main__':
    scoville = [1, 2, 3]
    K = 11
    print(solution(scoville, K))