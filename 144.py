"""
二叉树的先根遍历

有两种方法

-   递归

    1.  访问根节点
    2.  递归地调用自身，左边子节点作为参数传入
    3.  递归地调用自身，右边子节点作为参数传入

-   用stack模拟递归

    1.  stack压入根节点
    2.  stack弹出一个节点，访问这个节点
    3.  stack压入这个节点的 **右边子节点** (如果不为null的话)
    4.  stack压入这个节点的左边子节点 （如果不为null的话）
    5.  回到第2步，直到stack空了

"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     if root:
    #         res = [root.val]
    #         if root.left:
    #             res += self.preorderTraversal(root.left)
    #         if root.right:
    #             res += self.preorderTraversal(root.right)
    #         return res
    #     else:
    #         return []
    # 一改：用stack会比递归快一点，而且不会受递归深度限制

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            res = []
            stack = [root]

            while stack:
                node = stack.pop()
                res.append(node.val)
                if node.right: # 这里要记住是右边先进stack，因为这样才能做到下一次弹出的时候是左边子节点先弹出
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

            return res
        else:
            return []