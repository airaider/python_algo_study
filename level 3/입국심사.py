def solution(n, times):

    left = 0
    right = n*times[-1]
    answer = right

    while left<=right:
        print(left, right)
        mid = (left+right)//2
        print(mid)
        cnt=0
        for t in times:
            cnt+=mid//t
        print(cnt)
        if cnt >= n:
            if answer>mid:
                answer=mid
            right=mid-1
        else:
            left = mid+1
    print(mid)
    print(answer)
    return answer


if __name__ == '__main__':
    n = 6
    times = [7,10]
    solution(n, times)