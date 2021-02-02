import re


def re_solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st


def solution(new_id):

    answer = new_id.lower()

    temp = ''
    for let in answer:
        if let.isalnum() or let in '-_.':
            temp+=let
    answer=temp

    while '..' in answer:
        answer = answer.replace('..', '.')

    answer = answer[1:] if answer[0] == '.' and len(answer)>1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer

    if answer == '': answer='a'
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    while len(answer) <=2:
        answer +=answer[-1]

    print(answer)

    return answer


if __name__ == '__main__':
    new_id = "...!@BaT#*..y.abcdefghijklm"
    solution(new_id)