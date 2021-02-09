def solution(brown, yellow):
    total = yellow + brown
    limit = int(total ** (1 / 2))
    for i in range(3, limit + 1):
        if total % i == 0 and (i - 2) * (total / i - 2) == yellow:
            return [total / i, i]


if __name__ == '__main__':
    brown = 24
    yellow = 24
    print(solution(brown, yellow))
