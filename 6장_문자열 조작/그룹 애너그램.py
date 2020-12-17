#https://leetcode.com/problems/group-anagrams/

#딕셔너리 자료형
import collections
def solution(strs: list[str]):

    anagrams = collections.defaultdict(list)
    for str in strs:
        anagrams[''.join(sorted(str))].append(str)
    print(anagrams.values())



if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    solution(strs)