def solution(n):
    c = bin(n).count('1')
    for i in range(n+1, 10000001):
        if bin(i).count('1') == c:
            return i


if __name__ == '__main__':
    n = 78
    solution(n)
