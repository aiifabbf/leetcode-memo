"""
和96差不多，96题只要你算出种类个数，这一题要你真的输出这些树。

思路也是差不多的，但是需要写一个辅助函数，因为拆分的时候可能会出现[i, i + 1, ..., n]，所以这个辅助函数的作用就是生成[a, a + 1, a + 2, ..., b]的所有BST的可能的情况。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generateTreesBetween(1, n)

    def generateTreesBetween(self, a: int, b: int) -> List[TreeNode]:
        # 输出[a, a + 1, a + 2, ..., b]的所有BST
        if b < a:
            return []
        if b == a:
            return [
                TreeNode(b)
            ] # 只有一种情况
        else:
            res = []

            for i in range(a, b + 1):
                leftCombinations = self.generateTreesBetween(a, i - 1) # 左边子树的所有排列
                rightCombinations = self.generateTreesBetween(i + 1, b) # 右边子树的所有排列
                if leftCombinations != [] and rightCombinations != []: # 左右子树都非空

                    for left in leftCombinations:

                        for right in rightCombinations:
                            root = TreeNode(i)
                            root.left = left
                            root.right = right
                            res.append(root)

                elif leftCombinations == [] and rightCombinations != []: # 左边子树空

                    for right in rightCombinations:
                        root = TreeNode(i)
                        root.right = right
                        res.append(root)

                elif leftCombinations != [] and rightCombinations == []: # 右边子树空

                    for left in leftCombinations:
                        root = TreeNode(i)
                        root.left = left
                        res.append(root)

                # 左右子树全空的情况在上一层已经解决了
            return res