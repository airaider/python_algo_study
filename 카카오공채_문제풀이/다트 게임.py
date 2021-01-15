def solution(dartResult):
    print(dartResult)
    nums = []
    temp = ""
    for s in dartResult:
        if s == 'S':
            
            nums.append(temp)
            temp=""
        elif s == 'D':
            nums.append(temp)
            temp = ""
        elif s == 'T':
            nums.append(temp)
            temp = ""
        else:
            temp+=s
    print(nums)
    return

if __name__ == '__main__':
    dartResult = "1S2D*3T"
    solution(dartResult)