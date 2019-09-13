"""
array A里面有哪些字符串的直方图能完全覆盖array B里面每个字符串的直方图？

暴力做法是把array A里面的每个字符串都做出直方图，然后和array B里面每个字符串的直方图比较，看看能不能覆盖，假设直方图比较的操作是 `O(1)` （当然只能假设），array A的长度是 `n` ，array B的长度是 `m` ，那么复杂度是 `O(nm)` 。

想一想哪里可以优化。我发现可以把array B里所有字符串的直方图先做一个或操作，全部合并成一个最大的直方图，然后把array A里每个字符串的直方图和这个大直方图作比较。这样做和一个一个对比效果相同，但是复杂度就变成 `O(n)` 了。

啥叫合并呢？就是取每个字符在array B中的字符串里出现次数的最大值。比如 ``a`` 在

-   ``amazon`` 里出现了2次
-   ``apple`` 里出现了1次
-   ``facebook`` 里出现了1次
-   ``google`` 里出现了0次（没出现）

那么最后合并的结果里 ``a`` 出现了2次（取自 ``apple`` 里出现了2次 ``a`` ），又如 ``z`` 在

-   ``amazon`` 里出现了0次
-   ``apple`` 里出现了0次
-   ``facebook`` 里出现了0次
-   ``google`` 里出现了0次

所以在最后的合并结果里 ``z`` 出现了0次。事实上我们不需要把 ``a`` 到 ``z`` 都遍历一遍，然后去B里面每个字符串里去数出现了几次（换成中文怎么办？中文有几万个字），只要分别统计出每个字符串里那些出现过的字符出现了几次，再最后合并起来就可以了。

.. 其实一图胜千言，然而这里没法画图。
"""

from typing import *

import collections
# from functools import reduce
# from operator import or_

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        universalCounter = collections.Counter() # 合并后的结果直方图

        for v in B: # 合并B所有字符串的直方图
            counter = collections.Counter(v) # 做出B中某个字符串的直方图

            for key, value in counter.items(): # key是某个出现过的字符，value是这个字符在这个字符串里出现的次数
                universalCounter[key] = max(universalCounter[key], value) # 合并直方图

            # 也可以这样
            # universalCounter = universalCounter | collections.Counter(v)

        # 甚至还可以上面全都不要，这样写
        # universalCounter = reduce(or_, map(collections.Counter, B))
        # 写起来爽但是速度好像一般，我觉得是因为每次都要重新生成一个新的Counter、频繁申请内存

        res = []

        for v in A:
            counter = collections.Counter(v)
            if all(counter[k] >= universalCounter[k] for k in universalCounter.keys()): # b是a的subset的条件是，b里面每个字符在a中都要出现，并且b里面每个字符x出现的次数小于等于x在a中出现的次数。universalCounter[x]就是字符x在b中出现的次数，counter[x]是字符在x中a中出现的次数，univesalCounter.keys()是b中出现的所有字符
                res.append(v)

        return res

# s = Solution()
# print(s.wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"])) # ["facebook","google","leetcode"]
# print(s.wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"])) # ["apple","google","leetcode"]
# print(s.wordSubsets(A = ["amazon","apple","facebook","google", "leetcode"], B = ["e","oo"])) # ["facebook","google"]
# print(s.wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"])) # ["google","leetcode"]
# print(s.wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"])) # ["facebook","leetcode"]