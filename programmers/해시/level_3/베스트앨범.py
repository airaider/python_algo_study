from programmers.util.test_runner import run_tests

from collections import defaultdict
def solution(genres, plays):
    cnt = defaultdict(int)
    order = defaultdict(list)
    index=0
    for genre, play in zip(genres, plays):
        cnt[genre] += play
        order[genre].append((index, play))
        index += 1
    sorted_order = sorted(cnt.items(), key=lambda x: (x[1]), reverse=True)
    answer = []
    for i in sorted_order:
        a = sorted(order[i[0]], key=lambda x: (-x[1], x[0]))
        answer.extend(genre[0] for genre in a[:2])
    return answer


if __name__ == "__main__":
    run_tests(solution)
