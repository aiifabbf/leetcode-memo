"""
.. default-role:: math

用一种奇怪的方式构建二叉树，每次只能选相邻两个节点组成一个子树，子树的根节点的值是这两个节点中大的那个节点 [#]_ ，然后记录下这两个节点的积。问最后所有节点构成一个树之后，这些积的和最小是多少。

例子，对于array

::

    6 2 4

有两种构建树的方法，第一种是6和2先组合，然后再和4组合

::

            6
          /   \
        6       4
      /   \
    6       2

积是 ``12 + 24 = 36``

第二种是2和4组合，然后再和6组合

::

            4
          /   \
        6       4
              /   \
            2       4

积是 ``8 + 24 = 32`` ，所以答案是第二种的 ``32`` 。

看到题马上就想到了 `Huffman树的构建过程 <https://en.wikipedia.org/wiki/Huffman_coding>`_ ，然后就试着用这个方法做了一下，结果过了

1.  每次从array里面找积最小的两个相邻节点
2.  记录下这两个节点的积
3.  把这两个相邻节点替换成这两个节点中大的那个

    这里和Huffman树构造过程不一样，Huffman树构建过程中是把这两个相邻节点替换成两个节点的和。

4.  重复步骤1，直到array里只有一个节点（这个节点就是根节点）

复杂度应该是 `O(n^2)` 。

讲道理我不清楚为啥这个能work。看了讨论之后发现其他人都把这个方法叫greedy。

.. [#] 我知道题目里子树的根节点是两个节点的积，可是这样理解不是更好吗。

.. code:: markdown

    Python `Huffman tree'-like, O(n^2)

    Somehow when reading this question's description, I came up with Huffman coding and [the construction process of a Huffman tree](https://en.wikipedia.org/wiki/Huffman_coding). Though I don't know how this problem is related to building a Huffman tree, but anyway the code works (like any greedy solutions)...

    This idea is to repeatedly find a pair of two adjacent elements in the array with the smallest product, record the smallest product, and then replace these two elements with the greater one among these two, until there is only one element in the array.

    ```python3
    class Solution:
        def mctFromLeafValues(self, arr: List[int]) -> int:
            res = [] # to record the smallest product of each iteration

            while len(arr) >= 2: # until reaching root node
                smallestProduct = float("inf") # smallest product met in this iteration
                smallestProductPosition = -1 # position of the two adjacent elements that makes the smallest product
                bigger = -1 # greater one among these two elements

                for i in range(len(arr) - 1): # iterate over the array
                    a = arr[i] # element1
                    b = arr[i + 1] # element2
                    if a * b <= smallestProduct: # smaller pair product found
                        smallestProduct = a * b
                        smallestProductPosition = i
                        bigger = max(a, b)

                res.append(smallestProduct) # record the smallest product
                arr[smallestProductPosition: smallestProductPosition + 2] = [bigger] # replace the two adjacent elements with the greater one after iteration

            return sum(res)
    ```

    If anyone has an idea how (or whether?) this problem is related to Huffman tree building, please do comment. Thanks!
"""

from typing import *

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = [] # 记录每次迭代找到的最小积

        while len(arr) >= 2: # 直到array里只有一个节点
            smallestProduct = float("inf") # 两个相邻节点的最小积
            smallestProductPosition = -1 # 最小积所在的左边节点的下标
            bigger = -1 # 组成最小积的两个相邻节点中较大的那个节点的值

            for i in range(len(arr) - 1):
                a = arr[i]
                b = arr[i + 1]
                if a * b <= smallestProduct: # 找到了更小的积
                    smallestProduct = a * b # 记录下最小积
                    smallestProductPosition = i # 记录下下标
                    bigger = max(a, b) # 记录下较大的那个节点的值

            res.append(smallestProduct) # 记录这次迭代的最小积
            arr[smallestProductPosition: smallestProductPosition + 2] = [bigger] # 把组成最小积的那两个节点替换成那两个节点中较大的那个节点

        return sum(res)

# s = Solution()
# print(s.mctFromLeafValues([6, 2, 4])) # 32