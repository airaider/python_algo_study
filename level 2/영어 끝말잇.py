def solution(n, words):
    answer = []
    dict=[]
    last = words[0][-1]
    print(last)
    dict.append(words[0])
    for i,v in enumerate(words[1:]):
        print(v)
        if v in dict or v[0]!=last:
            return [(i + 1) % n + 1, (i + 1) // n + 1]
        else:
            dict.append(v)
            last = v[-1]

    return [0,0]


if __name__ == '__main__':
    n=3
    words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    solution(n,words)