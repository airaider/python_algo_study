import collections
import itertools

def solution(food_times, k):
    cnt = 0
    N = len(food_times)
    for _ in range(k):
        if cnt==N:
            cnt = 0
        if food_times[cnt]==0:
            cnt+=1
        if cnt==N:
            cnt = 0
        food_times[cnt] -= 1
        cnt+=1
    print(food_times)
    if cnt==N:
        cnt=1
    else: cnt+=1
    print(cnt)
    return


if __name__ == '__main__':
    food_times = [3,1,2]
    k = 5
    solution(food_times, k)
