from programmers.util.test_runner import run_tests

from collections import defaultdict


def solution(genres, plays):
    cnt = defaultdict(int)
    info = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        cnt[g] += p
        info[g].append((i, p))
    cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    answer = []
    for genre in cnt:
        sorted_plays = sorted(info[genre[0]], key=lambda x: (-x[1], x[0]))
        answer.extend(i[0] for i in sorted_plays[:2])
    return answer


if __name__ == "__main__":
    run_tests(solution)
