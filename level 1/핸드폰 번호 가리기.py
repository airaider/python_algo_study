def solution(phone_number):
    answer = ''
    for i in phone_number[:-4]:
        answer+='*'
    answer+=phone_number[-4:]
    print(answer)
    return answer

def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]


if __name__ == '__main__':
    phone_number = '01033334444'
    solution(phone_number)