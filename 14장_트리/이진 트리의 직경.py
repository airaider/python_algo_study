# https://leetcode.com/problems/diameter-of-binary-tree/

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

import collections
longest : int = 0
def solution(self, root):
    def dfs(node : TreeNode):
        if not node:
            return -1
        left = dfs(node.left)
        right = dfs(node.right)

        self.longest = max(self.longest, left+right+2)

        return max(left, right)+1

    dfs(root)
    return self.longest


