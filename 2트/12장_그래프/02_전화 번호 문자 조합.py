# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Nested function, DFS
def solution(digits):

    def dfs(index, path):
        if len(digits) == len(path):
            answer.append(path)
        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)

    dic = {
        "2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"
    }
    if not digits:
        return ""
    answer = []
    dfs(0, "")
    print(answer)


if __name__ == '__main__':
    digits = "23"
    solution(digits)
