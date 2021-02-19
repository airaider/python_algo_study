def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[1]=1
    dp[2]=2
    for i in range(3, n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]%1234567


def solution1(n):
    a,b=1,2
    for _ in range(2, n):
        a,b = b,a+b
    print(b)
    


if __name__ == '__main__':
    n=4
    solution1(n)