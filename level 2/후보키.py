import itertools

def solution(relation):
    answer = 0

    for r in relation:
        print(r)

    temp = list(map(list, zip(*relation)))
    print(temp)

    candidates = []
    for i in range(1, len(temp)+1):
        candidates.extend(itertools.combinations(range(len(temp)), i))
    print(candidates)

    final = []

    for key in candidates:
        tmp = [tuple([item[k] for k in key]) for item in relation]
        print(tmp)
        print(len(set(tmp)))
        if len(set(tmp)) == len(relation):
            final.append(key)

    print(final)
    result = set(final[:])
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                result.discard(final[j])



    print(result)




    return answer


if __name__ == '__main__':
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    solution(relation)