import itertools


def solution(numbers):
    answer = set()
    for a,b in itertools.combinations(numbers, 2):
        answer.add(a+b)
    return sorted(answer)


if __name__ == '__main__':
    numbers = [2,1,3,4,1]
    solution(numbers)