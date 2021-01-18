import collections
import itertools

def solution(nodeinfo):
    temp = [(v,i+1) for i,v in enumerate(nodeinfo)]
    print(temp)
    temp.sort(key=lambda x:(-x[0][1], x[0][0]))
    print(temp)


    return


if __name__ == '__main__':
    nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    solution(nodeinfo)
