def solution1(palin: str):
    strs = []
    for c in palin:
        if c.isalnum():
            strs.append(c.lower())

    while len(strs) > 1:
        if strs.pop() != strs.pop(0):
            return False

    return True


# 데크 자료형 O(n)
from collections import deque


def solution2(palin: str):
    strs = deque()
    for c in palin:
        if c.isalnum():
            strs.append(c.lower())

    while len(strs) > 1:
        if strs.pop() != strs.popleft():
            return False
    return True


# 슬라이싱
import re


def solution3(palin: str):
    palin = palin.lower()
    strs = re.sub('[^a-z0-9]', '', palin)
    return strs == strs[::-1]


if __name__ == '__main__':
    print(solution1("race a car"))
    print(solution1("A man, a plan, a canal: Panama"))

    print(solution2("race a car"))
    print(solution2("A man, a plan, a canal: Panama"))

    print(solution3("race a car"))
    print(solution3("A man, a plan, a canal: Panama"))
