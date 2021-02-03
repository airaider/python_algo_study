def solution(s):
    answer = []
    words = s.split(" ")
    for word in words:
        temp=''
        for i,v in enumerate(word):
            if i%2==0:
                temp+=v.upper()
            else:
                temp+=v.lower()
            print(temp)
        answer.append(temp)
    print((' ').join(answer))
    return answer


if __name__ == '__main__':
    s = "try hello world"
    solution(s)