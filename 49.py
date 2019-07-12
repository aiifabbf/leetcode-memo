"""
把一组array按anagram归类

如果两个字符串的直方图完全一样，也就是说如果统计两个字符串中每个字符出现的频数，发现完全一样，就称这两个字符串互为anagram。其实说直方图，有点限制思维了，因为目标是要找到一种快速判断两个字符串是否互为anagram的方法，而用 ``Counter`` 做直方图是很慢的，关键是 ``Counter`` 是不可hash的，所以要放到结果集里面还需要变成可hash的东西。不管怎样， 用 ``Counter`` 至少是能过的。

后来我想到了直接计算其中每个字符的hash、然后再全部相加的方法，虽然这种理论上是有撞hash的风险的，但是因为python的 ``hash()`` 返回的是一个63位的int，非常非常大，如果两个字符串不互为anagram，它们每个字符分别hash再相加之后得到的int相等的概率非常非常小。

提交了之后看了答案发现可以直接给字符串排序，因为如果两个字符串互为anagram，按字典顺序排列它们得到的字符串相等，如果两个字符串不互为anagram，按字典顺序排列他们得到的字符串不相等。

答案里还有一种是不用 ``Counter`` ，用一个长度26的tuple来存每个字母出现的次数。但是好像速度不是很快。

实测hash和排序最快。
"""

from typing import *

import collections
import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        ordOfA = ord("a")

        for v in strs:
            # counter = collections.Counter(v)
            # key = tuple(sorted(counter.most_common()))
            # 用counter是绝对不会出错的方法，可惜太慢

            # key = sum(map(hash, v))
            # 其实有撞hash的风险

            # key = "".join(sorted(v))
            # 其实排序一下就好了……

            counter = [0] * 26

            for letter in v:
                counter[ord(letter) - ordOfA] += 1

            key = tuple(counter)
            res[key] = res.get(key, []) + [v]

        return list(res.values())

# s = Solution()
# print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))