def solution1(n):
    dp=[0]*(n+1)
    print(dp)
    dp[1]=1
    if n==1:
        return 1
    for i in range(2, n+1):
        if i%2==0:
            dp[i]=dp[i//2]
        else: dp[i]=dp[i-1]+1
    print(dp)
    print(dp[n])
    return


def solution(n):
    print(bin(n)[2:].count('1'))
    return


if __name__ == '__main__':
    N = 5000
    solution(N)