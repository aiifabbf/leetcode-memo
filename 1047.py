"""
两个两个地去掉字符串里相邻重复的字符，而且要全部去掉直到最后没有相邻重复的字符。

比如 ``abbaca`` 最后要变成 ``ca``

::

    abbaca -> aaca 去掉bb之后，两个aa又相邻重复了，所以还要继续去掉
    aaca -> ca 去掉aa之后，再也没有相邻重复了，所以就完成了

比如 ``abbbaca`` 最后要变成 ``abaca``

::

    abbbaca -> abaca 去掉bb之后，没有再相邻重复的两个字符了

一开始想用状态机做，但是做了很久都没有做出来，所以看了一下related topics，发现居然是stack，马上就有醍醐灌顶的感觉，半分钟就写出来了。

真的非常非常简单，用一个stack来做，遍历字符串里的每个字符，如果stack是空的，直接就放进去；如果stack不是空的，把这个字符和stack顶部的字符比较一下，如果相同，就把stack顶部的字符弹出，如果不相同，把这个字符放进stack。
"""

from typing import *

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []

        for v in S:
            if stack: # stack不是空的
                if stack[-1] != v: # 如果stack顶部的字符和当前字符不同
                    stack.append(v) # 把当前字符放进stack
                else: # 如果stack顶部的字符和当前字符相同
                    stack.pop() # 把stack顶部的字符弹出
            else: # stack是空的
                stack.append(v) # 直接把当前字符放进去

        return "".join(stack)

# s = Solution()
# print(s.removeDuplicates("abbaca")) # ca
# print(s.removeDuplicates("abbbaca")) # abaca