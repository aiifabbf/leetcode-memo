# 检查一个树是不是二分搜索树

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # if root:
        #     if root.left and root.right:
        #         return self.isValidBST(root.left) and root.left.val < root.val and self.isValidBST(root.right) and root.right.val > root.val
        #     elif root.left:
        #         return self.isValidBST(root.left) and root.left.val < root.val
        #     elif root.right:
        #         return self.isValidBST(root.right) and root.right.val > root.val
        #     else:
        #         return True
        # else:
        #     return True
        
        # 这样单纯递归地检查每个节点的左子节点是否小于节点、右子节点是否大于节点是不对的。考虑 ``[20, 10, 30, null, null, 5, 40]``

#      20
#     /  \
#   10    30
#        /  \
#       5    40

        # 每个节点都满足条件，但是30下面出现了一个5，5小于20，所以这个二叉树不能构成BST。

        # 所以观察发现，在递归判断的同时，还要保留上一层传递下来的一些信息。

        # 在遍历到5的时候，除了5要小于30以外，还要大于20。
        return self.isBST(root, float("-inf"), float("inf"))

    def isBST(self, root: TreeNode, lower: int, upper: int) -> bool: # 除了root还要传入上下界
        if root:
            if root.val > lower and root.val < upper: # 首先根节点要在上下界之内
                if root.left != None and root.right == None: # 左边子树非空、右边子树空
                    return root.left.val < root.val and self.isBST(root.left, lower, root.val) # 下界不变，上界变成根节点的值
                elif root.left == None and root.right != None: # 左边子树空、右边子树非空
                    return root.right.val > root.val and self.isBST(root.right, root.val, upper) # 下界变成根节点的值，上界不变
                elif root.left != None and root.right != None:
                    return root.left.val < root.val and root.right.val > root.val and self.isBST(root.left, lower, root.val) and self.isBST(root.right, root.val, upper)
                else:
                    return True
            else: # 不然即使自己是BST，作为子树放在上层里也不能使大树是BST
                return False
        else: # 空树是BST
            return True