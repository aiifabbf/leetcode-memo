"""
在一个BST里面，找到两个节点的最近公共祖先节点。

我的思路是先找到从根节点到p、从根节点到q的路径，然后给这两条路径做diff，找出第一次两条路径出现分叉之前的那个节点，一定就是它们的最近公共祖先节点。

比如 ``[6, 2, 8, 90, 4, 7, 9, null, null, 3, 5]`` 这个树，要找到2和4的最近公共祖先，就先找到从根节点到2的路径 ``[6, 2]``，找到根节点到4的路径 ``[6, 2, 4]``，然后这两个路径diff一下，马上就找到是2了。

为什么感觉我的复杂度是 :math:`O(\log n)`……
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        routeToP = self.routeToNode(root, p) # 找到从根节点到p的路径
        routeToQ = self.routeToNode(root, q) # 找到从根节点到q的路径
        i = 0

        # 把两个路径做个diff，取得第一次两条路径出现不同之前的那个节点
        while i < min(len(routeToP), len(routeToQ)):
            if routeToP[i].val != routeToQ[i].val: # 出现了不同
                return routeToP[i - 1] # 之前那个节点肯定是最近公共祖先
            i += 1

        return routeToP[i - 1] # 发现其中一条路径已经走完了，说明出现了包含关系，直接返回较短的那条路径的最后一个元素。

    def routeToNode(self, tree: TreeNode, node: TreeNode) -> List[TreeNode]: # 返回从根节点到目标节点的路径
        if tree.val == node.val:
            return [tree]
        else:
            if node.val < tree.val:
                return [tree] + self.routeToNode(tree.left, node)
            else:
                return [tree] + self.routeToNode(tree.right, node)