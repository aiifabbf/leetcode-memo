"""
只用stack实现queue

一个标准stack只允许这些操作

-   ``push()`` 放元素到顶端

    对应py就是 ``list.insert(0, x)``

-   ``peek()`` 得到最顶端的元素（但是不删除）

    对应py就是 ``list[-1]``

-   ``pop()`` 得到最顶端的元素（同时删除）

    对应py就是 ``list.pop()``

-   ``isEmpty()`` 判断一个stack是否为空

    对应py就是 ``list == []``

一个标准queue只允许这些操作

-   ``push()`` 放元素到队列尾部

    对应py就是 ``list.append(x)``

-   ``peek()`` 得到队列最前面的元素（但是不删除）

    对应py就是 ``list[0]``

-   ``pop()`` 得到队列最前面的元素（同时删除）

    对应py就是 ``list.pop(0)``

-   ``isEmpty()`` 判断一个queue是否为空

    对应py就是 ``list == []``

.. note:: 镜像题目225用queue实现stack
"""

from typing import *

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None: # 放元素到queue尾部
        """
        Push element x to the back of queue.
        """
        self.stack.append(x) # stack.push(x)

    def pop(self) -> int: # 得到queue最前面的元素，同时删除
        """
        Removes the element from in front of queue and returns that element.
        """
        tempStack = [] # 建一个临时stack

        while self.stack:
            tempStack.append(self.stack.pop()) # 把原stack里的所有元素，按顶端到低端的顺序、全部pop出来，放入临时stack。这样临时stack最顶端的元素就是queue最前面的元素

        res = tempStack.pop() # 取出临时stack最顶端的元素，同时删除

        while tempStack:
            self.stack.append(tempStack.pop())

        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        tempStack = []

        while self.stack:
            tempStack.append(self.stack.pop())

        res = tempStack[-1]

        while tempStack:
            self.stack.append(tempStack.pop())

        return res

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()