def solution(n, arr1, arr2):

    map = []
    for i in range(n):
        line = ''
        for j in format(arr1[i]|arr2[i], 'b'):
            if j == '1':
                line+='#'
            else:
                line+=' '
            print(line)
        while len(line)<n:
            line=' '+line

        map.append(line)
    print(map)

    return



if __name__ == '__main__':
    n = 6
    arr1 = [46, 33, 33 ,22, 31, 50]
    arr2=[27 ,56, 19, 14, 14, 10]
    solution(n, arr1, arr2)