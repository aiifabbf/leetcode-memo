"""
算出逆波兰式（后缀表达式）的值。

挺简单的，算是学了算法和数据结构之后，用stack的基本操作吧。具体做法是

-   遇到数字就放入stack
-   遇到符号就从stack一下子弹出两个数字，算完之后再放入栈
"""

from typing import *

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for v in tokens:
            # if v.isnumeric(): # 这里坑了，负数是会false的
            if v not in ["+", "-", "*", "/"]:
                stack.append(int(v))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if v == "+":
                    stack.append(operand1 + operand2)
                elif v == "-":
                    stack.append(operand1 - operand2)
                elif v == "*":
                    stack.append(operand1 * operand2)
                else:
                    # stack.append(operand1 // operand2) # 这里是第二个坑，//是不对的
                    stack.append(int(operand1 / operand2))
            # print(v, stack)
        
        return stack.pop()

s = Solution()
# print(s.evalRPN(["4","13","5","/","+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))