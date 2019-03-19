"""
从先根遍历路径、后根遍历路径重现出二叉树。

之前做过

-   从先根遍历路径、中根遍历路径重现出二叉树
-   从后根遍历路径、中根遍历路径重现出二叉树

可以看到先根、中根路径可以完全唯一地确定一个二叉树，后根、中根路径也可以完全确定一个二叉树，原因在于中根遍历路径的信息量是比先根、后根遍历路径都要大的，因为有了中根遍历路径和根节点的位置，就可以知道中根遍历路径中左边子树和右边子树的范围。

::

    o [     ] (     )   pre-order
    [     ] o (     )   in-order
    [     ] (     ) o   post-order

给出先根、后根遍历路径不能唯一确定一个二叉树的原因是，虽然左边子树和右边子树包含的元素一定相同，但是满足相同这个标准的左边子树和右边子树的范围可能有多种选取方式。 [#]_

.. [#] 我一时举不出例子……

题目只要求返回任意一种就可以。

先根遍历路径的第一个元素、后根遍历路径的最后一个元素一定是根节点的值，剩下的是左边子树和右边子树各自的先根遍历路径和后根遍历路径，所以子树的先根、后根遍历路径的划分要满足两个条件

-   子树的先根遍历路径的第一个元素和后根遍历路径的最后一个元素相等

    这个很好理解，因为总不能根节点值不一样吧。

-   子树的先根遍历路径里所含的元素和后根遍历路径里所含的元素相同

    不能出现比如先根遍历路径有1、后根遍历路径没有1的情况。两个路径包含的元素要种类相同、数量分别相等。

所以每次提取完根节点之后，就按上面的标准来划分左右边子树。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if pre:
            if len(pre) == 1:
                return TreeNode(pre[0])
            else:
                root = TreeNode(pre[0])

                for leftTreeSize in range(1, len(pre)): # 尝试每一种划分位置
                    leftTreePreorderPath = pre[1: 1 + leftTreeSize] # 拟测试的左边子树的先根遍历路径
                    leftTreePostorderPath = post[0: leftTreeSize] # 左边子树的后根遍历路径
                    rightTreePreorderPath = pre[1 + leftTreeSize: ] # 右边子树的先根遍历路径
                    rightTreePostorderPath = post[leftTreeSize: ] # 右边子树的后根遍历路径s
                    if set(leftTreePreorderPath) == set(leftTreePostorderPath) and leftTreePreorderPath[0] == leftTreePostorderPath[-1] and rightTreePreorderPath[0] == rightTreePostorderPath[-1]: # 元素同种同数量、先根遍历路径第一个元素和后根遍历路径最后一个元素相等
                        root.left = self.constructFromPrePost(leftTreePreorderPath, leftTreePostorderPath)
                        root.right = self.constructFromPrePost(rightTreePreorderPath, rightTreePostorderPath)
                    # 因为题目保证答案存在，所以失败的情况不考虑

                return root
        else:
            return None