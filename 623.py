"""
在二叉树里第d行插入一行值为v的节点

插入的规则是这样的

-   如果d = 1，意思是要在第1层插入一行节点，可是第1层是只有一个节点，而且是根节点，这时候就建一个新的节点，值是v，然后把原来的根节点接到新节点的左边，返回新节点
-   其他情况，给d - 1层上的每个节点，都添加一个值为v的左节点、一个值为v的右节点，然后把原来节点上的左边子树接到新的左节点左边、原来节点上的右边子树接到新的右节点的左右边

挺简单的，按层遍历就好了。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1: # d = 1特殊处理
            newRoot = TreeNode(v) # 建一个值是v的新节点
            newRoot.left = root # 原根节点接到新节点的左边
            return newRoot # 返回新节点
        else: # 其他情况
            depth = 1 # 记录当前是第几层
            queue = [root]

            while queue:
                levelQueue = [] # 按层遍历
                if depth == d - 1: # 当前是d - 1层

                    for node in queue: # 对d - 1层上的每个节点
                        newLeftNode = TreeNode(v) # 建一个新的左节点
                        newLeftNode.left = node.left # 把左节点接到新的左节点上
                        node.left = newLeftNode # 把新的左节点接到节点的左边

                        newRightNode = TreeNode(v) # 建一个新的右节点
                        newRightNode.right = node.right # 把右节点接到新的右节点上
                        node.right = newRightNode # 把新的右节点接到节点的右边

                    return root # 插入完成之后就可以直接返回根节点了，不用再往下遍历了
                else: # 还没有到达d - 1层

                    for node in queue: # 普通的按层遍历
                        if node.left:
                            levelQueue.append(node.left)
                        if node.right:
                            levelQueue.append(node.right)

                queue = levelQueue
                depth += 1

            return root