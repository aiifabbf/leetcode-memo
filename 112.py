# 判断二叉树里存不存在一条从根节点到叶子的路径，使得路径上的节点值之和等于sum

# 感觉还是一个递归的思路，可以转换成存不存在从左子节点、从右子节点出发到叶子的路径和等于sum - root.val的问题，再这样以此类推。

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root:
            # if root.val == sum: # 因为要求是从根节点到叶子的路径，所以要加一条判断，判断是不是叶子。如果到了中间一半就得到了sum也没用。
            if root.val == sum and root.left == None and root.right == None:
                return True
            else:
                return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        else:
            return False