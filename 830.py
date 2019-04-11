"""
把字符串按相同字符分成许多个substring（要连续），然后取出所有长度大于等于3的substring，列出这些substring的起止位置

比如 ``abbxxxxzzy`` 切成 ``a, bb, xxxx, zz, y`` ，因为 ``a, bb, zz, y`` 长度不满3，所以扔掉，只留一个 ``xxxx`` ， ``xxxx`` 在原字符串中的起止位置是3和6，所以就返回 ``[[3, 6]]`` 。

.. 最后还有一句 ``The final answer should be in lexicographic order.`` 不用管，因为test case根本没在意这个顺序，按起始位置排序就好了。

字面意思，按部就班做就好了。
"""

from typing import *

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        groups = [] # 记录所有满足条件的substring和它们的起始位置，(substring, startPosition)
        buffer = S[0] # 暂存substring
        start = 0 # 暂存起始位置
        S += "0" # 最后添个dummy char，省得出循环再收尾

        for i, v in enumerate(S[1: ], 1):
            if v == buffer[-1]: # 当前字符和buffer里的字符相等
                buffer += v # buffer延长一格
            else: # 不相等
                if len(buffer) >= 3: # 看substring长度有没有到3
                    groups.append((buffer, start)) # 到了就记录一下
                # else: # 没到直接扔掉
                #     pass
                buffer = v # 不管到没到，都要重新从这个字符开始继续数下去
                start = i # 记录起始位置

        # groups = sorted(groups, key=lambda x: x[0])
        return list(map(lambda x: [x[1], x[1] + len(x[0]) - 1], groups))

# s = Solution()
# print(s.largeGroupPositions("abbxxxxzzy"))
# print(s.largeGroupPositions("abc"))
# print(s.largeGroupPositions("abcdddeeeeaabbbcd"))