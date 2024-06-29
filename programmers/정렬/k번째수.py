def solution(array, commands):
    answer = []
    for c in commands:
        a = sorted(array[c[0]-1:c[1]])
        answer.append(a[c[2]-1])
    return answer


def solution1(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]


if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    solution(array, commands)