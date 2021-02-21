import collections

def solution(gems):
    answer = []

    dia = collections.defaultdict()
    need = len(set(gems))
    

    left = start = end = 0
    for right, gem in enumerate(gems, 1):
        if gem in need:
            need.remove(gem)
            kind-=1

        if not kind:
            while left<right and gems[left] not in need:
                need.add(gems[left])
                left+=1

            if not end or right-left <= end-start:
                start, end = left, right
                need.add(gems[left])
                kind+=1
                left+=1
    print(start-1, end-1)

    return answer


if __name__ == '__main__':
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    solution(gems)
    gems = ["AA", "AB", "AC", "AA", "AC"]
    solution(gems)
    gems = ["XYZ", "XYZ", "XYZ"]
    solution(gems)
    gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    solution(gems)