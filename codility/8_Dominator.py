import collections


def solution(A):
    lmt = len(A)//2
    print(lmt)
    for i in collections.Counter(A).items():
        if i[1] > lmt:
            print(i[0])
            print(A.index(i[0]))

    return -1


if __name__ == '__main__':
    A = [3,4,3,2,3,-1,3,3]
    solution(A)
