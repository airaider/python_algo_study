import math
import heapq


def solution(arr):
    answer = 0
    heapq.heapify(arr)
    while arr:
        a = heapq.heappop(arr)
        if len(arr)==0:
            print(a)
            return a
        b = heapq.heappop(arr)
        heapq.heappush(arr,(a*b)//(math.gcd(a,b)))

    return answer


if __name__ == '__main__':
    arr = [2,6,8,14]
    solution(arr)