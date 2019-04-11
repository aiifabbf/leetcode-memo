"""
设计一种数据结构，可以实现

-   :math:`O(1)` 插入操作
-   :math:`O(1)` 删除操作
-   :math:`O(1)` 随机返回一个元素，概率服从均匀分布
"""

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bag = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.bag:
            self.bag.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.bag:
            self.bag.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.sample(self.bag, 1)[0] # 这里不能用random.choice()因为这个

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()