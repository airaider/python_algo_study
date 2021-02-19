def solution(dirs):
    answer = 0
    path = set()
    x,y = 0,0
    print(x,y)
    for dir in dirs:
        print(dir)
        nx=x
        ny=y
        if dir == 'U':
            ny=y+1
            if ny>5: continue
            path.add((x, (ny+y)/2))
        elif dir == 'D':
            ny=y-1
            if ny<-5: continue
            path.add((x, (ny+y)/2))
        elif dir == 'R':
            nx=x+1
            if nx>5: continue
            path.add(((nx+x)/2, y))
        elif dir == 'L':
            nx=x-1
            if nx<-5: continue
            path.add(((nx+x)/2, y))
        x=nx
        y=ny
        print(x,y)

    print(path)
    print(len(path))


    return answer


if __name__ == '__main__':
    dirs = "LULLLLLLU"
    solution(dirs)