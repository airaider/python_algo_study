#https://leetcode.com/problems/longest-substring-without-repeating-characters/

#투포인터
import collections
def solution(s):
    used = {}
    max_len = start = 0
    for i, c in enumerate(s):
        if used and c in used:
            start = used[c] + 1
        else:
            max_len = max(max_len, i - start + 1)
        used[c] = i
    print(max_len)


if __name__ == '__main__':
    s= "abcabcbb"
    solution(s)