# 判断二叉树是不是平衡二叉树

# 我也不是很懂它这个定义是啥，感觉上去像是最浅层叶子和最深层叶子所在的层数不超过1？

# 定义是树里面每个节点的左边子树和右边子树的深度差距不超过1。

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import functools

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # if root:
        #     queue = [root]
        #     depth = 0
        #     firstLeaveOccurrenceDepth = -1 # -1说明还没遇到叶子过
        #     while queue:
        #         depth += 1
        #         levelQueue = []
        #         for i in queue:
        #             if i.left and i.right: # 非叶子
        #                 levelQueue.append(i.left)
        #                 levelQueue.append(i.right)
        #             else: # 遇到了叶子
        #                 if firstLeaveOccurrenceDepth != -1:
        #                     if depth - firstLeaveOccurrenceDepth > 1:
        #                         return False
        #                     else:
        #                         pass
        #                 else:
        #                     firstLeaveOccurrenceDepth = depth

        #                 if i.left:
        #                     levelQueue.append(i.left)
        #                 if i.right:
        #                     levelQueue.append(i.right)
        #             queue = levelQueue
        #     return True
        # else:
        #     return True
        # 一改：算了……好像理解错了。那什么也不管了，按照定义来吧。
        if root:
            return abs(self.getDepth(root.left) - self.getDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) # 三个条件：自己要平衡、左边子树要平衡、右边子树要平衡
        else:
            return True

    @functools.lru_cache()
    def getDepth(self, root: TreeNode) -> int:
        if root:
            queue = [root]
            depth = 0

            while queue:
                depth += 1
                levelQueue = []
                
                for i in queue:
                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)

                queue = levelQueue

            return depth
        else:
            return 0