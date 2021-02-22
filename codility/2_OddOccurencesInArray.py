import collections

def solution(A):
    # write your code in Python 3.6
    word = collections.defaultdict(int)
    for i in A:
        if i in word:
            del word[i]
        else:
            word[i]+=1
    a = word.keys()
    for i in a:
        return i
    pass


if __name__ == '__main__':
    A = [9,3,9,3,9,7,9]
    solution(A)