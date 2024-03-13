#https://leetcode.com/problems/group-anagrams/

#딕셔너리 자료형
import collections
def solution(strs: list[str]):

    anagrams = collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)


    print(anagrams.values())



if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    solution(strs)