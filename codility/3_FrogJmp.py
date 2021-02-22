import math

def solution(X,Y,D):
    print(Y-X)
    print(math.ceil((Y-X)/D))

    pass


if __name__ == '__main__':
    X = 10
    Y = 85
    D = 30
    solution(X, Y, D)