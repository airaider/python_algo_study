def solution(n):
    ls = list(str(n))
    ls.sort(reverse=True)
    return int(''.join(ls))


if __name__ == '__main__':
    n=118372
    solution(n)