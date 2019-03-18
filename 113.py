"""
找到一个二叉树里，路径和为sum的、所有根节点到叶子节点的路径。

还是递归的思路。要找从根节点到叶子节点的这样一条路径，可以转换成两个子问题

-   找到左边子树里，路径和为sum减去根节点值（即 ``sum - root.val`` ）的、所有从左节点到左边子树的叶子节点的路径
-   找到右边子树里，路径和为sum减去根节点值（即 ``sum - root.val`` ）的、所有从右节点到右边子树的叶子节点的路径

这样一层一层递归下去，最终到达叶子的时候，只要判断叶子值是否等于sum一路减下去之后的那个值。
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root: # 非空树
            if root.left == None and root.right == None: # 叶子
                if root.val == sum: # 刚好加到这里就是sum
                    return [
                        [root.val]
                    ] # 很巧，找到了这样一条路径
                else: # 加到这里不是sum，又因为这里已经是叶子了，所以没可能再加下去了
                    return []
            else: # 不是叶子，那么接下去是仍然有可能存在这种路径的
                return [[root.val] + i for i in self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)] # 分别从左边子树、右边子树展开
        else: # 空树
            return [] # 绝对不存在这种路径