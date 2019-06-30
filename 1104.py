r"""
有一个二叉树是这样的

::

    1
    3 2
    4 5 6 7
    15 14 13 12 11 10 9 8
    ...

规律是把原来按顺序递增的二叉树

::

    1
    2 3
    4 5 6 7
    8 9 10 11 12 13
    ...

里，奇数（从0开始数）的层颠倒，偶数的层不变。给一个数字n，问你从根节点到这个数字的路径是怎样的。

从根节点到数字的路径很难想，不如想着怎样得到从数字到根节点的路径、然后最后再颠倒一下。因为在顺序的二叉树中，任意一个数字n的父节点是n // 2，比如想要得到11的父节点，直接用11整除2得到5就是11的父节点。

至于其中一层隔一层颠倒也是很容易搞定的，找一下规律就可以很容易发现，如果一个数字n在第k+1层，那么这个数字的父节点在第k层，并且这个数字的父节点就是 :math:`2^{k + 1} - \left\lfloor{n \over 2}\right\rfloor + 2^k - 1` 。比如在顺序二叉树里面，9整除2是4，所以9的父节点应该是4，但是因为上面一层颠倒顺序了，所以9的父节点变成了7，7正好就是8 - 4 + 3。

所以思路也就出来了

1.  找到数字n在顺序二叉树的第几层

    顺序二叉树的第k层的第一个元素是2^k，最后一个元素是2^(k + 1) - 1。所以可以每次判断数字是否比该层第一个元素小，如果发现比该层第一个元素小，那么说明数字在上一层。

2.  一层一层往上找父节点，直到到1为止
"""

from typing import *

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        k = 0 # 从第0层开始搜索

        while True:
            if label < 2 ** k: # 如果发现数字比第k层第一个数字还要小
                k = k - 1 # 说明数字在上一层
                break
            else: # 数字大于等于第k层第一个数字
                k += 1 # 试试再往下一层
        # 出循环之后，k就是数字所在的层编号
        res = [label] # 从数字到根节点的路径

        for levelIndex in reversed(range(0, k)): # 一层一层往上找父节点
            res.append(2 ** (levelIndex + 1) - res[-1] // 2 + 2 ** (levelIndex) - 1)

        return res[:: -1] # 颠倒一下，就得到了从根节点到数字的路径

# s = Solution()
# print(s.pathInZigZagTree(1))
# print(s.pathInZigZagTree(8))
# print(s.pathInZigZagTree(15))
# print(s.pathInZigZagTree(14))