"""
给一个只由 ``L, R`` 组成的字符串，拆成尽可能多的substring，使得每个substring里 ``L`` 的个数和 ``R`` 的个数相同。

因为是要拆成尽可能多的substring，所以有种贪婪的感觉。

我的做法是从左到右扫描，只要发现能拆的，马上就拆掉。

具体做法是记录到目前为止见过的 ``L`` 和 ``R`` 的数量，一旦发现到某个位置 ``L`` 和 ``R`` 的数量相等了，就把前面这段substring拆出来，然后重新开始计数。

比如 ``RLRRLLRLRL``

::

    RLRRLLRLRL
    ^---------- R: 1, L: 0

    RLRRLLRLRL
     ^--------- R: 1, L: 1

拆掉 ``RL`` ，然后计数清零

::

      RRLLRLRL
      ^-------- R: 1, L: 0

      RRLLRLRL
       ^------- R: 2, L: 0

      RRLLRLRL
        ^------ R: 2, L: 1

      RRLLRLRL
         ^----- R: 2, L: 2

拆掉 ``RRLL`` ，然后计数清零

::

          RLRL
          ^---- R: 1, L: 0

          RLRL
           ^--- R: 1, L: 1

拆掉 ``RL`` ，然后计数清零

::

            RL
            ^-- R: 1, L: 0

            RL
             ^- R: 1, L: 1

拆掉 ``RL`` ，然后计数清零

这样总共拆出来4个substring。
"""

from typing import *

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rCount = 0 # 从上一次拆substring结束开始到现在见过的R的数量
        lCount = 0 # 从上一次拆substring结束开始到现在见过的L的数量
        res = 0 # 到现在为止拆出来的substring的数量

        for v in s:
            if v == "R": # 如果遇到R
                rCount += 1 # R计数器+1
            elif v == "L": # 如果遇到L
                lCount += 1 # L计数器+1
            
            if rCount == lCount: # 看一下R计数器和L计数器数量是否相等，如果相等，就要把前面的substring拆出来
                rCount = lCount = 0 # 清零
                res += 1 # 又拆出来一个substring

        return res

# s = Solution()
# print(s.balancedStringSplit("RLRRLLRLRL")) # 4
# print(s.balancedStringSplit("RLLLRRRLR")) # 3
# print(s.balancedStringSplit("LLLLRRRR")) # 1