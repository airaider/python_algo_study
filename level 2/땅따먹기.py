def solution(land):

    def p(map):
        for i in map:
            print(i)
        print("==========")
    p(land)
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]
            p(land)
    return max(land[-1])


if __name__ == '__main__':
    land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
    solution(land)