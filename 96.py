"""
给一个大小为n的排好序的array，可以构成多少种不同的二分搜索树？

对于一个排好序的array来说，可以任意选取其中的一个元素作为BST的根节点。又因为BST需要满足

    对于BST的任意一个子树，这个子树的左边子树里的任意一个节点的值都小于子树的根节点的值，右边子树里的任意一个节点的值都大于子树的根节点的值。

现在选取的这个元素左边的所有元素因为都比这个元素小，所以必定只能放在根节点的左边子树里面；同理，右边的所有元素都比这个被选取的元素大，所以必定只能放在根节点的右边子树里。

想到这里，其实隐隐有点递归的感觉了，因为同样这个根节点的左边子树、右边子树也是BST，还可以分别拆分下去，直到一个树里只有0个、1个或者2个元素为止。

.. _Catalan Number: https://en.wikipedia.org/wiki/Catalan_number
"""

from typing import *

import functools
import operator
class Solution:
    @functools.lru_cache()
    def numTrees(self, n: int) -> int:
        if n == 0: # 空树
            return 1
        elif n == 1: # 单元素
            return 1
        elif n == 2: # 两个元素
            return 2
        else:
            summation = 0
            for i in range(1, n + 1): # 第1到第n个元素都可以做根节点
                summation += self.numTrees(i - 1) * self.numTrees(n - i) # 第i个元素做根节点的时候，左边子树可能的排列情况总数是以左边第1到第i - 1个元素、共i - 1个元素形成新的BST的排列情况总数，右边子树可能的排列情况总数也是以右边第i + 1个元素到第n个元素、共n - i个元素形成新的BST的排列情况总数。左边子树和右边子树的排列毫无关联、互相独立，所以是选取第i个元素作为根节点的排列方式是左边排列总数乘以右边排列总数。
            return summation
        
            # return round(functools.reduce(operator.mul, [(n + k) / k for k in range(2, n + 1)])) # 也可以直接用通项公式。这个通项公式叫做Catalan number。