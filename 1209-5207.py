"""
.. default-role:: math

不停地删除字符串里所有连续重复了 `k` 次的字符，直到没有这样的字符可删为止。

比如 ``deeedbbcccbdaa`` 并且 `k = 2` 时，删除过程是这样的

::

    deeedbbcccbdaa
     ^^^   ^^^    --- eee和ccc可删除
    
    ddbbbdaa
      ^^^   --- 删除完eee和ccc之后前后的字符合并，导致bbb可删除

    dddaa
    ^^^  --- 删除完bbb之后再次合并，导致ddd可删除

    aa
      --- 没有任何字符可以删除了

暴力做法就是不停地扫描字符串里连续重复出现k次的元素，删掉，合并两端变成新的字符串，再扫描……这样不停地重复下去，直到发现再也没有能删的元素为止。

用暴力的做法可以过，可是又有什么意义呢（无奈脸），面试肯定会问你更优的方法。

我想到了用stack的做法（话说这种类似消消乐的感觉都能用stack做），但我一开始发现只用一个stack好像不行，和朋友交流过后他们说确实要用2个stack。不过我后来还是想到了只用一个stack的方法，嘻嘻。最关键的事情是：

stack不要只存元素，像这样是反面教材

::
    
    底 -> 顶

    1, 2, 3, 3, 2, 2, 4, 4

因为这样的话，假设现在来了一个 ``4`` ，你只能知道stack顶端的元素是 ``4`` ，而不知道从顶端开始往下有多少个连续重复的 ``4`` ，所以stack里应该存元素、和这个元素在这一段里重复了多少次，比如 ``1, 2, 3, 3, 2, 2, 4, 4`` 在stack里这么存

::

    底 -> 顶

    (1, 1), (2, 1), (3, 2), (2, 2), (4, 2)

这样假设还是来了一个 ``4`` ，立马就可以知道这个新来的 ``4`` 可以和stack顶端的2个 ``4`` 一起凑成3个 ``4`` 。

顺便提一下如果要用暴力做法的话，标准库里有 ``itertools.groupby()`` ，用这个东西可以把字符串里连续重复的块拆分出来，比如可以把 ``aaabb`` 拆成 ``["aaa", "bb"]`` 。
"""

from typing import *

# import itertools
import collections

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # last = s

        # while True:
        #     groups = map(lambda v: "".join(v[1]), itertools.groupby(s)) # 用itertools.groupby()可以把字符串分成几个连续重复的块
        #     groups = map(lambda v: v[: len(v) % k], groups) # 删掉重复k次的字符，这里用了个小技巧，直接取substring长度对k的余数
        #     s = "".join(groups) # 删除完成之后要合并
        #     if s == last: # 如果发现这一轮操作之后字符串没有任何变化
        #         return s # 那么说明字符串里已经没有可以删除的内容了
        #     else: # 字符串有变化
        #         last = s # 下一轮接着删
        # 上面是暴力做法

        # 下面是stack的做法
        stack = [] # stack里存(v, v在这一段连续重复出现的次数)

        for v in s:
            if stack: # stack不为空
                if stack[-1][0] == v: # 如果新来的元素和顶端元素相同
                    stack[-1] = (stack[-1][0], stack[-1][1] + 1) # 可以和顶端元素凑成一段连续重复的字符串
                    if stack[-1][1] == k: # 如果这串凑好的字符串正好长度就是k
                        stack.pop() # 直接pop掉
                else: # 如果新来的元素和顶端元素不相同
                    stack.append((v, 1)) # 那也没办法了，只能先放进去了，看后面有没有机会消吧
            else: # stack为空
                stack.append((v, 1)) # 啥也别说直接放进去就完事儿了

        return "".join(map(lambda v: v[0] * v[1], stack)) # 最后stack里剩下的元素就是不能再消去的元素，把它们按出现顺序、连续重复出现次数合并起来就是最终答案了，比如剩(1, 2), (2, 2)就先把1重复2次变成11，2重复2次变成22，再把11和22连接起来

# s = Solution()
# print(s.removeDuplicates("abcd", 2)) # abcd
# print(s.removeDuplicates("deeedbbcccbdaa", 3)) # aa
# print(s.removeDuplicates(s = "pbbcggttciiippooaais", k = 2)) # ps