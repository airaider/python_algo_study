def solution(n, arr1, arr2):
    print(n, arr1, arr2)
    maps=[]
    for i,j in zip(arr1, arr2):
        maps.append(bin(i | j)[2:].replace('1', '#').replace('0', " "))
    print(maps)
    for map in maps:
        print(map)

    return



if __name__ == '__main__':
    n = 6
    arr1 = [46, 33, 33 ,22, 31, 50]
    arr2=[27 ,56, 19, 14, 14, 10]
    solution(n, arr1, arr2)