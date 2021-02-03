import math

def solution(n, m):
    answer = []
    answer.append(math.gcd(n,m))
    answer.append((n*m)/math.gcd(n,m))
    return answer


if __name__ == '__main__':
    n=3
    m=12
    solution(n,m)