import collections


def solution(s,k):
    left = right = 0
    cnt = collections.Counter()
    print(cnt)

    for right in range(1,len(s)+1):
        cnt[s[right-1]]+=1
        print(cnt)
        max_char_n = cnt.most_common(1)[0][1]
        print(max_char_n)
        if right-left-max_char_n>k:
            cnt[s[left]]-=1
            left += 1
    print(right, left)
    return

if __name__ == '__main__':
    s = "AAABBC"
    k = 2
    solution(s,k)
