# 输出一个树的最大深度

# 思路还是用广度优先，同时用一个变量保存当前是第几层。

from typing import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root:
            depth = 0
            queue = [root]
            while queue: # 当queue空的时候，说明到最后一层以下一层了
                levelQueue = sum((i.children for i in queue), []) # 得到这层所有节点的所有子节点。没有直接append到queue的原因是会丢失深度信息
                queue = levelQueue
                depth += 1
            # 退出循环的时候，depth就是深度
            return depth
        else:
            return 0