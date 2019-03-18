"""
替换一个二分搜索树里的每个节点的值，用这个树里面出现的所有比这个节点大的节点的值的和、加上自己本身的值。

比如 ``[5, 2, 13]`` 替换成 ``[18, 20, 13]`` 因为

-   比5大的元素只有13，再加上自己就是18
-   比2大的元素有5和13，再加上自己就是20
-   没有比13大的元素，所以加上自己就是13不变。

我的思路是先用中根遍历，遍历一遍这个二分搜索树，这样直接就得到了从小到大排好序的array。这样就方便很多了，再求出累积和，再来一遍中根遍历，一个一个替换掉。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import itertools

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            inorderPath = self.inorderTraversal(root)
            array = list(itertools.accumulate(inorderPath[:: -1]))[:: -1]

            newRoot = self.copyTree(root) # 因为没说in-place，所以我觉得还是返回一个新的吧，不要直接修改任何传进来的东西，虽然慢一点，但是可以避免副作用。

            def replace(root: TreeNode): # 这个函数我怎么都想不到没有副作用的版本。如果能想到就很好了。
                if root:
                    replace(root.left)
                    root.val = array.pop(0)
                    replace(root.right)
                else:
                    pass

            replace(newRoot) # 副作用：会修改传入的树
            return newRoot
        else:
            return None

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            res = []
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right) 
            return res
        return []

    def copyTree(self, root: TreeNode) -> TreeNode:
        if root:
            newRoot = TreeNode(root.val)
            newRoot.left = self.copyTree(root.left)
            newRoot.right = self.copyTree(root.right)
            return newRoot
        else:
            return None