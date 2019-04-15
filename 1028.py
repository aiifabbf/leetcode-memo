"""
从一种奇怪的先根遍历路径里恢复出原二叉树

这种奇怪的先根遍历路径是这样的

-   数字前面的 ``-`` 的数量表示数字所在的节点的深度

    比如 ``1-2--4-3`` 表示1是根节点，2是左边子节点，3是右边子节点，4是2的左边子节点。

-   如果一层只出现了一个子节点，默认这个子节点是左边子节点

    比如 ``1-2--4-3`` 里面，2只有一个子节点4，这种情况下4被认为是2的左边子节点。

还是一个递归的思路，和105、106没有太大的差别。先找到根节点，再找到左边子树在string中的起始位置、右边子树在string中的起始位置。然后这一层就搞定了把左边子树每个数字前的 ``-`` 去掉一个，然后递归地恢复出左边子树，粘到根节点上。右边同理。

根节点不用说了，肯定是string的第一个数。左边子节点和右边子节点的在string中的特征是，它们的前面只有1个 ``-`` 。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if S:
            nodes = ["-" if v == "" else v for v in S.split("-")] # 和介绍中不一样，我这里先去掉了所有的 ``-``
            root = TreeNode(int(nodes[0]))
            if len(nodes) == 1: # 如果只有一个节点，说明只有根节点
                return root
            elif len(nodes) == 2: # 如果有两个节点，说明只有根节点和左边子节点
                root.left = TreeNode(int(nodes[1]))
                return root
            else: # 三个及三个以上节点
                for i, v in enumerate(nodes[2: ], 2): # 如果存在右边子树，一定从第2个节点开始，因为第0个节点是根节点、第1个节点是左边子节点
                    if nodes[i - 1] != "-" and v != "-": # 发现了右边子节点
                        rightPosition = i
                        break
                else:
                    rightPosition = len(nodes)

                leftTraversal = nodes[1: rightPosition] # 左边子树的起始位置
                rightTraversal = nodes[rightPosition: ] # 右边子树的起始位置

                root.left = self.recoverFromPreorder("".join(leftTraversal)) # 递归地恢复出左边子树。因为最前面已经去掉过一次 ``-`` 了，这里就不用去掉了，直接连接起来就可以了
                root.right = self.recoverFromPreorder("".join(rightTraversal)) # 递归地恢复出右边子树
                return root
        else:
            return None