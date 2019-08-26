"""
.. default-role:: math

定义一个函数 `f(s)` ，定义是字符串 ``s`` 里ascii值最小的那个字符在 ``s`` 中出现的次数。给一个string array ``queries`` 和一个string array ``words`` ，返回一个array ``answer`` ，其中 ``answer[i]`` 是 ``words`` 中满足 ``f(w) > f(queries[i])`` 的 ``w`` 个数。

计算 `f(s)` 用 ``Counter`` 秒做。

后面query本质上就是二分搜索，也不用多说了。注意要用 ``bisect_right()`` 而不是 ``bisect_left()`` ，设想

::

    1 2 2 2 3 4

其中 ``queries[i] = 2`` ，如果是 ``bisect_left()``

::

    1|2 2 2 3 4
     ^

多算了 ``2 2 2`` ，不对。如果是 ``bisect_right()``

::

    1 2 2 2|3 4
           ^

是正确答案。
"""

from typing import *

import collections
import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        wordFrequencies = [] # 记录words里每个元素的f(w)

        for word in words:
            counter = collections.Counter(word) # 统计这个词中每个字符出现的次数
            wordFrequencies.append(counter[min(counter.keys())]) # 得到f(w)。分为两步：先取得ascii值最小的那个字符，然后取得那个字符在词中出现的次数

        wordFrequencies.sort() # 排序
        length = len(words)
        res = []

        for query in queries:
            counter = collections.Counter(query) # 统计直方图
            queryFrequency = counter[min(counter.keys())] # 得到f(queries[i])
            right = bisect.bisect_right(wordFrequencies, queryFrequency) # 用二分搜索找到f(queries[i])应该插入的位置
            res.append(length - right) # 总长度减去插入的位置就是满足条件的词的个数

        return res

# s = Solution()
# print(s.numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"])) # [1]
# print(s.numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"])) # [1, 2]