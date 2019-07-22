"""
写一个支持括号、加号、减号、正数的计算器

好像又是编译原理……先要把表达式变成token list，然后再构建AST。然而这道题不要求支持乘法和除法，不会出现运算符优先级的问题，所以好像不用AST，直接用一个stack就可以了。

用 ``re.finditer()`` 可以做到tokenize，可以把类似 ``1 + 200 - (3+4)`` 这种表达式变成

::

    '1', '+', '200', '-', '(', '3', '+', '4', ')'

一串具有最小单位语义的字符串。

得到token list之后就可以开始用stack来evaluate了

-   遇到左括号 ``(``

    啥也不说直接push到stack里就好了，因为没有什么你能做的操作。

-   遇到加号或者减号 ``+, -``

    也是啥也不说直接push到stack。

-   遇到右括号 ``)``

    稍微复杂一点。出现右括号表示当前的这个子表达式结束了，那么当前的子表达式从哪里开始呢？是从最近一次遇到的左括号 ``(`` 开始的，所以我们要不停地pop stack，直到stack弹出了一个左括号，这期间stack弹出的所有的东西就是子表达式，然后evaluate这个子表达式，把结果再push回stack就可以了。

-   遇到数字

    最复杂，首先要看stack的顶端是不是加号或者减号，如果是的话，那么加减号前面肯定也是一个数字，而且组成了类似 ``a + b`` 的结构，这时候就先pop一次，拿到加减号，再pop一次拿到被加数或者被减数，然后evaluate出结果，再push回stack。

    如果stack顶端是左括号，那也没什么办法，只能把数字push进stack。

然而这样是过不了的……有两个问题

1.  ``list`` 实在是太慢了

    我不知道Python的 ``list`` 底层是用链表还是连续数组实现的，对于stack这种需要频繁pop和push、而不需要快速随机访问的东西，用链表比较好。

    好在 ``collections`` （又是这个包）提供了一个叫做 ``deque`` 的东西，支持在左端和右端的快速pop和push，效果还不错。

2.  最后还要evaluate一次stack

    考虑这样一个表达式

    ::

        1 + (2 + 3)
                  ^

    遇到最后一个右括号的时候，stack里面的内容是

    ::

        1, +, (, 5

    因为遇到了右括号，按照上面的步骤，要pop stack直到遇到左括号。pop出的内容是 ``(, 5, )`` evaluate这个子表达式，得到5，再push回stack，这样stack变成了

    ::

        1, +, 5

    最后还要evaluate一次这个表达式才能得到最终结果，有点麻烦。
    
    可以在每次evaluate子表达式之后，把结果放回到token list的最前面，而不是push到stack里。这样的话下次从token list的最前面拿出来的token就是子表达式的值，然后遇到stack最顶端的加减号，就会自动evaluate了。

有一个巨坑必须要注意，就是 ``str.isdigit()`` 只会检测字符串那里是不是都是数字，所以如果有负号，这个方法是返回false的。解决办法是先用 ``.lstrip("+-")`` 去掉前面可能有的加减号，再用 ``.isdigit()`` 判断就好了。
"""

from typing import *

import collections
import re

class Solution:
    def calculate(self, s: str) -> int:
        patternString = "".join([
            r"(0|[1-9][0-9]*)", # group1 数字
            r"|(\+|-)", # group2 加号和减号
            r"|(\(|\))"
         ]) # group3 括号
        pattern = re.compile(patternString) # 编译pattern，这样会快
        tokens = map(lambda v: v.group(), pattern.finditer(s)) # 用generator可以省内存
        return self.evaluateTokens(tokens)

    def evaluateTokens(self, tokens: "Iterable") -> int:
        stack = collections.deque() # stack需要频繁pop和push，用deque会快很多
        buffer = collections.deque() # 因为token list现在是个generator了，所以没办法insert了，用一个deque做缓冲区

        while True:
            if buffer: # 如果缓冲区里有token
                token = buffer.popleft() # 先取缓冲区里的token
            else:
                token = next(tokens, None) # 不然就从generator里取
                if token == None: # token list和缓冲区都空了
                    break
            v = token
            if v == "(": # 左括号
                stack.append(token) # 直接push到stack顶端
            elif v == ")": # 右括号
                buffer.appendleft(stack.pop())
                stack.pop()
            elif v.lstrip("+-").isdigit(): # 数字。巨坑，.isdigit()对负数返回false
                if stack and (stack[len(stack) - 1] == "+" or stack[len(stack) - 1] == "-"): # 如果stack非空，并且顶端是加减号
                    op = stack.pop() # 得到操作符
                    thatNumber = stack.pop() # 被加数或者被减数
                    if op == "+":
                        stack.append(str(int(v) + int(thatNumber))) # evaluate一下a + b
                    else:
                        stack.append(str(int(thatNumber) - int(v))) # evaluate一下a - b
                else: # stack空
                    stack.append(token) # 只能push了
            else: # 加号或者减号
                stack.append(token) # 只能push

        if stack: # stack非空时只会有一个数字，这就是最终结果
            return int(stack[0])
        else: # stack空，说明token list空，表达式为空
            return 0

# s = Solution()
# print(s.calculate("")) # 0
# print(s.calculate("1")) # 1
# print(s.calculate("1 + 1")) # 2
# print(s.calculate("(1 + 1)")) # 2
# print(s.calculate(" 2-1 + 2")) # 3
# print(s.calculate("0-1")) # -1
# print(s.calculate("0-1+2")) # 1
# print(s.calculate("(1+(4+5+2)-3)+(6+8)")) # 23
# print(s.calculate("8+4-(1)")) # 11
# print(s.calculate("8+4-(1)+8-10")) # 9
# print(s.calculate("2-4-(8+2-6+(8+4-(1)+8-10))")) # -15
# print(s.calculate("1+7-7+3+3+6-3+1-8-2-6-1+8-0+0-2+0+10-6-9-9+0+6+4+2+7+1-4-6-6-0+6+3-7+0-4+10-2-5+6-1-3+7+7+2+0+2-8+7+2-3-8-9-6+10-7-6+3-8+5+6-7-10-6-8-10-8+1+9+1-9-1+10+10+3+7-1-10+1-0-7+0-3-3+4+7-9-10-1+4-8-3-0-1-0-3+5-10+6-6-0-6-6-7+7+10+10-5-9-10-2-8+9-2-8-7-9-0-6-5-1+1+3+8-5-8+3-9+9+6-5+0-2+0+8+8-4+6+1-2-0-10-8+1-2-8+2-2-2-4+2+5+3-9+1+9-8+9-8+7+10+1+10-9+2+2+8+7-10-8+6+6+3+0+4-1+0+7-3+8-8-4+8-6-6+3-3-9+6+4+6+7-2-0+6-10+8-2-4+3-8+1-2+8+1-2-4-3-9-4-1-3+5+9+7-8-2+7-10+7+9+1+5-5+8-3-10-7-1-7+10+3+2-8-8+0+9+3+6+8+4+2+10+8+6-1+2+10-5+5+4-2+10+7-6-5+9-9+5-5-2+5+2-1+7-8+4-2+2+2+5-10-7-0+5-8-6-10-5+9-1+1-8+10-7+2-3-3+2+3-8+4-6-7+3-0+6-6-3+1+2-6+2+3+0-4-0+3-5-1-4-0+9+5-6+3-10+0+10-4+6-6-5-6+5+3+7-4+6+2+0+10+4-3+10-10-0-10-4-8+9-5-0-0-9-8-3-2+6")) # -99
# print(s.calculate("1 + (2 + (3 + (4 + 5) + 6 + (9 + 1)+9+2+1+4) + (1 + 3 + 3) + 7) + 8")) # 69

# import os
# import sys

# with open(os.path.join(sys.path[0], "224.test")) as f:
#     print(s.calculate(f.read())) # -1946