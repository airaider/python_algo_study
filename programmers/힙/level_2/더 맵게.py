from programmers.util.test_runner import run_tests

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) >= 2:
        score1 = heapq.heappop(scoville)
        if score1 < K:
            score2 = heapq.heappop(scoville)
            heapq.heappush(scoville, score1 + score2 * 2)
            cnt += 1
        else:
            return cnt
    if len(scoville) == 1 and scoville[0] >= K:
        return cnt
    return -1


if __name__ == "__main__":
    run_tests(solution)
