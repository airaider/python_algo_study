def solution(key, lock):

    def rotate90(arr):
        return list(zip(*arr[::-1]))

    def attach(x,y,M, rotate_key, map):
        for i in range(M):
            for j in range(M):
                map[x+i][y+j]+=rotate_key[i][j]

    def detach(x,y,M, rotate_key, map):
        for i in range(M):
            for j in range(M):
                map[x+i][y+j]-=rotate_key[i][j]

    def check(board, M, N):
        for i in range(N):
            for j in range(N):
                if board[M + i][M + j] != 1:
                    return False;
        return True

    M = len(key)
    N = len(lock)
    map = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]

    for i in range(N):
        for j in range(N):
            map[M+i][M+j]=lock[i][j]
    rotate_key = key

    for _ in range(4):
        rotate_key = rotate90(rotate_key)
        for x in range(1, N+M):
            for y in range(1, N+M):
                attach(x,y,M, rotate_key, map)
                if check(map, M, N):
                    print("True")
                    return True
                detach(x,y,M, rotate_key, map)
    print("False")
    return False


if __name__ == '__main__':
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    solution(key, lock)