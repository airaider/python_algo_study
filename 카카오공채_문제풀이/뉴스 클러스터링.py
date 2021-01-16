import re
import collections

def solution(str1, str2):
    str1s = [
        str1[i:i+2].lower()
        for i in range(len(str1)-1)
        if re.findall('[a-z]{2}', str1[i:i+2].lower())
    ]
    str2s = [
        str2[i:i + 2].lower()
        for i in range(len(str2) - 1)
        if re.findall('[a-z]{2}', str2[i:i + 2].lower())
    ]
    s1 = collections.Counter(str1s)
    s2 = collections.Counter(str2s)
    print(s1, s2)
    intersection = sum((s1 & s2).values())
    union = sum((s1 | s2).values())
    if union == 0 :
        return 65536
    jaccard = 1 if union==0 else intersection/union
    print(int(jaccard*65536))
    return int(jaccard*65536)

if __name__ == '__main__':
    str1 = "FRANCE"
    str2 = "french"
    solution(str1, str2)