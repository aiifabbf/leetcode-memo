# 检查一个二叉树是不是完全二叉树

# 完全二叉树的定义是

# -   倒数第二层全部排满
# -   倒数第一层的元素尽量往左排满

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
            finalLevelReached = False
            while queue:
                levelQueue = []
                for i in queue:
                    if not finalLevelReached:
                        if i.left != None and i.right != None:
                            levelQueue.append(i.left)
                            levelQueue.append(i.right)
                        elif i.left == None and i.right != None:
                            return False
                        elif i.left != None and i.right == None: # 说明应该已经到了最后一层了
                            if i.left.left or i.left.right: # 但是发现最后一层下面还有一层
                                return False # 那可以肯定不是完全二叉树
                            else:
                                finalLevelReached = True
                        else:
                            
                    else:

                queue = levelQueue
            
        else:
            return True