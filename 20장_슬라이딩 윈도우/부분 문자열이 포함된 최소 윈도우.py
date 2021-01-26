import collections

def solution(s,t):
    print(s,t)
    need = collections.Counter(t)
    missing = len(t)

    print(need)
    print(missing)

    left = start = end = 0

    for right, char in enumerate(s, 1):

        missing -= need[char] > 0
        need[char]-=1

        if missing == 0:
            while left<right and need[s[left]]<0:
                need[s[left]]+=1
                left+=1
            if not end or right-left <= end-start:
                start, end = left, right
                need[s[left]] += 1
                left += 1
                missing+=1
    print(s[start:end])
    return

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    solution(s,t)
