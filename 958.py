"""
检查一个二叉树是不是完全二叉树

完全二叉树的定义_ 是

-   倒数第二层全部排满
-   倒数第一层的元素尽量往左排满

.. _完全二叉树的定义: https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees

所以能推测出，广度优先遍历一个完全二叉树的时候，一旦遇到一次null，后面一定遇到的全部都是null了。如果后面还遇到非null，说明这个树一定不是完全二叉树。
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root:
            queue = [root]
            nullMet = False

            # 一改：这里没必要用按层遍历，普通的广度优先就够了
            while queue:
                i = queue.pop(0)
                if i.left: # 左边子节点存在
                    if nullMet: # 但是之前已经遇到过null了
                        return False
                    queue.append(i.left)
                else: # 左边子节点不存在
                    nullMet = True # 标志已经遇到过null了，后面不能再遇到非null了
                if i.right: # 对右边子节点同理
                    if nullMet:
                        return False
                    queue.append(i.right)
                else:
                    nullMet = True

            return True
        else:
            return True