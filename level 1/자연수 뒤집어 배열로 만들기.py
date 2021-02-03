def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    print(answer[::-1])
    return answer[::-1]


def solution1(n):
    return list(map(int, reversed(str(n))))


if __name__ == '__main__':
    n=12345
    solution(n)