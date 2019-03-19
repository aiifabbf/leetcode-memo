"""
给一个节点值只会是0或者1的二叉树，把所有不含有1的子树都删掉。

换个等价的说法是，把所有全0的子树都删掉。

应该是后根遍历吧……因为要先更新子树的状态，再更新大树的状态。
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # if root:
        #     if root.val == 0 and root.left == None and root.right == None:
        #         root.left = self.pruneTree(root.left)
        #         root.right = self.pruneTree(root.right)
        #         return root
        #     else:
        #         return None
        # else:
        #     return root
        # 一改：上面的写法有一个问题，就是会导致全0子树的根节点，再删完左边子树和右边子树时候，自己却不删除。

        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if root.left == None and root.right == None and root.val == 0:
                return None
            else:
                return root
        else:
            return None

        # 我觉得写的比参考答案好好吧……