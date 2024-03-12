# https://leetcode.com/problems/group-anagrams/

# 딕셔너리 자료형
import collections


def solution(strs: list[str]):
    anagrams = collections.defaultdict(list)

    print(anagrams.values())


if __name__ == '__main__':
    strs = ["babad", "cbbd"]
    ans = ["bab or aba", "bb"]
    solution(strs)