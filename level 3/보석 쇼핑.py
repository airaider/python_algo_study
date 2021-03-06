import collections


def solution(gems):
    n = len(set(gems))
    answer = [0, len(gems)-1]
    start = end = 0
    dic1 = collections.defaultdict(int)
    dic1[gems[0]]=1

    while start<len(gems) and end<len(gems):
        print(start, end)
        print(gems[start:end + 1])
        if len(dic1) == n:
            if end-start<answer[1]-answer[0]:
                answer[1]=end
                answer[0]=start
            dic1[gems[start]]-=1
            if dic1[gems[start]]==0:
                del dic1[gems[start]]
            start += 1
        else:
            end+=1
            if end==len(gems):
                break
            dic1[gems[end]]+=1
    print(answer)
    print(answer[0]+1, answer[1]+1)
    return [answer[0]+1, answer[1]+1]


if __name__ == '__main__':
    # gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    # solution(gems)
    gems = ["AA", "AB", "AC", "AA", "AC"]
    solution(gems)
    # gems = ["XYZ", "XYZ", "XYZ"]
    # solution(gems)
    # gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    # solution(gems)