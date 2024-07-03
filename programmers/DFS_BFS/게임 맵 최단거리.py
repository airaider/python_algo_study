from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    maps[0][0] = 0
    que = deque([(0, 0, 1)])
    while deque:
        x, y, cnt = que.popleft()
        if x == n - 1 and y == m - 1:
            return cnt
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    que.append((nx, ny, cnt + 1))
                    maps[nx][ny] = 0
    return -1


if __name__ == '__main__':
    maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
    answer = 11
    solution(maps)
