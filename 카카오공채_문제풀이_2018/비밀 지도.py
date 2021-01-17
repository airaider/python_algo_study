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
    n = 5
    arr1 = [9,20,28,18,11]
    arr2 = [30,1,21,17,28]
    solution(n, arr1, arr2)