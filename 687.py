"""
在一个二叉树里，找到一路上节点的值保持不变的最长路径的长度。

题目对这条路径没有任何要求，既没有要求一定要从根节点出发一定要到叶子，也没有要求路径一定是单向的，所以这个路径可能可以从底端往上走，走到一个节点之后再往下走也可以……总之怎么走都可以。 [#]_

.. [#] 突然觉得有点类似543题。这里也是解决子问题再合并没法直接解决大问题，因为最长值不变路径不一定经过根节点，而是有可能在下面的某个子树里面。

所以和543题一样，定义一个函数，表示一定从传入的树的根节点出发的最长值不变路径的长度，然后遍历树里面每个节点，利用这个函数，找到从这个节点出发、往左边子树向下走和往右边子树向下走能取得的最长的路径，加起来就可以了。一边遍历，一边记录到现在为止最长的路径长度。遍历完成之后，最长的路径长度也就出来了。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import functools

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root:
            queue = [root]
            res = 0

            while queue: # 遍历每个节点，找到从这个节点开始的最长值不变路径
                i = queue.pop()
                maximumPathLength = 0 # 记录目前为止最长的路径的长度
                if i.left:
                    queue.append(i.left)
                    if i.left.val == i.val: # 左边节点可以接上根节点
                        maximumPathLength += self.longestUnivalueDownwardDepthFromRoot(i.left) # 看一下如果往左边子树走，最远能走到哪里
                if i.right:
                    queue.append(i.right)
                    if i.right.val == i.val: # 右边节点可以接上根节点
                        maximumPathLength += self.longestUnivalueDownwardDepthFromRoot(i.right) # 看一下如果往右边子树走，最远能走到哪里
                res = max(res, maximumPathLength) # 更新最长路径长度
            
            return res
        else:
            return 0

    @functools.lru_cache()
    def longestUnivalueDownwardDepthFromRoot(self, root: TreeNode) -> int: # 一定从根节点开始的、最长的值不变路径 **经过的节点个数**。不用路径长度的原因是递归不方便……
        if root:
            if root.left == None and root.right == None:
                return 1
            elif root.left != None and root.right == None:
                if root.left.val == root.val:
                    return 1 + self.longestUnivalueDownwardDepthFromRoot(root.left)
                else:
                    return 1
            elif root.left == None and root.right != None:
                if root.right.val == root.val:
                    return 1 + self.longestUnivalueDownwardDepthFromRoot(root.right)
                else:
                    return 1
            else:
                if root.left.val == root.val == root.right.val:
                    return 1 + max(self.longestUnivalueDownwardDepthFromRoot(root.left), self.longestUnivalueDownwardDepthFromRoot(root.right))
                elif root.left.val == root.val and root.val != root.right.val:
                    return 1 + self.longestUnivalueDownwardDepthFromRoot(root.left)
                elif root.left.val != root.val and root.val == root.right.val:
                    return 1 + self.longestUnivalueDownwardDepthFromRoot(root.right)
                else:
                    return 1
        else:
            return 0

    # 好像最后还挺快的……80%