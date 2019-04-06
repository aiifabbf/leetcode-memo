"""
用queue实现stack

.. note:: 镜像题目232用stack实现queue
"""

from typing import *

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        tempQueue = []

        while self.queue:
            element = self.queue.pop(0)
            if self.queue:
                tempQueue.append(element)
            else:
                break

        while tempQueue:
            self.queue.append(tempQueue.pop(0))

        return element

    def top(self) -> int:
        """
        Get the top element.
        """
        tempQueue = []
        
        while self.queue:
            element = self.queue.pop(0)
            if self.queue:
                tempQueue.append(element)
            else:
                tempQueue.append(element)
                break

        while tempQueue:
            self.queue.append(tempQueue.pop(0))

        return element

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()