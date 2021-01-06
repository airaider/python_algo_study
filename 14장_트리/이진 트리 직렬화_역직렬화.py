# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        result = ['#']
        while queue :
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append("#")
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '# #':
            return None
        nodes = data.split()
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        idx = 2
        while queue:
            node = queue.popleft()
            if nodes[idx] is not '#':
                node.left = TreeNode(int(nodes[idx]))
                queue.append(node.left)
            idx+=1

            if nodes[idx] is not '#':
                node.right = TreeNode(int(nodes[idx]))
                queue.append(node.right)
            idx += 1
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))