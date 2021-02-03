import math


def solution(n):
    root = math.sqrt(n)
    print(root)
    if n//root == root:
        return (root+1) **2
    return -1


if __name__ == '__main__':
    n=1
    print(solution(n))