def solution(n, t, m, p):
    answer = ''

    def convert(n, base):
        T = "0123456789ABCDEF"
        q, r = divmod(n, base)  # n을 base로 나눈 몫과 나머지를 튜플형태로 반환
        if q == 0:
            return T[r]
        else:
            return convert(q, base) + T[r]
    s = ''
    i=0
    while len(s)<t*m:
        s+=convert(i, n)
        i+=1
    print(s)
    for i in range(0,len(s), m):
        answer+=s[i:i+m][p-1]
        if len(answer)==t:
            print(answer)
            return answer


if __name__ == '__main__':
    n = 16
    t = 16
    m = 2
    p = 1
    solution(n, t, m, p)