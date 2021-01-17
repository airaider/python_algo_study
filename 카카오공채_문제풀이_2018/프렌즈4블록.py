def solution(m, n, board):
    board = [list(x) for x in board]
    print(board)
    see(m, n, board)

    matched = True
    while matched:
        matched = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == \
                        board[i + 1][j] == \
                        board[i][j + 1] == \
                        board[i + 1][j + 1] != '#':
                    matched.append([i, j])
        for i,j in matched:
            print(i,j)
            board[i][j] = board[i][j+1] = board[i+1][j] = board[i+1][j+1] = "#"
        see(m, n, board)
        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i + 1][j] == '#':
                        board[i + 1][j], board[i][j] = board[i][j], '#'
        see(m, n, board)
    see(m, n, board)
    print(sum(x.count('#') for x in board))
    return

def see(m, n, board):
    for i in range(m):
        for j in range(n):
            print(board[i][j], end="")
        print()
    print("============================")

if __name__ == '__main__':
    n = 6
    m = 6
    board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
    solution(m, n, board)
