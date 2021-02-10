def solution1(s):
    answer = []
    s = s.replace("{{", '').replace("}}", '').split('},{')
    print(s)
    s.sort(key=lambda x:len(x))
    for i in s:
        for el in i.split(','):
            if int(el) not in answer:
                answer.append(int(el))
    print(answer)
    return answer


import re
import collections
def solution(s):
    answer = []
    s = collections.Counter(re.findall('\d+', s))
    print(s)
    print(list(map(int, [k for k,v in sorted(s.items(), key=lambda x:x[1], reverse=True)])))

    return answer


if __name__ == '__main__':
    s = '{{4,2,3},{3},{2,3,4,1},{2,3}}'
    solution(s)