# 리스트 변환 O(n^2)
def solution1(palin : str):
    strs = []

    for char in palin:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
        if strs.pop() != strs.pop(0):
            return False
    return True

# 데크 자료형 O(n)
from collections import deque
def solution2(palin : str):
    que = deque()

    for char in palin:
        if char.isalnum():
            que.append(char.lower())

    while len(que) > 1:
        if que.popleft() != que.pop():
            return False
    return True

#슬라이싱
import re
def solution3(palin : str):
    palin = palin.lower()
    #정규식
    palin = re.sub('[^a-z0-9]', '', palin)
    return palin == palin[::-1]


if __name__ == '__main__':

    print(solution1("race a car"))
    print(solution1("A man, a plan, a canal: Panama"))

    print(solution2("race a car"))
    print(solution2("A man, a plan, a canal: Panama"))

    print(solution3("race a car"))
    print(solution3("A man, a plan, a canal: Panama"))
