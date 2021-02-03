def solution(num):
    cnt=0
    while num!=1 and cnt<=500:
        print(num)
        if num%2==0: num=num/2
        else: num=num*3+1
        cnt+=1
    if cnt > 500: return -1
    return cnt

if __name__ == '__main__':
    n = 6
    solution(n)