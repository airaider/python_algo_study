
def solution(begin, target, words):
    track = [0] * len(words)
    answer = len(words)+1
    def dfs(now, visit):
        nonlocal answer
        if now == target:
            answer = min(answer, sum(1 for i in visit if i == 1))

        for i, word in enumerate(words):
            cnt = sum(1 for i, j in zip(now, word) if i!=j)
            if cnt == 1 and not visit[i]:
                visit[i] = 1
                dfs(word, visit)
                visit[i] = 0
    dfs(begin, track)
    if answer != len(words)+1:
        return answer
    return 0


from collections import deque
def solution(begin, target, words):
    que = deque()
    que.append((begin, 0))
    visited = [False] * len(words)
    while que:
        node, answer = que.popleft()
        if node == target:
            return answer
        for i, word in enumerate(words):
            cnt = sum(1 for i,j in zip(node, word) if i!=j)
            if cnt == 1 and not visited[i]:
                que.append((word, answer+1))
                visited[i] = True
    return 0




if __name__ == "__main__":
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    begin = "hit"
    target = "cog"
    solution(words, begin, target)
