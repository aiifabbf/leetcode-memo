"""
实现一个二分搜索树迭代器

……又是中根遍历
"""

from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.array = self.inorderTraversal(root) # 直接生成从小到大的排好序的array
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            res = []
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
            return res
        else:
            return []

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.array.pop(0) # 要一个给一个

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.array)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()