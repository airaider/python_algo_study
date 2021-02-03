def solution(s, n):
    answer = ''
    for char in s:
        if char == ' ':
            answer+=' '
            continue
        if char.isupper():
            move = (ord(char)-ord('A')+n)%26 + ord('A')
        elif char.islower():
            move = (ord(char)-ord('a')+n)%26 + ord('a')
        answer+=chr(move)
    print(answer)
    return answer


if __name__ == '__main__':
    s = 'a B z'
    n = 4
    solution(s,n)