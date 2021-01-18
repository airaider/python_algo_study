import collections
import itertools

def solution(relation):
    answer = []
    n_row = len(relation)
    n_col = len(relation[0])
    candidates = []

    for i in range(1, n_col + 1):
        candidates.extend(itertools.combinations(range(n_col), i))

    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == n_row:
            answer.append(keys)
    final = set(answer[:])

    for i in range(len(answer)):
        print("-----------")
        print(answer[i])
        for j in range(i+1, len(answer)):
            if len(answer[i]) == len(set(answer[i]).intersection(set(answer[j]))):
                final.discard(answer[j])

    return len(final)


if __name__ == '__main__':
    relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
    solution(relation)
