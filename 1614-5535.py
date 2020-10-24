r"""
.. default-role:: math

括号的最大嵌套深度

比如给 ``(1+(2*3)+((8)/4))+1`` ，去掉所有不是括号的字符，变成 ``(()(()))`` ，那么最大深度是3。为啥呢，这么展开写就懂了

::

    (
        ()
        (
            ()
        )
    )

就很像HTML

::

    <section>
        <h2></h2>
        <p>
            <ul></ul>
        </p>
    </section>

写成文档树是

::

        section
        /     \
       h2      p
              /
             ul

等效于求这个树的深度，也就等价于求前根遍历这个树的过程中，函数帧的最大深度了。

所以用个stack就好了。
"""

from typing import *


class Solution:
    def maxDepth(self, s: str) -> int:
        stack = [] # 还可以进一步优化成数字
        res = 0

        for v in s:
            if v == "(": # 遇到(说明调用了别的函数，函数帧又深了一层
                stack.append(v)
            elif v == ")": # 遇到)说明从某个函数返回，函数帧变浅了一层
                stack.pop()

            res = max(res, len(stack)) # 记下过程中函数帧的最大层数

        return res
