"""
解析一种语言。这种语言是类似 ``E k[E] E`` 的形式，其中 ``k`` 是重复的次数、 ``E`` 可以是嵌套的另一个表达式、或者是几个字母。

我的思路是只解析最外层的内容，内层的内容用递归交给下一层处理。

头条面试被问到了这个题目，没答出来，很尴尬。马上下午去听了两节编译原理课，发现这个好像是某种上下文无关文法，叫CFG。CFG的解析挺复杂的，但是本质上还是有限状态机，所以我这里简单分析了一波，就做出来了。
"""

from typing import *

class Solution:
    def decodeString(self, s: str) -> str:
        # print(s)
        if not ("[" in s or "]" in s):
            return s
        else:
            res = "" # 存放结果
            buffer = "" # 存放内层的还未解析、将要交给下一层处理的内容
            times = "" # 下层处理完之后，乘以次数
            stack = [] # 空stack表示外层、非空stack表示遇到的字符都是内层字符，不做处理

            for i, v in enumerate(s):
                if v == "[": # 遇到左括号
                    buffer = buffer + v # 这里不判断左括号是外层左括号还是内层左括号
                    stack.append(v)
                elif v == "]": # 遇到右括号，有可能表示内层字符结束了
                    buffer = buffer + v
                    stack.pop()
                    if stack == []: # stack空，说明buffer里面的内容是内层字符，并且已经结束
                        res = res + self.decodeString(buffer[1: -1]) * int(times) # 去掉buffer最外面的一对括号，剩下的交给下一层处理
                        times = "" # 重置次数
                        buffer = "" # 重置buffer
                    else: # stack非空，说明buffer里面的内层字符还没有结束，继续等待，直到stack变成空的，才说明内层字符已经结束
                        pass
                elif v.isnumeric(): # 遇到数字，有可能是外层的表示重复次数的数字，也有可能是内层字符的一部分
                    if stack == []: # stack为空，说明这个数字是外层的
                        times = times + v # 存起来
                    else: # stack非空，说明这个数字是内层字符，不用管，直接放入buffer等待内层处理
                        buffer = buffer + v
                else: # 遇到英文字母，还是一样的道理，有可能是外层的、普通的、无需重复的字母，也有可能是内层字符
                    if stack == []: # stack空，说明是这个字母属于外层，并且无需重复
                        res = res + v # 那么直接追加到最终结果里就可以了
                    else: # stack非空，说明这个字母是内层字符
                        buffer = buffer + v # 和数字一样，不用管，直接放入buffer交给下一层处理

            res = res + buffer # 出循环的时候要检查buffer是否为空
            return res

# s = Solution()
# print(s.decodeString("")) # 
# print(s.decodeString("abc")) # abc
# print(s.decodeString("3[a]2[bc]")) # aaabcbc
# print(s.decodeString("3[a2[c]]")) # accaccacc
# print(s.decodeString("2[abc]3[cd]ef")) # abcabccdcdcdef
# print(s.decodeString("a13[a]2[bc]")) # aaaabcbc