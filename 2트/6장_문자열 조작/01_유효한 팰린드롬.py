def solution1(palin: str):
    return True


# 데크 자료형 O(n)
from collections import deque


def solution2(palin: str):
    return True


# 슬라이싱
import re


def solution3(palin: str):
    return True


if __name__ == '__main__':
    print(solution1("race a car"))
    print(solution1("A man, a plan, a canal: Panama"))

    print(solution2("race a car"))
    print(solution2("A man, a plan, a canal: Panama"))

    print(solution3("race a car"))
    print(solution3("A man, a plan, a canal: Panama"))
