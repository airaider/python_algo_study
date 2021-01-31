import collections


def solution(words, queries):
    result = []
    for q in queries:
        Q=len(q)
        cnt = q.count('?')
        ans = 0

        if Q == cnt:
            for word in words:
                if Q == len(word):
                    ans+=1

        elif q[-1]=='?':
            for word in words:
                if Q == len(word) and q[0:Q-cnt] == word[0:Q-cnt]:
                    ans+=1
        elif q[0]=='?':
            for word in words:
                if Q == len(word) and q[cnt:] == word[cnt:]:
                    ans+=1
        result.append(ans)
    print(result)
    return


if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    solution(words, queries)