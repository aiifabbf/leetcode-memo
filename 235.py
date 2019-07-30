"""
在一个BST里面，找到两个节点的最近公共祖先节点的值。

我的思路是先找到从根节点到p、从根节点到q的路径，然后给这两条路径做diff，找出第一次两条路径出现分叉之前的那个节点，一定就是它们的最近公共祖先节点。

比如 ``[6, 2, 8, 90, 4, 7, 9, null, null, 3, 5]`` 这个树，要找到2和4的最近公共祖先，就先找到从根节点到2的路径 ``[6, 2]``，找到根节点到4的路径 ``[6, 2, 4]``，然后这两个路径diff一下，马上就找到是2了。

为什么感觉我的复杂度是 :math:`O(\log n)`……

也可以利用一下BST的性质，用递归来做。从根节点开始，比较当前子树的根节点和p、q的大小关系，如果发现

-   根节点的值等于p的值或者q的值

    那么根节点就是p和q的最近公共祖先。

-   p、q的值全都小于根节点的值

    这时候当前子树的根节点确实是p、q的公共祖先，但不是最近公共祖先。
    
    因为左边子树里全都是小于根节点的节点，所以应该往左边子树继续搜索。

-   p、q的值全都大于根节点的值

    同理，根节点确实是p、q的公共祖先，但不是最近公共祖先。

    因为右边子树里全都是大于根节点的节点，所以应该往右边子树继续搜索。

-   p小于根节点、q大于根节点，或者p大于根节点、q小于根节点

    此时出现了分叉，根节点就是p和q的最近公共祖先。
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
    #     routeToP = self.routeToNode(root, p) # 找到从根节点到p的路径
    #     routeToQ = self.routeToNode(root, q) # 找到从根节点到q的路径
    #     i = 0

    #     # 把两个路径做个diff，取得第一次两条路径出现不同之前的那个节点
    #     while i < min(len(routeToP), len(routeToQ)):
    #         if routeToP[i].val != routeToQ[i].val: # 出现了不同
    #             return routeToP[i - 1] # 之前那个节点肯定是最近公共祖先
    #         i += 1

    #     return routeToP[i - 1] # 发现其中一条路径已经走完了，说明出现了包含关系，直接返回较短的那条路径的最后一个元素。

    # def routeToNode(self, tree: TreeNode, node: TreeNode) -> List[TreeNode]: # 返回从根节点到目标节点的路径
    #     if tree.val == node.val:
    #         return [tree]
    #     else:
    #         if node.val < tree.val:
    #             return [tree] + self.routeToNode(tree.left, node)
    #         else:
    #             return [tree] + self.routeToNode(tree.right, node)
    # 不如利用一下BST的性质

        if root:
            p, q = sorted([p, q], key=lambda v: v.val) # 让p永远是小的那个节点、q是那个大的节点
            if (p.val < root.val and root.val < q.val) or (p.val == root.val) or (q.val == root.val): # 如果出现分叉、或者p或q的值和root的值相等
                return root # root就是最近公共祖先
            elif p.val < root.val and q.val < root.val: # p, q < r
                return self.lowestCommonAncestor(root.left, p, q) # 往左边子树继续搜索
            else: # r < p, q
                return self.lowestCommonAncestor(root.right, p, q) # 往右边子树继续搜索
        else:
            return None