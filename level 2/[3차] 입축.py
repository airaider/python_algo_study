def solution(msg):
    answer = []
    LZW = {}
    for i in range(0, 26):
        LZW[chr(ord('A')+i)]=i+1
    print(LZW)
    cnt = 27
    idx = 0
    rc = 0

    while True:
        rc+=1
        if not msg[idx:idx + rc] in LZW:
            answer.append(LZW[msg[idx:idx+rc-1]])
            LZW[msg[idx:idx+rc]] = cnt
            cnt += 1
            idx+=rc-1
            rc=0
        else:
            if idx+rc-1 == len(msg):
                answer.append(LZW[msg[idx:idx + rc - 1]])
                break

    print(LZW)
    print(answer)
    return answer


if __name__ == '__main__':
    msg = 'KAKAO'
    solution(msg)