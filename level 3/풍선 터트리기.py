def solution(a):
    answer = 0
    print(a)
    dp = [[0]*len(a) for _ in range(2)]
    print(dp)
    l_min = a[0]

    for i in range(0, len(a)):
        if l_min> a[i]:
            l_min = a[i]
        dp[0][i] = l_min
    print(dp[0])

    r_min = a[-1]
    for i in range(len(a)-1, -1, -1):
        if r_min> a[i]:
            r_min = a[i]
        dp[1][i] = r_min

    print(dp)

    for i,v in enumerate(a):
        if v <= dp[0][i] or v <= dp[1][i]:
            answer+=1
    print(answer)
    return answer

def solution1(a):
    answer = 1
    M = min(a)
    for _ in range(2):
        m = a[0]
        i = 1
        while m != M:
            if m >= a[i]:
                m = a[i]
                answer += 1
            i += 1
        a.reverse()
    return answer



if __name__ == '__main__':
    a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]

    solution(a)