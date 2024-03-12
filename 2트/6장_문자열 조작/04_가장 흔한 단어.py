#https://leetcode.com/problems/most-common-word/

#리스트 컴프리헨션, Counter 객체
import re
import collections
def solution(paragraph : str, banned : list[str]):
    print(paragraph, banned)


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    solution(paragraph, banned)