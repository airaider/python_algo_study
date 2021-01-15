def solution(dartResult):
    print(dartResult)
    nums = []
    answer=0
    temp = ""
    for s in dartResult:
        if s == 'S':
            nums.append(int(temp))
            temp=""
        elif s == 'D':
            nums.append(int(temp)**2)
            temp = ""
        elif s == 'T':
            nums.append(int(temp)**3)
            temp = ""
        elif s == '*':
            print(nums[-1]*2)
            nums[-1]=nums[-1]*2
            if len(nums)>=2:
                print(nums[-2]*2)
                nums[-2] = nums[-2] * 2
            pass
        elif s == '#':
            print(nums[-1]*-1)
            nums[-1] = nums[-1]*-1
            pass
        else:
            temp+=s
    print(nums)
    print(sum(nums))
    print("############################")
    return

if __name__ == '__main__':
    dartResult = "1S2D*3T"
    solution(dartResult)
    dartResult = "1D2S#10S"
    solution(dartResult)
    dartResult = "1D2S0T"
    solution(dartResult)
    dartResult = "1S*2T*3S"
    solution(dartResult)
    dartResult = "1D#2S*3S"
    solution(dartResult)
    dartResult = "1T2D3D#"
    solution(dartResult)
    dartResult = "1D2S3T*"
    solution(dartResult)