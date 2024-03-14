#https://leetcode.com/problems/reorder-data-in-log-files/

#투 포인터
def solution(logs : list[str]):
    digits = []
    letters = []

    for word in logs:
        if word.startswith("dig"):
            digits.append(word)
        elif word.startswith("let"):
            letters.append(word)
    print(digits)
    print(letters)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    print(letters+digits)

if __name__ == '__main__':
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    solution(logs)