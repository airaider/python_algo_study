def solution(n,a,b):
    cnt = 0
    while a!=b:
        cnt+=1
        a = (a+1)//2
        b = (b+1)//2
    print(cnt)
    return cnt


if __name__ == '__main__':
    N=8
    A=4
    B=7
    solution(N,A,B)