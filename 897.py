# 二叉树的中根遍历，然后再变成一个右单链二叉树

# 我的思路是先用94题，把二叉树变成一个array，再从这个array构建出右单链二叉树

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        array = self.inorderTraversal(root)
        if array:
            rootNode = lastNode = TreeNode(array[0])
            for i in array[1: ]:
                node = TreeNode(i)
                lastNode.right = node
                lastNode = node
            return rootNode
        else:
            return None

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            res = []
            if root.left:
                res += self.inorderTraversal(root.left)
            res.append(root.val)
            if root.right:
                res += self.inorderTraversal(root.right)
            return res
        else:
            return []