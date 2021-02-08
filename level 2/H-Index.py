def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        if citations[i]>=len(citations)-i:
            print(len(citations)-i)
            return
    return answer


if __name__ == '__main__':
    citations = [3,0,6,1,5]
    solution(citations)