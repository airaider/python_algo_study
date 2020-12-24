#https://leetcode.com/problems/valid-parentheses/

#스택
def solution(s : str):
    stack = []
    table = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for char in s:
        if char in table:
            stack.append(table[char])
        elif not stack or stack.pop() != char:
            return False
    return len(stack) == 0


if __name__ == '__main__':
    s = "()"
    solution(s)