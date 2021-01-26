import collections

def solution(s,t):
    print(s,t)
    need = collections.Counter(t)
    missing = len(t)

    left = start = end = 0

    print(need)
    print(missing)
    for right, char in enumerate(s, 1):

        missing -= need[char] > 0

        # need[char]-=1
        # if missing == 0:
        #     while left<right and need[s[left]]<0:
        #         need[s[left]]+=0
        #         left+=1

    return

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    solution(s,t)
