from programmers.util.test_runner import run_tests
import math


def solution(progresses, speeds):
    stack = []
    for p, s in zip(progresses, speeds):
        stack.append(math.ceil((100 - p) / s))
    last = stack[0]
    cnt = 0
    answer = []
    while stack:
        day = stack.pop(0)
        if day <= last:
            cnt += 1
        else:
            answer.append(cnt)
            last = day
            cnt = 1
    answer.append(cnt)
    return answer


if __name__ == "__main__":
    run_tests(solution)
