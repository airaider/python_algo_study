#https://leetcode.com/problems/reorder-data-in-log-files/

#투 포인터
def solution(logs : list[str]):
    digits = []
    letters = []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
#key는 x.split()[1:] 식별자를 제외한 [1:] 이후를 키로 지정, 만약 동일시에는 x.split()[0] 식별자로 순서 지정
    letters.sort(key =lambda x: (x.split()[1:], x.split()[0]))
    print(letters+digits)

if __name__ == '__main__':
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    solution(logs)