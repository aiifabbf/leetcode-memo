"""
从先根遍历路径构造出二分搜索树

回想先根遍历路径的分区

::

    o [     ] (     )
    -----------------
    0 1              n

大致思路就出来了

1.  array的第一个元素就是根节点
2.  找到array里第一个大于根节点的元素，从这里开始就是右边子树

    因为二分搜索树必须满足右边子树的每个节点都比根节点大，所以array中如果开始出现比第一个元素大的元素，说明进入到了右边子树的分区了。

3.  递归地重现出二分搜索树
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder:
            root = TreeNode(preorder[0])
            rightTreeStartPosition = len(preorder) # 因为有可能右边子树不存在，所以先给它初始化一个末尾

            for index, value in enumerate(preorder[1: ], 1): # 从第二个开始找
                if value > root.val: # 发现了array中第一个比根节点大的元素
                    rightTreeStartPosition = index # 保存右边子树的分区
                    break
            # 有可能不存在右边子树，这时出了迭代之后rightTreeStartPosition还是末尾

            root.left = self.bstFromPreorder(preorder[1: rightTreeStartPosition]) # 递归地重建出左边子树
            root.right = self.bstFromPreorder(preorder[rightTreeStartPosition: ]) # 递归地重建出右边子树
            return root
        else:
            return None