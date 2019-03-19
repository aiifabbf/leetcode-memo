"""
获得二叉树的最大宽度，要考虑null。

所谓最大宽度就是某一层最左边的非null元素和最右边的非null元素之间的 **间隔数 + 1** ，注意不是间隔数，然后取每一层的最大值。

比如 ``[1, 2, 3, 4, 5, null, 6]`` 这个树，第一层宽度是1（而不是0），第二层宽度是2（而不是1），第三层宽度是4（而不是3）。虽然第三层有一个null，但是因为夹在两边的非null节点里，所以算宽度的时候也要算上。

.. 第一遍做的时候比较暴力，直接在维护队列的时候，把null全部放进去，然后果然层数一多就memory limit exceed了……话说我还是第一次遇到爆内存的情况。

思路是，在广度优先遍历的时候，不要只放一个Node对象，而是附带着保存一个水平位置的信息。 [#]_ 然后维护队列的时候，下一层的节点的位置可以这样算

-   左边子节点的水平位置是当前节点水平位置的两倍，即 ``2 * pos``
-   右边子节点的水平位置是当前节点水平位置的两倍加一，即 ``2 * pos + 1``

想想这样做其实还挺有道理的。如果把一个二叉树放在一个左下斜三角形里，每层每个节点的水平位置确实就是这样的。

.. [#] 以往我们广度优先遍历二叉树的时候，队列里面只会放Node对象，但是其实是可以附带一些其他信息的，就像这道题，可以用 ``(Node, pos)`` 这样放进队列里。
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # if root:
        #     queue = [root]
        #     maxWidth = 1
        #     while queue:
        #         for index, value in enumerate(queue):
        #             if value:
        #                 break
        #         firstNonNullPosition = index
        #         for index,value in list(enumerate(queue))[::-1]:
        #             if value:
        #                 break
        #         lastNonNullPosition = index
        #         maxWidth = max(maxWidth, lastNonNullPosition - firstNonNullPosition + 1)
        #         levelQueue = []
        #         for i in queue:
        #             if i:
        #                 levelQueue.append(i.left)
        #                 levelQueue.append(i.right)
        #             else:
        #                 levelQueue.append(None)
        #                 levelQueue.append(None)

        #         queue = levelQueue if any(i != None for i in levelQueue) else []
        #     return maxWidth
        # else:
        #     return 0
        # 一改：memory limit exceed

        if root:
            queue = [
                (root, 0)
            ] # 为了避免过多null，解决办法是同时记录节点和节点的水平位置
            maximumWidth = 0

            while queue:
                levelQueue = []
                maximumWidth = max(maximumWidth, queue[-1][1] - queue[0][1]) # 记录当前遇到的最大水平宽度

                for i in queue:
                    if i[0].left:
                        levelQueue.append(
                            (i[0].left, i[1] * 2) # 因为是左边子节点，所以水平位置是当前节点水平位置的两倍
                        )
                    if i[0].right:
                        levelQueue.append(
                            (i[0].right, i[1] * 2 + 1) # 因为是右边子节点，所以水平位置是当前节点水平位置的两倍加一
                        )

                queue = levelQueue

            return maximumWidth + 1 # 记得+1。因为题目要求的是节点宽度而不是间距宽度
        else:
            return 0