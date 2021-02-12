import collections

def solution(str1, str2):
    answer = 0
    dict1=[]
    dict2=[]
    str1=str1.lower()
    str2= str2.lower()
    for i in range(len(str1)-1):
        if str1[i:(i+2)].isalpha():
            dict1.append(str1[i:(i+2)])
    for i in range(len(str2)-1):
        if str2[i:(i+2)].isalpha():
            dict2.append(str2[i:(i+2)])
    s1 = collections.Counter(dict1)
    s2 = collections.Counter(dict2)
    union = sum((s1 | s2).values())
    inter = sum((s1 & s2).values())
    print(union, inter)
    if union == 0:
        return 65536
    jaccard = inter/union
    jaccard+=65536
    return int(jaccard)


if __name__ == '__main__':
    str1 = 'E=M*C^2'
    str2 = 'E=M*C^2'
    solution(str1, str2)