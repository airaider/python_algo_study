from collections import defaultdict


def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
        lose[result[1]].add(result[0])
        win[result[0]].add(result[1])

    print(win)
    print(lose)

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    print(win)
    print(lose)

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer


if __name__ == '__main__':
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    solution(n, results)
