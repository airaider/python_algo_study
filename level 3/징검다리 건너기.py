def solution(stones, k):
    def check(var):
        cnt=0
        for stone in stones:
            if stone <= var:
                cnt+=1
                if cnt==k:
                    return True
            else:
                cnt=0
        return False

    left = 0
    right = max(stones)
    answer = right
    while left<=right:
        mid = (left+right)//2

        if check(mid):
            if answer>mid:
                answer=mid
            right=mid-1
        else:
            left = mid+1
    print(answer)
    return answer


def solution1(stones, k):
    left, right = min(stones), max(stones)
    while left < right:
        mid = (right + left + 1) // 2
        cnt = 0
        for stone in stones:
            if stone < mid:
                cnt += 1
            if stone >= mid:
                cnt = 0
            if cnt >= k:
                right = mid
                break
        else:
            left = mid
    print(left)
    return left


if __name__ == '__main__':
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    solution(stones, k)
    stones = [1]
    k = 1
    solution1(stones, k)