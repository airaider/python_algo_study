import math

from programmers.util.test_runner import run_tests

import collections
import itertools
import math


def solution(numbers):
    def check(num):
        if num < 2:
            return False
        if num == 2 or num == 3:
            return True
        if num >= 4:
            for i in range(2, math.floor(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
        return True

    a = list(numbers.strip())
    b = set()
    for i in range(1, len(a) + 1):
        p = list(itertools.permutations(a, i))
        for j in p:
            b.add(int(''.join(j)))
    cnt = 0
    for i in b:
        if check(i): cnt += 1
    return cnt


import itertools
import math


def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def solution1(numbers):
    # 모든 가능한 숫자 조합 생성
    num_set = set()
    for i in range(1, len(numbers) + 1):
        num_set.update(int(''.join(p)) for p in itertools.permutations(numbers, i))

    # 소수 개수 계산 및 반환
    return sum(1 for num in num_set if is_prime(num))

if __name__ == "__main__":
    run_tests(solution)
