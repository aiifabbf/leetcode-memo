"""
设计LRU缓存

LRU是least recently used的意思，也就是每次存、取都算一次used，在缓存容量不足、需要替换缓存的时候，把访问时间距离现在最远的那个格子替换成新的内容。

原理虽然很简单，但是如果直接把访问时间戳和内容放在一个array里，每次存、取的时候去遍历这个array的话，实在是太慢了。

这时候你可能会想到用set来做，因为判断一个元素是否在set里的复杂度是 :math:`O(1)` ，但是这样只能解决取的问题，存的时候，你还是不知道set里哪个内容的访问时间戳是最小的，还是需要遍历一遍set里所有的元素，找到那个访问时间距离现在最远的元素。

或者换一个思路，用array中元素的顺序来表示访问时间戳这个信息，下标越大表示访问时间戳越大，也就是访问时间离现在越近。

所以我们好像需要一种set和array的结合体

-   能像set一样，访问复杂度是 :math:`O(1)`
-   能像array一样，能记忆访问的顺序

这种数据结构叫OrderedDict，java里面叫LinkedHashMap，底层确实是用array和dict结合来实现的，array用来存储key的顺序，dict用来存key和value对。
"""

from typing import *

import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int: # 取操作也算一次访问
        if key in self.mapping: # 如果key存在
            self.mapping[key] = self.mapping.pop(key) # 先取出来再放回去，这样当前元素的时间戳最大。无论是java还是python，更新一个已有的key的value是不会改变key的顺序的，所以一定要先取出来再放回去
            return self.mapping[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None: # 存操作可能涉及到缓存替换
        if key in self.mapping: # 如果key存在，更新value
            self.mapping[key] = self.mapping.pop(key) # 还是先取出来再放回去
            self.mapping[key] = value # 设置成新的value
        else: # key不存在
            if len(self.mapping) == self.capacity: # 要检查缓存容量，如果达到容量上限，要替换缓存
                self.mapping.popitem(last=False) # 把访问时间距今最远的缓存删掉
            self.mapping[key] = value # 插入新的(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# s = LRUCache(2)
# s.put(1, 1)
# s.put(2, 2)
# print(s.get(1)) # 1
# s.put(3, 3)
# print(s.get(2)) # -1
# s.put(4, 4)
# print(s.get(1)) # -1