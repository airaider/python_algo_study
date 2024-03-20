#https://leetcode.com/problems/number-of-islands/

#Nested function, DFS
def solution(grid):
    def search(i,j):
        if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0 or grid[i][j]=='0':
            return
        grid[i][j]='0'
        search(i, j+1)
        search(i+1, j)
        search(i-1, j)
        search(i, j-1)

    count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='1':
                count+=1
                search(i, j)
    print(count)



if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    solution(grid)