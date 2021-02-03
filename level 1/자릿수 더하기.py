import math

def solution(n):
    answer = 0
    l = len(str(N))
    print(n)
    div = 10 ** (len(str(N))-1)
    print(div)
    for i in range(l):
        answer+=n//div
        n=n%div
        div=div/10

    return answer


if __name__ == '__main__':
    N = 987
    solution(N)