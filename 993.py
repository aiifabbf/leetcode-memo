# 判断x和y是不是cousin。所谓cousin就是深度相同、但是parent节点不同的节点。

# 好像还是广度优先的方法吧……

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root:
            queue = [root]
            while queue:
                levelQueue = []
                xParent = None # x的parent
                yParent = None # y的parent
                for index, value in enumerate(queue):
                    if value.left:
                        levelQueue.append(value.left)
                        if value.left.val == x:
                            xParent = value
                        elif value.left.val == y:
                            yParent = value
                    if value.right:
                        levelQueue.append(value.right)
                        if value.right.val == x:
                            xParent = value
                        elif value.right.val == y:
                            yParent = value
                if xParent and yParent and xParent != yParent: # x的节点和y的节点都找到了，且它们的parent不是同一个。
                    return True
                elif (xParent == None and yParent != None) or (yParent == None and xParent != None): # x的节点找到了但是y的节点没找到、或者y的节点找到了但是x的节点找到了，那么下面也直接不用找了。
                    return False
                queue = levelQueue
            return False # 二叉树里根本不存在值是x或值是y的节点
        else: # 空二叉树
            return False