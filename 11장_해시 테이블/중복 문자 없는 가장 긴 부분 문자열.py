#https://leetcode.com/problems/longest-substring-without-repeating-characters/

#투포인터
import collections
def solution(s):
    print(s)
    used = {}
    max_len = start = 0
    for index, char in enumerate(s):
        print(index, char)
        if char in used and start <= used[char]:
            start = used[char]+1
        else:
            max_len = max(max_len, index-start+1)
        used[char]=index
    print(max_len)

if __name__ == '__main__':
    s= "abcabcbb"
    solution(s)