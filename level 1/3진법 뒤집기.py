def solution(n):
    answer = 0
    three = ''
    while n >0:
        three += str(n%3)
        n = n//3
    print(int(three, 3))
    return answer


if __name__ == '__main__':
    n = 45
    solution(n)