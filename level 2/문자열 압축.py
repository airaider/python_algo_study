

def solution(s):
    print(len(s))
    answer = 99999999
    if len(s) == 1:
        return 1
    for sl in range(1, len(s)//2+1):
        print(sl)
        prev=s[0:sl]
        cnt=1
        line=''
        print(prev)
        for i in range(sl, len(s)+1, sl):

            print(s[i:i+sl])
            if s[i:i+sl] == prev:
                cnt+=1
            else:
                if cnt == 1:
                    line+=prev
                else:
                    line+=str(cnt)+prev
                    cnt=1
            prev = s[i:i+sl]
        line+=prev
        print(line)
        answer = min(answer, len(line))


    print(answer)
    return


if __name__ == '__main__':
    s = "xababcdcdababcdcd"
    solution(s)