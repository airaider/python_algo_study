# https://leetcode.com/problems/invert-binary-tree/

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

import collections
# 파이썬 풀이법 (bottom-up)
def invertTree(self, root):
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root

# bfs (top-down)
def invertTree(self, root):
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node:
            node.right, node.left = node.left, node.right

            queue.append(node.right)
            queue.append(node.left)
    return root






