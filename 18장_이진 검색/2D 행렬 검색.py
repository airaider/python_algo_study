import collections
import bisect


def solution1(matrix, target):
    row = 0
    col = len(matrix)-1

    while row <= len(matrix) and col>=0:
        if target == matrix[row][col]:
            print(row, col)
            return True
        elif matrix[row][col]<target:
            row+=1
        elif matrix[row][col]>target:
            col-=1
    return False


def solution2(matrix, target):
    return any(target in row for row in matrix)


if __name__ == '__main__':
    matrix = [
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
    ]
    target = 17
    solution1(matrix, target)
    solution2(matrix, target)
