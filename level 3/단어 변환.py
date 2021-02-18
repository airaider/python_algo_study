from collections import deque


def solution(begin, target, words):
    answer = 0
    que = deque([begin])
    visit = []

    while que:
        answer += 1
        for _ in range(len(que)):
            cur = que.popleft()
            for word in words:
                if word not in visit:
                    cnt = 0
                    for i, j in zip(cur, word):
                        if i != j: cnt += 1
                    if cnt == 1:
                        if word == target:
                            print(answer)
                            return answer
                        que.append(word)
                        visit.append(word)
    return 0


if __name__ == '__main__':
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution(begin, target, words)
