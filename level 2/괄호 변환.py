def solution(p):
    def check(var):
        cnt = 0
        for i in var:
            if i == '(':
                cnt += 1
            else:
                if cnt == 0: return False
                cnt -= 1
        return True

    def split(var):
        cnt = 0
        for i, v in enumerate(var):
            if v == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                return var[0:i + 1], var[i + 1:]

    def reverse(var):
        string = ''
        for i in var:
            if i == '(':
                string += ')'
            else:
                string += '('
        return string

    def recursive(string):
        if string == '':
            return ''
        u, v = split(string)
        if check(u):
            return u + recursive(v)
        else:
            return '(' + recursive(v) + ')' + reverse(u[1:-1])

    return p if check(p) else recursive(p)


if __name__ == '__main__':
    p = "()))((()"
    solution(p)
