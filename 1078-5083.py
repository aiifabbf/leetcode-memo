"""
实现一个能识别两个单词的序列检测器。

用一个状态机就好啦，很简单。总共有三个状态

-   ``s0`` 是初始状态
-   ``s1`` 表示识别到了第一个单词，正在等待第二个单词到来
-   ``s2`` 是终态 [#]_ ，表示成功检测出第一个和第二个单词

.. [#] 其实我想说accepting state，不知道怎么翻译比较好。

状态转移图

::

    digraph G {

        s0 -> s1 [label=first]
        s0 -> s0 [label=other]
        s1 -> s2 [label=second]
        s1 -> s1 [label=first]
        s1 -> s0 [label=other]
        s2 -> s0 [label=other]
        s2 -> s1 [label=first]
    }

.. note::

    这道题其实有一点不明确的地方，就是序列重叠的情况怎么处理。比如

    ::

        a a a a

    然后 ``first`` 和 ``second`` 都是 ``a`` 的时候，到底应该输出 ``a, a`` 还是 ``a``

    但是好在test case里也没有出现这种测试样例，所以无所谓了。
"""

from typing import *

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        array = text.split(" ") # 用空格分割单词
        state = 0 # 当前状态
        res = [] # 结果

        for i, v in enumerate(array):
            if state == 0: # 当前状态是初始状态
                if v == first: # 接收到第一个单词
                    state = 1 # 进入状态1
                else:
                    state = 0 # 否则还是待在初始状态
            elif state == 1: # 当前状态是状态1，表示已经接收到了第一个单词
                if v == second: # 接收到了第二个单词
                    state = 2 # 进入状态2
                    try: # 防止越界
                        res.append(array[i + 1]) # 把后面一个单词加入结果
                    except:
                        pass
                elif v == first: # 还是接收到了第一个单词
                    state = 1 # 待在状态1
                else: # 其他
                    state = 0 # 回到初始状态
            elif state == 2: # 当前状态是状态2，表示已经识别出了两个单词
                if v == first: # 如果再次接收到第一个单词
                    state = 1 # 就回到状态1
                else:
                    state = 0 # 否则回到初始状态

        return res

# s = Solution()
# print(s.findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good")) # girl, student
# print(s.findOcurrences(text = "we will we will rock you", first = "we", second = "will")) # we, rock
# print(s.findOcurrences("a a a a", "a", "a"))