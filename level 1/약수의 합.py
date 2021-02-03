import math


def solution(n):
    answer = 0

    if n==0:
        return 0
    print(round(math.sqrt(n)))
    for i in range(1, round(math.sqrt(n))+1):
        if n%i==0:
            print(i, n/i)
            if i == n/i: answer+=i
            else: answer+=(i+n/i)
    print(answer)
    return answer


if __name__ == '__main__':
    n = 25
    solution(n)