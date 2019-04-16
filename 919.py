"""
实现一个完全二叉树插入器。

按层遍历吧。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, v: int) -> int:
        queue = [self.root]

        while queue: # 按层遍历每个节点
            levelQueue = []

            for node in queue:
                if node.left != None and node.right != None: # 左边节点和右边节点都不为空
                    levelQueue.append(node.left)
                    levelQueue.append(node.right)
                if node.left != None and node.right == None: # 左边节点不空，但是右边节点空，说明下一层是最后一层了，欲插入的节点应该变成这个节点的右边子节点
                    node.right = TreeNode(v)
                    return node.val
                if node.left == None and node.right == None: # 左边节点和右边节点都为空，说明下一层是最后一层了，欲插入的节点应该变成这个节点的左边子节点
                    node.left = TreeNode(v)
                    return node.val
            # 还有一种情况我们还没有处理，就是最后一层全满的情况，此时应该新开一行，欲插入的节点放在这一行的第一个位置
            if levelQueue == []: # 这一层全满，可是下一层却全空
                queue[0].left = TreeNode(v) # 欲插入的节点应该是这个最后一层第一个节点的左边子节点
                return queue[0]
            else:
                queue = levelQueue

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()