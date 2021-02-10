def solution(s):
    answer = 0
    cnt=0

    while s!='1':
        cnt+=1
        print(s)
        answer+=s.count('0')
        s = s.replace('0', '')
        s = format(int(len(s)), 'b')
    print(cnt)
    print(answer)
    return [cnt, answer]


if __name__ == '__main__':
    s = "01110"
    solution(s)