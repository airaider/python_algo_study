import heapq


def solution(A):
    # write your code in Python 3.6
    heapq.heapify(A)
    if len(A) < 3: return 0

    a = heapq.heappop(A)
    b = heapq.heappop(A)
    while A:
        c = heapq.heappop(A)
        if a + b > c:
            return 1
        a, b = b, c
    return 0


if __name__ == '__main__':
    A = [10, 2, 5, 1, 8, 20]
    solution(A)
