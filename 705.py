"""
设计HashSet

既然是HashSet，那么就要求

-   添加操作复杂度 :math:`O(1)`
-   判断是否存在复杂度 :math:`O(1)`
-   删除复杂度 :math:`O(1)`

暴力做法是直接建一个下标能覆盖所有key范围的巨大的array，因为array按下标随机访问复杂度全是 :math:`O(1)` 所以可以满足要求。

我觉得好像也可以用巨长的整数来实现。

706题是设计HashMap。
"""

from typing import *

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = [-1] * 1000001 # array的下标代表key，值如果是-1代表不存在、0代表存在

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.array[key] = 0 # 添加元素就是简单地把第key个元素设置成0

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.array[key] = -1 # 删除元素也是简单地把第key个元素设置成-1

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if self.array[key] == 0:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)