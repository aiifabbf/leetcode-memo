"""
找到

.. math::

    \max\{a_i + a_j + i - j | 0 \leq i < j \leq n - 1}

最差 :math:`O(n^2)` ，想找一个 :math:`O(n)` 的解决方法。这种目标函数优化的题，往往都是用动态规划来做。

观察发现这题里面的目标函数 :math:`f(i, j)` 可以分解成关于i和关于j的两个独立的函数的和

.. math::

    f(i, j) = f_1(i) + f_2(j)

其中

.. math::

    \begin{aligned}
        f_1(i) = a_i + i \\
        f_2(j) = a_j - j
    \end{aligned}

在想动态规划的时候，可以先从暴力搜索的角度来想，再考虑优化其中的重复过程，降低复杂度的阶数。这道题里这种思路非常有效，我的代码从暴力搜索、到 :math:`O(n)`、最后自发优化到与参考答案一模一样，都是基于这个思路。

先想暴力搜索的方式。我们的做法是

1.  固定一个i
2.  扫描j，从i+1扫描到最后
3.  对每个i都做这种扫描

考虑动态规划的时候，一般会反过来想

1.  固定一个j
2.  扫描i，从0扫描到j-1
3.  对每个j都做这种扫描

代码大概会是这样子

.. code:: python

    maxGain = float("-inf")

    for j in range(1, len(A)):

        for i in range(0, j):
            maxGain = max(maxGain, f(i, j))

因为 :math:`f(i, j)` 有可以分解成两个单一变量函数的性质，所以代码会变成这样

.. code:: python

    maxGain = float("-inf")

    for j in range(1, len(A)):

        for i in range(0, j):
            maxGain = max(maxGain, f1(i) + f2(j))

立刻就能发现， ``f2(j)`` 重复计算了，所以把它放到最前面

.. code:: python

    maxGain = float("-inf")

    for j in range(1, len(A)):
        rightGain = f2(j)

        for i in range(0, j):
            maxGain = max(maxGain, f1(i) + rightGain)

但是这样并不能降低时间复杂度的阶数，迭代次数仍然是 :math:`O(n^2)` 。需要继续考虑是否存在非常严重的重复操作。上面的写法，不太容易看出重复的迭代，下面换一种写法

.. code:: python

    maxGain = float("-inf")

    for j in range(1, len(A)):
        rightGain = f2(j)
        maxLeftGain = max(map(f1, A[: j])) # 这里有重复迭代
        maxGain = max(maxGain, maxLeftGain + rightGain)

写成上面的方式，或者在纸上模拟求 :math:`f_1(i)` 的最大值的时候，就能很容易发现问题：在固定好 :math:`j` 之后，我们需要把 :math:`[0, 1, ..., j - 1]` 的每个元素都迭代一遍，计算出 :math:`[f_1(0), f_1(1), ..., f_1(j - 1)]` 从而才能计算出 :math:`\max\{f_1(0), f_1(1), ..., f_1(j - 1)\}` ，然而，在固定到 :math:`j + 1` 的时候，我们需要计算 :math:`[f_1(0), f_1(1), ..., f_1(j - 1), f_1(j)]` 从而计算出 :math:`\max\{f_1(0), f_1(1), ..., f_1(j - 1), f_1(j)\}` 。

发现问题了吧！其实 :math:`f_1(0), f_1(1), ..., f_1(j - 1)` 中的最大值在上一次固定 :math:`j` 的时候已经计算过一次了，但是到下一个 :math:`j + 1` ，这个值还是计算了一次。如果每次能把这一轮里 :math:`f_1(i)` 的最大值缓存起来，下次就无需从最前面重新迭代、计算最大值，而是可以用上一轮的最大值，和这一轮新增的值作比较，直接就可以取最大值了。

换句话说，这里利用了 :math:`\max\{\}` 的结合律

.. math::

    \begin{aligned}
        \max\{a_0, a_1, ..., a_{j - 1}, a_j\} = \max\{\max\{a_0, a_1, ..., a_{j - 1}\}, a_j\}
    \end{aligned}

这样代码变成了

.. code:: python

    maxGain = float("-inf")
    maxLeftGain = f1(0)

    for j in range(1, len(A)):
        rightGain = f2(j)
        maxGain = max(maxGain, maxLeftGain + rightGain) # 利用上一轮迭代的结果
        maxLeftGain = max(maxLeftGain, f1(j)) # 更新这一轮的缓存，给下一轮做准备

这就是标准答案了。最后再把 ``f1(), f2()`` 改成真实的函数就可以了。

比较有意思的是，上面的这个代码，不仅对这道题有效，对任何具有分解为单变量函数之和的目标函数都有效。
"""

from typing import *

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # i = 0
        # j = 1
        # maximum = A[i] + A[j] + i - j

        # while i + 1 < j < len(A) - 1:
        #     print(i, j)
        #     moveLeftTarget = A[i + 1] + A[j] + i + 1 - j
        #     moveRightTarget = A[i] + A[j + 1] + i - (j + 1)
        #     moveWholeRightTarget = A[i + 1] + A[j + 1] + i - j
        #     if moveLeftTarget == max(moveLeftTarget, moveRightTarget, moveWholeRightTarget):
        #         i += 1
        #         maximum = max(maximum, moveLeftTarget)
        #         continue
        #     elif moveRightTarget == max(moveLeftTarget, moveRightTarget, moveWholeRightTarget):
        #         j += 1
        #         maximum = max(maximum, moveRightTarget)
        #         continue
        #     else:
        #         i += 1
        #         j += 1
        #         maximum = max(maximum, moveWholeRightTarget)
        #         continue

        # return maximum

        # maximum = float("-inf")

        # for i in range(len(A) - 1):

        #     for j in range(i + 1, len(A)):
        #         maximum = max(maximum, A[i] + A[j] + i - j)

        # return maximum
        # 有人说暴力是可以过的，我信了。

        # dp = [A[0] + 0 + A[1] - 1]
        maxGain = float("-inf")
        maxLeftGain = A[0] + 0

        # for i in range(2, len(A)):
        for i, v in enumerate(A[1: ], 1):
            # dp.append(max(leftGain[: i]) + rightGain[i]) # 最naive的做法。如果能把这里的max优化掉，就可以把复杂度从O(n^2)降低到O(n)，而优化的方法也很简单。
            # dp.append(maxLeftGain + A[i] - i) # 其实还可以进一步优化，dp的历史在这里没有用到，所以可以优化掉最后一次迭代
            # maxGain = max(maxGain, maxLeftGain + A[i] - i)
            # maxLeftGain = max(maxLeftGain, A[i] + i)
            maxGain = max(maxGain, maxLeftGain + v - i)
            maxLeftGain = max(maxLeftGain, v + i)

        return maxGain
        # return max(dp) # 这里的迭代可以优化掉。不过不影响复杂度阶数，所以就算了。

# s = Solution()
# assert s.maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11
# assert s.maxScoreSightseeingPair([3, 7, 2, 3]) == 9
# assert s.maxScoreSightseeingPair([2,7,5,8,8,8]) == 15
# assert s.maxScoreSightseeingPair([1, 3, 5]) == 7