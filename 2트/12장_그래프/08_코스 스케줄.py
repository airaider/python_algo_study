# https://leetcode.com/problems/course-schedule/
import collections

def solution1(numCourses, prerequisites):
    print(numCourses)
    graph = collections.defaultdict(list)

    for x,y in prerequisites:
        graph[x].append(y)
    print(graph)
    traced = set()

    def dfs(i):
        if i in traced:
            return False
        traced.add(i)

        for y in graph[i]:
            if not dfs(y):
                return False
        traced.remove(i)
        return True
    for x in list(graph):
        if not dfs(x):
            return False
    return True


def solution2(numCourses, prerequisites):
    pass
    print(numCourses)

if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    solution1(numCourses, prerequisites)
    solution2(numCourses, prerequisites)