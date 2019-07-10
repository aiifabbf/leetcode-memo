"""
.. default-role:: math

用一种奇怪的方式重新排列字符串。

具体方式是先从上往下排 `n` 个字符，然后从倒数第二行开始从下往上再排 `n - 2` 个字符，然后再从上往下排 `n` 个字符……直到所有字符都用完。排完之后，从左到右一行一行输出字符。

比如给 ``paypalishiring`` （怀疑paypal软广），排3行，变成

::

    p a h n
    aplsiig
    y i r

然后按正常阅读顺序输出

::

    pahnaplsiigyir

没什么好说的，就按要求来吧。首先既然是n行，那就创建n个list，用来存每一行的字符。然后每次pop出原字符串最前面的字符，追加到对应下标的list里。

list下标的顺序是两部分连接在一起、再不停地反复，所以可以用一个 ``itertools.chain()`` 把两部分连接起来，再用 ``itertools.cycle()`` 不停地反复。

第一部分是 ``0, 1, 2, ... n - 1`` ，所以是 ``range(n)`` ；第二部分是 ``n - 2, n - 3, n - 4, ..., 1`` ，所以是 ``range(n - 2, 0, -1)`` 。
"""

from typing import *

import itertools

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        charList = list(s) # 先变成list，这样才能pop
        res = [[] for _ in range(numRows)] # 存结果

        for rowIndex in itertools.cycle(itertools.chain(range(numRows), range(numRows - 2, 0, -1))): # 0, 1, 2, ..., n - 1; n - 2, n - 3, ..., 1不停反复
            if charList == []: # 没有字符了
                break
            else:
                char = charList.pop(0) # 取最前面的字符
                res[rowIndex].append(char) # 追加到对应位置的list里

        return "".join(sum(res, [])) # 把list拼起来再拼成字符串

# s = Solution()
# print(s.convert("paypalishiring", 3))