# 选出所有左叶子节点，算出它们值的累加。

# 递归吧。

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root:
            if root.left and root.left.left == None and root.left.right == None: # 左节点是左叶子:
                return root.left.val + self.sumOfLeftLeaves(root.right) # 这里判断出左子节点是左叶子之后，右子节点不能就这样不管了，因为右子树也可能含有左叶子
            else:
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        else:
            return 0