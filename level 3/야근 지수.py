import heapq


def solution(n, works):
    answer = 0
    heap = []

    for w in works:
        heapq.heappush(heap, (-w,w))
    print(heap)

    for _ in range(n):
        a = heapq.heappop(heap)[1]-1
        heapq.heappush(heap, (-a, a))
    print(heap)

    for h in heap:
        if h[1]<0:continue
        answer+=h[1]**2
    print(answer)

    return answer


if __name__ == '__main__':
    n = 4
    works = [4,3,3]
    solution(n, works)