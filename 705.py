"""
设计HashSet

既然是HashSet，那么就要求

-   添加操作复杂度 :math:`O(1)`
-   判断是否存在复杂度 :math:`O(1)`
-   删除复杂度 :math:`O(1)`

暴力做法是直接建一个下标能覆盖所有key范围的巨大的array，因为array按下标随机访问复杂度全是 :math:`O(1)` 所以可以满足要求。

我觉得好像也可以用巨长的整数来实现。从低位到高位依次表示key是否存在，这样

-   添加操作就是把第key位变成1

    可以用or实现，把原整数和一个只有第key位是1、其他位都是0的整数按位或。

-   判断操作就是看第key位是不是1

    可以用and实现，把原整数和一个只有第key位是1、其他位都是0的整数按位与，看结果是不是0，如果是0，说明第key位是0；如果不是0，说明第key位是1。

-   删除操作是把第key位变成0

    可以用and实现，把原整数和一个只有第key位是0、其他位都是1的整数按位与。这个只有第key位是0、其他位都是1的整数是一个只有第key位是1、其他位都是0的整数的按位非。

706题是设计HashMap。
"""

from typing import *

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.array = [-1] * 1000001 # array的下标代表key，值如果是-1代表不存在、0代表存在
        self.array = 0 # 一开始全0，表示都不存在

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        # self.array[key] = 0 # 添加元素就是简单地把第key个元素设置成0
        self.array |= 1 << key # 和0000...010...0000按位或

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        # self.array[key] = -1 # 删除元素也是简单地把第key个元素设置成-1
        self.array &= ~(1 << key) # 和1111...101...1111按位与

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        # if self.array[key] == 0:
        #     return True
        # else:
        #     return False
        if self.array & (1 << key) == 0: # 和0000...010...0000按位与，如果第key位是1，那一位不会被中间的1给mask掉，所以结果会是一个非零数，如果第key位是0，和中间的1相与还是得到0，而此时其他位也全0，所以结果是0
            return False
        else:
            return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)