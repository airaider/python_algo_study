def solution(n):
    answer = 0
    a,b = 1,1
    for i in range(n):
        a,b = b,a+b
    print(a%1000000007)

    return answer


if __name__ == '__main__':
    n = 4
    solution(n)