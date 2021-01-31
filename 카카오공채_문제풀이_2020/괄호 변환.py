

def solution(p):

    def check(line):
        cnt=0
        for l in line:
            if l == '(':
                cnt+=1
            else:
                if cnt==0:
                    return False
                cnt-=1
        return True

    def step(line):
        lc = 0
        rc = 0
        print(line)
        for i, val in enumerate(line):
            if val == '(':
                lc += 1
            else:
                rc += 1
            if lc == rc:
                u = line[0:i + 1]
                v = line[i + 1:]
                return u,v

    def reverse(u):
        return ''.join([')' if s == '(' else '(' for s in u])


    def recursive(string):
        if string=='':
            return ''
        u,v = step(string)
        if check(u):
            return u+recursive(v)
        else:
            return '('+recursive(v)+')'+reverse(u[1:-1])

    return p if check(p) else recursive(p)

if __name__ == '__main__':
    p= "()))((()"
    solution(p)