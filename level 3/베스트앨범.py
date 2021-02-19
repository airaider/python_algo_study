import collections

def solution(genres, plays):
    answer = []

    music = collections.defaultdict(list)
    score = collections.defaultdict(int)

    idx=0
    for g, p in zip(genres, plays):
        score[g]+=p
        music[g].append((idx, p))
        idx+=1
    score = sorted(score.items(), key=lambda x:x[1], reverse=True)
    for rank in score:
        rank = rank[0]
        music[rank].sort(key=lambda x:(x[1], -x[0]), reverse=True)
        cnt=0
        for m in music[rank]:
            cnt += 1
            answer.append(m[0])
            if cnt==2:break
    print(answer)
    return answer


if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 501, 800, 900]
    solution(genres, plays)