r"""
.. default-role:: math

写一个支持 ``let, add, mult`` 和变量、整数、作用域的lisp解释器。

.. 终于做出来了，虽然我还没看完编译原理……

lisp的表达式长这样

::

    (functionName arg1 arg2 ... returnValue)

整个程序最外层只能有一个表达式 [#]_ 。

不过这道题为了简单，规定只有 ``let`` 语句可以有 `2n` 个参数。 ``add, mult`` 都只能有2个参数。例子

-   ``(let x 2 y 3 x)``
-   ``(add x y)``
-   ``(mult x y)``

注意这里面除了 ``let`` 的奇数下标的参数 ``x, y`` 不能是表达式之外，其他参数统统都可以是更复杂的表达式，比如

::

    (let x 2 y 3 (add (mult (let x 3 x) y) y))

.. [#] 想到了那个偷阿波罗代码最后一页发现都是 ``)))))`` 的笑话）

三个阶段

1.  tokenize

    把表达式字符串里切分成具有意义的最小单位，这一步我挺熟练了，用 ``re`` 配合 ``(?P<Category>patternString)`` 这种形式的正则表达式来做。

2.  parse

    tokenize之后，表达式变成了一个 ``List[Tuple[str, str]]`` 类型的token list，其中每个tuple都是 ``(内容, 这个内容所在的分类)`` 。但是这个token list仍然是一维的、扁平的，没有表达出层级嵌套关系。parse的目标就是把每个token的层级结构分析出来。

    好在lisp的层级非常简单，就是遇到一个左括号就多一级、遇到一个右括号就减一级。

    ``(let x 2 (mul x))`` 这种表达式经过第一步的tokenize之后，会变成类似

    ::

        [
            ("(", "LeftParenthese),
            ("let", "Function"),
            ("x", "Variable"),
            ("2", "Number"),
            ("(", "LeftParenthese"),
            ("mul", "Function"),
            ("x", "Variable"),
            (")", "RightParenthese"),
            (")", "RightParenthese")
        ]
    
    的token list。parse的目标是把token list中的 ``(, )`` 变成真正的层级

    ::

        [
            ("let", "Function"),
            ("x", "Variable"),
            ("2", "Number"),
            [
                ("mul", "Function"),
                ("x", "Variable")
            ]
        ]

    用递归可以实现这件事。

3.  evaluate

    最终解释执行也是用递归。每次遇到用list括起来的复杂表达式，就先evaluate这个复杂表达式。

    变量、作用域非常容易，用一个dict来表示作用域的符号表就好了。每次递归到内层时，都copy一下这个符号表，因为lisp是函数式语言，讲究的是函数的纯洁性、不能产生副作用，所以内层无论发生了什么，都不能对外层作用域的符号表产生任何影响。

这一次终于用到语法树了。不过还是很容易分析的，没有涉及到（刚看的）文法、生产式之类的。

.. 怀疑Leetcode里其实根本没有涉及到文法的题目？

写的时候参考了 `Peter Norvig的这篇文章 <http://norvig.com/lispy.html>`_ 。这篇文章也被收录在 `GitHub上的一个叫build-your-own-x的仓库里 <https://github.com/danistefanovic/build-your-own-x#build-your-own-programming-language>`_ 。
"""

from typing import *

import re
import collections

class Solution:
    def evaluate(self, expression: str) -> int:
        env = {
            "add": lambda x, y: x + y, # (add x y)
            "mult": lambda x, y: x * y, # (mult x y)
        } # 全局作用域的符号表
        tokens = self.tokenize(expression) # tokenize
        tree = self.parse(tokens) # parse
        res = self.evaluateWithEnvironment(tree, env) # evaluate
        return res

    def tokenize(self, s: str) -> Iterator[Tuple[str, str]]: # parse。这一步我很熟练了
        patternString = "".join([
            r"(?P<Number>[+-]?0|[+-]?[1-9][0-9]*)", # 数字。注意是整数，所以前面可能带符号的
            r"|",
            r"(?P<Function>let|add|mult)", # 函数名
            r"|",
            r"(?P<Variable>[a-z][a-z0-9]*)", # 变量名。题目上说是小写字母跟数字
            r"|",
            r"(?P<LeftParenthese>\()", # 左括号
            r"|",
            r"(?P<RightParenthese>\))", # 右括号
        ])
        pattern = re.compile(patternString)
        tokens = map(lambda v: (v.group(), v.lastgroup), pattern.finditer(s))
        return tokens

    def parse(self, tokens: Iterable[Tuple[str, str]]) -> List: # 递归地生成语法树
        iterator = iter(tokens)
        stack = collections.deque() # 存左括号，用于判断当前token是内层还是外层token
        buffer = collections.deque() # 暂存内层内容
        res = collections.deque() # 最外层的结果集

        while True:
            token = next(iterator, None)
            if token == None: # 说明token list已经遍历完了
                break
            else:
                v, category = token
                if category == "LeftParenthese": # 遇到左括号
                    if stack: # 如果stack不为空，说明这个左括号是内层括号
                        buffer.append(token) # 不管，放入buffer，给下一层处理
                    stack.append("(")
                elif category == "RightParenthese": # 遇到右括号
                    stack.pop() # 先pop stack
                    if len(stack) == 1: # 如果pop之后，stack只剩1个元素，这个元素就是最外层的左括号，说明内层buffer已经结束
                        buffer.append(token)
                        res.append(list(self.parse(buffer))) # 递归地生成内层内容的语法树
                        buffer.clear() # 记得清空buffer，后面可能还会出现内层内容
                    # elif not stack: # stack空，说明这个右括号是整个表达式的最后一个字符，是最外层的右括号
                    #     pass # 啥也不做
                    else: # stack里剩下大于1个元素，说明这个右括号关闭的是内层内容里的某个左括号，这个右括号属于内层内容
                        buffer.append(token) # 同样啥也不做
                else: # 遇到其他东西
                    if len(stack) >= 2: # 如果属于内层内容
                        buffer.append(token) # 加入buffer，交给递归函数处理
                    else: # 属于最外层内容
                        res.append(token) # 加入结果集

        return list(res)

    def evaluateWithEnvironment(self, tree: List, env: Dict[str, Any]) -> int: # 递归地解释语法树。除了传入语法树之外，还要传入上一层的符号表，不然内层会找不到符号
        env = env.copy() # 每一层作用域的变量是继承上一层的，当前层变量的变化不影响上一层里的同名变量
        firstToken = tree[0] # 这一层的第一个token

        if firstToken[0] == "let": # let虽然也是个function，但是目前我只想到特殊处理。可能可以合并到env里
            returnValueToken = tree[-1] # 最后一个元素表示let语句的返回值。返回值也可能是更复杂的表达式
            variableTokens = tree[1: -1: 2] # 除了最后的返回值，前面1, 3, 5, ...都是变量名
            valueTokens = tree[2: -1: 2] # 2, 4, 6, ...都是值。注意值可能是更复杂的表达式

            for variableToken, valueToken in zip(variableTokens, valueTokens): # 处理赋值
                variableName, _ = variableToken
                if not isinstance(valueToken, list): # 如果值不是更复杂的表达式
                    valueToken = [valueToken] # 包装成只含有一个元素的表达式，因为我不知道会不会出现(let x 2 y x)这种情况
                env[variableName] = self.evaluateWithEnvironment(valueToken, env) # 递归地evaluate出值的结果

            if not isinstance(returnValueToken, list): # 对返回值同理，返回值如果不是更复杂的表达式
                returnValueToken = [returnValueToken] # 也包装成只含有一个元素的表达式，因为可能出现(let x 2 x)这种
            return self.evaluateWithEnvironment(returnValueToken, env)
        elif firstToken[1] == "Number": # 处理(2)这种表达式。这是合法的lisp表达式吗？）
            return int(firstToken[0])
        elif firstToken[1] == "Variable": # 处理(x)这种表达式
            return env[firstToken[0]] # 从当前作用域符号表里取得变量的值
        else: # 函数调用语句，如(add 2 3)
            aToken = [tree[1]] if not isinstance(tree[1], list) else tree[1] # 第一个参数arg1
            bToken = [tree[2]] if not isinstance(tree[2], list) else tree[2] # 第二个参数arg2
            a = self.evaluateWithEnvironment(aToken, env) # arg1也有可能是更复杂的表达式
            b = self.evaluateWithEnvironment(bToken, env) # arg2同理
            functionName = firstToken[0] # 得到函数名
            return env[functionName](a, b) # 从当前作用域的符号表里得到函数的实现，然后调用函数

# s = Solution()
# print(s.evaluate("(add 1 2)")) # 3
# print(s.evaluate("(mult 3 (add 2 3))")) # 15
# print(s.evaluate("(let x 2 (mult x 5))")) # 10
# print(s.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))")) # 14
# print(s.evaluate("(let x 3 x 2 x)")) # 2
# print(s.evaluate("(let x 1 y 2 x (add x y) (add x y))")) # 5
# print(s.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))")) # 6
# print(s.evaluate("(let a1 3 b2 (add a1 1) b2)")) # 4
# print(s.evaluate("(let x0 4 x1 -2 x2 3 x3 -5 x4 -3 x5 -1 x6 3 x7 -2 x8 4 x9 -5 (mult x2 (mult (let x0 -3 x4 -2 x8 4 (mult (let x0 -2 x6 4 (add x5 x2)) x3)) (mult (mult -7 (mult -9 (let x0 -2 x7 3 (add -10 x0)))) x6))))"))