#https://leetcode.com/problems/palindrome-linked-list/
import collections
class Solution(object):
    def isPalindrome(self, head):
        q = []
        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True


    def isPalindrome2(self, head):
        q = collections.deque
        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True