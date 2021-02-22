def solution(X, A):
    leaf = set()

    for i, k in enumerate(A):
        leaf.add(k)
        if len(leaf) == X:
            print(i)
            return i
    return -1


if __name__ == '__main__':
    A = [1,3,1,4,2,3,5,4]
    K = 5
    solution(K, A)