from programmers.util.test_runner import run_tests

from itertools import permutations


def solution(k, dungeons):
    n = len(dungeons)
    case = list(permutations(range(n)))
    answer = 0
    for c in case:
        cnt = 0
        K = k
        for i in c:
            if K < dungeons[i][0]:
                continue
            else:
                K -= dungeons[i][1]
                cnt += 1
        answer = max(answer, cnt)
    return answer


if __name__ == "__main__":
    k = 80
    dungeons = [[80, 20], [50, 40], [30, 10]]
    result = 3
    solution(k, dungeons)
