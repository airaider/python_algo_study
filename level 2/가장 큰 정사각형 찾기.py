import itertools

def solution(board):
    answer = 0

    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if board[i][j] != 0 and board[i+1][j+1] != 0:
                board[i+1][j+1] = min(board[i][j], board[i+1][j], board[i][j+1])+1

    return max(itertools.chain(*board))**2


if __name__ == '__main__':
    board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
    solution(board)