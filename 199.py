# 画出二叉树的右视图

# 所谓右视图就是把二叉树看成一个平面上的图像，然后从右边往左看。左视图应该是一个单链。想象一下吧……

# 这道题就是我去面试联创被问到的……虽然我瞬间就明白了右视图是什么，但是没做出来QAQ

# 其实就是二叉树的广度优先、按层遍历。

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # if root == None:
        #     return []

        # queue = [root]
        # numberOfNodesOnThisLevel = 0
        # numberOfNodesOnNextLevel = 1
        # result = []

        # while numberOfNodesOnNextLevel != 0 :
        #     numberOfNodesOnThisLevel = numberOfNodesOnNextLevel
        #     numberOfNodesOnNextLevel = 0
        #     tempQueue = []
        #     result.append(queue[numberOfNodesOnThisLevel].val)

        #     for i in queue:
        #         if i.left:
        #             tempQueue.append(i.left)
        #             numberOfNodesOnNextLevel += 1
        #         if i.right:
        #             tempQueue.append(i.right)
        #             numberOfNodesOnNextLevel += 1
                
        #     queue = tempQueue

        # return result
        # 一改：这个代码也太难懂了……

        if root:
            queue = [root]
            result = []
            while queue:
                levelQueue = []
                for i in queue:
                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)
                result.append(queue[-1].val) # 如果要左视图，换成queue[0]就完事儿了
                queue = levelQueue
            return result
        else:
            return []