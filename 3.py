"""
.. default-math:: role

给一个字符串，最长的不含有重复字符的substring的长度是多少？

我想到的是用DP [#]_ 。设 ``dp[i]`` 是字符串里以第 `i` 个字符结尾的、最长的无重substring的长度。也就是说下标区间是 ``[i + 1 - dp[i], i + 1)`` 的这个substring是以第 `i` 个字符结尾的、最长的substring。

思考 ``dp[i]`` 和前面的项的关系

-   如果发现以 前（唐突空格）一个字符结尾的最长无重substring里，也就是下标区间为 ``[i - dp[i - 1], i)`` 的这个substring里，没有出现 ``s[i]`` ，那么很好，直接把 ``s[i]`` 追加在这个substring后面，就是以第 `i` 个字符结尾的最长无重substring了。这样 ``dp[i] = dp[i - 1] + 1``
-   如果发现以 前一个字符结尾的最长无重substring里，也就是下标区间为 ``[i - dp[i - 1], i)`` 的这个substring里，出现了 ``s[i]`` ，假设下标是 ``h`` ，那么从这个字符后面开始包括到 ``s[i]`` 至少能组成一个最长无重substring，也就是说，下标区间是 ``[h + 1, i + 1)`` 的这个substring是以第 `i` 个字符结尾的最长无重substring。这样 ``dp[i] = i - h``

看两个例子。比如

::
    0 1 2 3 4 5
    a b c d e f
          ^

到 ``d`` 的时候，以 前一个字符 ``c`` 结尾的最长无重substring是 ``abc`` ，长度是3，所以 ``dp[2] = 3`` ，现在发现 ``d`` 并不在 ``abc`` 里面，所以符合第一条规则， ``dp[3] = dp[2] + 1 = 4`` 。

比如

::

    0 1 2 3 4
    a b c b a
          ^

到 ``b`` 的时候，以 前一个字符 ``c`` 结尾的最长无重substring是 ``abc`` ，长度是3，所以 ``dp[2] = 3`` ，现在发现 ``b`` 在 ``abc`` 里，所以按照第二条规则，首先从 ``abc`` 里找到 ``b`` 的下标 ``h`` ，发现 ``h = 1`` ，那么下标区间 ``[h + 1, i + 1) = [2, 4)`` 的substring ``cb`` 组成了以 ``b`` 结尾的最长无重substring， ``dp[3] = 3 - 1 = 2``

现在来考虑优化的事情，按照上面的做法，复杂度还是 `O(n^2)` ，和暴力没有区别。那么来思考一下，遍历到第 `i` 个字符的之后，怎样才能快速确定以第 `i - 1` 个字符结尾的最长无重substring中含不含有第 `i` 个字符呢？这个好像很简单，用 ``set()`` 就好了， `O(1)` 判断一个元素是否存在。

那如果确定含有之后，怎样快速得到 ``h`` 的值呢？好像就要用到 ``dict()`` 了，key是字符，value是这个字符出现的下标。

所以除了 ``dp[i]`` 好像还要定义一个叫 ``seen[i]`` 的 ``dict`` ，用来表示以第 `i` 个字符结尾的最长无重substring中出现的字符（作为key）、和每个字符出现的下标（作为value）。这样每次判断起来都是 `O(1)` 。

如果不含有，那么 ``seen[i]`` 非常好办，直接就是 ``seen[i - 1]`` 加一条 ``(s[i], i)`` 的记录；但是如果含有， ``seen[i]`` 就不太好办，需要过滤掉 ``seen[i - 1]`` 里面所有value小于等于 ``seen[i - 1][s[i]]`` 的记录。

还是用上面的例子来说明

::

    0 1 2 3 4
    a b c b a
          ^

到 ``b`` 的时候，需要生成 ``seen[3]`` ，此时 ``seen[2]`` 应该是

::

    {
        "c": 2,
        "b": 1,
        "a": 0
    }

然后发现 ``b`` 这个key已经出现在 ``seen[2]`` 里面了，并且value是1，所以要把value小于等于1的记录全部删掉，也就是删掉 ``("a", 0)`` 和 ``("b", 1)`` 这两条记录。删掉之后再加上现在这个 ``b`` 的记录，这样 ``seen[3]`` 变成

.. parsed-literal::

    {
        "c": 2,
        **"b": 3,**
    }

这样每次都要重新生成dict其实也很慢，最坏情况复杂度还是 `O(n^2)` （吧） [#]_ 。所以要想个办法不要每次都重新生成新的dict。

那有没有办法复用之前的dict呢？最好能永远不创建新的，一直用老的。其实是可以的。我们发现有了 ``seen[i]`` 之后， ``dp[i]`` 其实等于 ``len(seen[i])`` 了，所以 ``dp[i]`` 这个信息是冗余的。那么我们想，有没有办法利用一下 ``dp[i]`` 的信息，节省创建dict的时间。

完全可以，其实完全没有必要每次都新建一个dict，每次直接更新 ``s[i]`` 为key的这条记录，把 ``s[i]`` 的最新位置放进去就可以了。因为 ``dp[i - 1]`` 表示以 第 `i - 1` 个字符结尾的最长无重substring的长度，暗示了 ``[i - dp[i - 1], i)`` 这个下标区间内的substring是无重的，所以遍历到 ``s[i]`` 的时候，如果发现dict里存在这个key，并且 ``seen[s[i]]`` 在 **无重区间之外** ，即如果发现 ``seen[s[i]] < i - dp[i - 1]`` 的话，直接就可以忽略，直接照第一条规则处理就好，因为此时以 第 `i - 1` 个字符结尾的最长无重substring里根本不包含 ``s[i]`` 这个字符。

还是用上面的例子

::

    0 1 2 3 4
    a b c b a
            ^

因为我们现在不新建dict了，所以到 ``b`` 处理完、即将处理 ``a`` 的时候， ``seen`` 应该是这样的

::

    {
        "b": 3, // 上一轮b的位置从1更新到了3
        "c": 2,
        "a": 0, // 现在不新建dict了，所以a的记录还保留在这里，虽然a并不在cb这个substring里
    }

以第3个字符 ``b`` 结尾的最长无重substring应该是 ``cb`` ，并没有 ``a`` ，但是因为没有新建dict，所以 ``"a": 0`` 这个记录还在dict里面。

好了现在要处理 ``a`` 了，我们发现 ``seen`` 里面是存在 ``a`` 这条记录的，显示 ``a`` 的位置是0，可是因为 ``dp[3] = 2`` ，说明以上一个字符 ``b`` 结尾的最长无重substring的下标区间是 ``[2, 4)`` ，这个区间不包括0，所以我们可以认为 ``a`` 在之前的substring里没有出现，所以放心地按照第一条规则处理就好了：让 ``dp[4] = dp[3] + 1 = 2 + 1 = 3`` ，并且更新 ``seen`` 变成

::

    {
        "b": 3,
        "c": 2,
        "a": 4, // 更新了a的最新位置
    }

这样复杂度就降到 `O(n)` 了。

``dp`` 这里也可以优化，因为我们发现遍历到第 `i` 个元素的时候，只会用到 ``dp[i - 1]`` 也就是前一项的值，所以 ``dp`` 完全没有必要是一个array，直接保存前一项的值就可以了。

.. [#] 虽然朋友说我这个做法不算DP……
.. [#] 这里复杂度我看不出来了……
"""

from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        seen = {
            s[0]: 0,
        }
        # dp = [1]
        lastDp = 1 # 因为只会用最后一项dp[i - 1]，所以直接只保存最后一项就好了
        res = 1 # 记录至今为止见到的最大的长度

        for i, v in enumerate(s[1: ], 1):
            if v not in seen: # s[i]从来没见过
                # dp.append(dp[-1] + 1)
                lastDp = lastDp + 1 # 把s[i]接在以上一个字符结尾的substring后面就好了
                seen[v] = i # 添加s[i]的记录
            # else:
            #     # dp.append(i - seen[v])
            #     lastDp = i - seen[v]
            #     # seen = {key: value for key, value in seen.items() if value > seen[v]}
            #     seen[v] = i
            # 每次新建dict太慢了
            elif seen[v] < i - lastDp: # s[i]之前见过，但是不在以前一个字符结尾的最长无重substring里，所以记录无效，和上一个case处理方法一样
                lastDp = lastDp + 1
                seen[v] = i
            else: # s[i]之前见过，并且在以前一个字符结尾的最长无重substring里，记录有效，要截断
                # dp.append(i - seen[v])
                lastDp = i - seen[v] # dp[i] = i - seen[s[i]]
                seen[v] = i

            # print(dp)
            # res = max(res, dp[-1])
            res = max(res, lastDp)

        return res

# s = Solution()
# print(s.lengthOfLongestSubstring("abcabcbb")) # 3
# print(s.lengthOfLongestSubstring("bbbbb")) # 1
# print(s.lengthOfLongestSubstring("pwwkew")) # 3
# print(s.lengthOfLongestSubstring("a")) # 1
# print(s.lengthOfLongestSubstring("abba")) # 2