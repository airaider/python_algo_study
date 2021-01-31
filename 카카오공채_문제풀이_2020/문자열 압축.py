

def solution(s):
    print(len(s))
    answer = 99999999
    if len(s) == 1:
        return 1
    for sl in range(1, len(s)//2+1):
        ret=''
        cnt = 1
        prev = s[:sl]
        for i in range(sl, len(s)+sl, sl):
            cur = s[i:i+sl]
            if prev == cur:
                cnt += 1
            else:
                if cnt != 1:
                    ret = ret+str(cnt)+prev
                else:
                    ret = ret+prev
                prev = s[i:i+sl]
                cnt=1
        answer = min(answer, len(ret))
    print(answer)
    return


if __name__ == '__main__':
    s = "a"
    solution(s)