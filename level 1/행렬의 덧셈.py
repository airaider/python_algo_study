def solution(arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        print(i, j)
        ans = []
        for a, b in zip(i,j):
            print(a,b)
            ans.append(a+b)
        answer.append(ans)
    print(answer)
    return answer

if __name__ == '__main__':
    arr1 = [[1, 2], [2, 3]]
    arr2 = [[3, 4], [5, 6]]
    solution(arr1, arr2)