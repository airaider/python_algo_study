# https://leetcode.com/problems/group-anagrams/


def solution(s: str):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i),
                     expand(i, i + 1),
                     key=len
                     )
    return result


if __name__ == '__main__':
    strs = ["babad", "cbbd"]
    ans = ["bab or aba", "bb"]
    for s in strs:
        solution(s)
