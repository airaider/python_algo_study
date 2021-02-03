def solution(n):
    return n % sum(int(i) for i in str(n)) == 0


if __name__ == '__main__':
    N = 18
    print(solution(N))