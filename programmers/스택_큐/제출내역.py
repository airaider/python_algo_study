from programmers.util.test_runner import run_tests
from collections import deque


def solution(priorities, location):
    deq = deque((i, j) for i, j in enumerate(priorities))
    cnt = 0
    while deq:
        current = deq.popleft()
        if any(current[1] < q[1] for q in deq):
            deq.append(current)
        else:
            cnt += 1
            if current[0] == location:
                return cnt


if __name__ == "__main__":
    run_tests(solution)
