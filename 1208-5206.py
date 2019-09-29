"""
.. default-role:: math

找累加和小于等于K的最长substring（要连续）的长度。

题目把这个问题的核心包装了一下：给两个长度相同的字符串 ``s, t`` ， ``s`` 的第 `i` 个字符 ``s[i]`` 变成 ``t[i]`` 的花费是各自的ASCII码的差值 `|s_i - t_i|` ，现在给一个最大花费 ``maxCost`` ，要在不超过这个预算的前提下，找到一个最长的substring ``s[i: j]`` ，把它变成 ``t[i: j]`` 。

我一开始没想到积分应该怎么做，用滑动窗口解决了，但是后来又突然想到积分确实能做这道题，而且也很简单。

滑动窗口的方法很简单，先算出把 ``s[i]`` 变成 ``t[i]`` 的花费 ``delta[i]`` ，然后遍历 ``delta`` ，同时维护一个窗口。

遍历到 ``delta[i]`` 的时候，如果发现窗口的累加和加上当前遍历到的 ``delta[i]`` 之后的和大于最大花费了，就把窗口最前面的元素删掉，再看看现在窗口的累加和加上 ``delta[i]`` 能不能小于或者等于最大花费，如果还是不能，继续删窗口的第一个元素……如果删完了都没法小于等于最大花费，那么窗口就只能空着；如果发现删掉了某个元素之后可以小于等于最大花费，那就恭喜！把 ``delta[i]`` 加到窗口的末尾，然后记录一下当前的长度。最后的结果就是每次记录的窗口长度的最大值了。

下面说说积分的方法。我还是更喜欢积分的方法，因为感觉上去更直观、易懂。

首先当然还是要算出把 ``s[i]`` 变成 ``t[i]`` 的花费 ``delta[i]`` 。然后给 ``delta`` 做一次积分，这样的话，计算 ``delta`` 的任意一个substring的累加和的复杂度都是 `O(1)` ，只要 ``integral[j] - integral[i]`` 就能得到 ``sum(delta[i: j])`` 了。

接下来遍历每个积分项 ``integral[j]`` ，遍历到每个积分项的时候，从 ``integral[0: j]`` 里搜索最靠左的 ``integral[i]`` ，使得 ``integral[j] - integral[i] <= maxCost`` 即 ``sum(delta[i: j]) <= maxCost`` 。为什么要最靠左？因为要找尽量长的substring，所以 `i` 越小越好。

问题在于每次都从 ``integral[0: j]`` 也就是从 ``i = 0`` 开始找起，这样复杂度和暴力做法没有区别，都是 `O(n^2)` 。怎么办？有办法的。

观察发现 ``delta`` 里面每一个数字都是非负数，所以 ``delta`` 的积分 ``integral`` 是一个单调递增（不一定严格递增）的数列，也就是一定有 ``integral[j] <= integral[j + 1]`` 。

所以其实我们不用每次都从 ``i = 0 `` 开始找，因为上一次找到了一个 ``integral[i]`` 使得 ``integral[j] - integral[i] <= maxCost`` 之后，由于 ``integral[j] <= integral[j + 1]`` ，所以对于 ``integral[j + 1]`` 来说，能使它满足 ``integral[j + 1] - integral[k] <= maxCost`` 的 ``integral[k]`` 一定要么就是 ``integral[i]`` 这一项、要么就在 ``integral[i]`` 的右边。

所以我们只要从上次停下的地方开始找起就好了，这样复杂度降低到了 `O(n)` 。
"""

from typing import *

import itertools

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # delta = list(map(lambda v: abs(ord(v[0]) - ord(v[1])), zip(s, t)))
        # res = 0
        # summation = 0 # 窗口的累加和，省得每次都要重新计算
        # window = [] # 窗口

        # for v in delta: # 遍历delta里的每个元素
        #     if summation + v <= maxCost: # 如果发现窗口累加和加上delta[i]可以小于等于最大花费
        #         window.append(v) # 只管往窗口里加就是了
        #         summation = summation + v
        #     else: # 如果发现窗口累加和加上delta[i]之后大于最大花费了
        #         while window: # 要保证非空窗口，不然pop出错
        #             summation -= window.pop(0) # 删掉窗口最前面的元素
        #             if summation + v <= maxCost: # 看看这个之后还能不能使得窗口累加和加上delta[i]之后小于等于最大花费，如果可以
        #                 window.append(v) # 往窗口里加就是了
        #                 summation += v
        #                 break

        #     res = max(res, len(window))

        # return res
        # 上面是滑动窗口方法（我也不明白为啥叫滑动窗口）

        # 我最喜欢的积分方法
        delta = list(map(lambda v: abs(ord(v[0]) - ord(v[1])), zip(s, t))) # delta[i]就是把s[i]变成t[i]的花费
        integral = [0] + list(itertools.accumulate(delta)) # 给delta做一次积分，这样integral[j] - integral[i] == sum(delta[i: j]) == 把s[i: j]变成t[i: j]的总花费
        i = 0 # 满足integral[j] - integral[i] <= maxCost的i
        res = 0 # 当前为止遇到的最长的满足条件的substring的长度

        for j in range(1, len(integral)): # 遍历每个积分项integral[j]

            while i < j: # 往前面找一个最靠左的integral[i]使得integral[j] - integral[i] <= maxCost。也有可能找不到的，这时候就限制i <= j，因为再往后面找也没有意义
                if integral[j] - integral[i] <= maxCost: # 很幸运，找到了
                    res = max(res, j - i) # 更新最长substring长度记录
                    break # 不用再往右找了，当前这个已经是对于当前这个j来说最长的符合条件的substring了
                else: # 没找到
                    i += 1 # 继续找

        return res

# s = Solution()
# print(s.equalSubstring(s = "abcd", t = "bcdf", maxCost = 3)) # 3
# print(s.equalSubstring(s = "abcd", t = "cdef", maxCost = 3)) # 1
# print(s.equalSubstring(s = "abcd", t = "acde", maxCost = 0)) # 1
# print(s.equalSubstring("pxezla", "loewbi", 25)) # 4
# print(s.equalSubstring("abcd", "cdef", 1)) # 0