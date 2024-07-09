from programmers.util.test_runner import run_tests


def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            cnt[0]+=1
        if answers[i] == b[i%8]:
            cnt[1]+=1
        if answers[i] == c[i%10]:
            cnt[2]+=1
    for i in range(3):
        if cnt[i] == max(cnt):
            answer.append(i + 1)
    return answer


def solution1(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    scores = [sum(answer == pattern[i % len(pattern)] for i, answer in enumerate(answers)) for pattern in patterns]

    max_score = max(scores)
    return [i + 1 for i, score in enumerate(scores) if score == max_score]


if __name__ == "__main__":
    run_tests(solution)
