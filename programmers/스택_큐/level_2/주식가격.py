from programmers.util.test_runner import run_tests
from collections import deque


def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer


def solution1(prices):
    answer = []
    q_prices = deque(prices)
    while q_prices:
        temp = q_prices.popleft()
        time = 0
        for n in q_prices:
            time += 1
            if n < temp: break
        answer.append(time)
    return answer


if __name__ == "__main__":
    run_tests(solution)
