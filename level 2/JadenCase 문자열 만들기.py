def solution1(s):
    answer = ''
    words = s.split()
    print(words)
    for w in words:
        w = w.replace(' ', '')
        answer+=w[0].upper()+w[1:].lower()+" "
    print(answer[:-1])
    return answer[:-1]


def solution(s):
    flag = True
    answer=''
    for i in s:
        if i == ' ':
            flag=True
        elif i.isalpha() and flag:
            i = i.upper()
            flag = False
        else :
            i = i.lower()
            flag = False
        answer+=i

    return answer


if __name__ == '__main__':
    s = '3people unFollowed me	'
    solution(s)