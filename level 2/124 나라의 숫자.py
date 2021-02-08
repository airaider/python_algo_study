def solution(n):
    answer = ''
    remain = -1
    while n:
        remain = n%3
        n = n//3
        if remain == 0:
            answer='4'+answer
            n-=1
        elif remain == 1:
            answer='1'+answer
        elif remain == 2:
            answer='2'+answer

    return answer[::-1]


def change124(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


if __name__ == '__main__':
    n = 12
    for i in range(1, n+1):
        print(str(i)+": "+solution(i))
