"""
设计一种数据结构，可以实现

-   :math:`O(1)` 插入操作
-   :math:`O(1)` 删除操作
-   :math:`O(1)` 随机返回一个元素，概率按元素出现的次数加权

比380题多的地方在于，元素可能重复，而且随机抽取的时候概率分布要符合元素出现的次数，比如1出现了2次，而2出现了1次，那么抽取到1的概率应该是2的两倍。
"""

import random
import collections

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = collections.Counter()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if self.counter[val] == 0:
            self.counter[val] += 1
            return True
        else:
            self.counter[val] += 1
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.counter[val] == 0:
            return False
        else:
            self.counter[val] -= 1
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choices(list(self.counter.keys()), list(self.counter.values()))[0] # random.choices() 有这种带权抽取功能


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()