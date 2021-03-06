# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

import collections
def solution(root):
    queue = collections.deque([root])
    depth = 0
    while queue:
        depth+=1
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
    return depth

