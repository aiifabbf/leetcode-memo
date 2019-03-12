# 实现一个数据结构，可以实现前缀匹配加和

from typing import *

import collections
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = collections.Counter()

    def insert(self, key: str, val: int) -> None:
        # for right in range(1, len(key) + 1):
            # self.counter[key[: right]] += val
        self.counter[key] = val

    def sum(self, prefix: str) -> int:
        return sum(value for index, value in self.counter.items() if index.startswith(prefix))


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
mapSum = MapSum()
mapSum.insert("apple", 3)
assert mapSum.sum("ap") == 3

mapSum.insert("app", 2)
assert mapSum.sum("ap") == 5

mapSum = MapSum()
mapSum.insert("aa", 3)
assert mapSum.sum("a") == 3
mapSum.insert("aa", 2)
assert mapSum.sum("a") == 2