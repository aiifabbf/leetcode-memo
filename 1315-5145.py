"""
给一个二叉树，找到这个二叉树里所有满足祖父节点（也就是父节点的父节点）是偶数的节点，再计算出这些节点的值的和。

我的做法是先BFS扫描一遍树，生成一个hash map表示每个节点的父节点是什么：key是节点，value是节点的父节点。然后再遍历一遍这个hash map，找到所有满足祖父节点是偶数的节点，把它们的值全部加起来。

挺简单的。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root:
            queue = [root]
            parent = {} # key是节点，value是这个节点的父节点

            while queue: # BFS扫描一遍二叉树，填满parent这个hash map
                size = len(queue)

                for _ in range(size):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                        parent[node.left] = node # 记下这个节点的左节点的父节点是当前节点
                    if node.right:
                        queue.append(node.right)
                        parent[node.right] = node # 记下这个节点的右节点的父节点是当前节点
            
            res = 0 # 满足祖父节点是偶数的所有节点的值的累加和

            for k, v in parent.items(): # 遍历一遍hash map
                # k是节点，v是这个节点的父节点，所以parent[v]应该是这个节点的祖父节点（如果存在的话）
                if v in parent and parent[v].val % 2 == 0: # 如果节点存在祖父节点、并且祖父节点的值是偶数的话
                    res += k.val # 记下节点的值

            return res
        else:
            return 0