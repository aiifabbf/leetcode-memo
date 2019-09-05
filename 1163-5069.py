r"""
.. default-role:: math

给一个字符串，这个字符串的所有substring（要连续）中、按字典顺序排序、最大的那个substring是什么。

暴力做法就是遍历字符串的所有substring，找到按字典顺序排列最大的那个substring。一个长度为 `n` 的字符串有 `O(n^2)` 个substring，按字典顺序比较两个长度分别为 `k, l` 的字符串的大小最坏情况复杂度是 `O(\min\{k, l\})` ，所以暴力做法的复杂度应该是 `O(n^2)` 和 `O(n^3)` 之间。题目的数据规模是 `10^5` ，应该是想要一种 `O(n)` 的做法。

想办法优化一下，这么 `O(n^2)` 个substring真的全部都要互相比较一遍吗？其实不用 [1]_ ，只要比较其中的 `n` 个substring就够了。你想，以第i个字符开头的所有substring，按字典顺序排序、最大的那个substring一定是从i到字符串结尾的那个substring，比如

::

    leetcode
       ^----

以 ``t`` 开头的substring总共有5个

-   ``t``
-   ``tc``
-   ``tco``
-   ``tcod``
-   ``tcode``

显然按字典顺序排序最大的那个是 ``tcode`` 。

所以实际上我们只需要确定

-   ``s[0: ]``
-   ``s[1: ]``
-   ...
-   ``s[i: ]``
-   ...
-   ``s[n - 1: ]``

总共n个substring的字典顺序就可以了。这样暴力的复杂度在 `O(n)` 到 `O(n^2)` 之间。

.. [1] 这个优化是我在想这道题是不是应该用DP的时候想到的。

照理说 `O(n^2)` 应该是过不了的，但是很奇怪比赛的时候居然过了，我也觉得很惊讶，大概是test case不太好、或者python是不是在字符串比较上做了究极优化。很容易就可以构造出最坏情况的test case，比如

::

    aaa...aaa
    ^-------^--- 10^5个a
"""

from typing import *

class Solution:
    def lastSubstring(self, s: str) -> str:
        return max(s[i: ] for i in range(len(s)))

# s = Solution()
# print(s.lastSubstring("abab")) # bab
# print(s.lastSubstring("leetcode")) # tcode
# print(s.lastSubstring("zrziy")) # zrziy