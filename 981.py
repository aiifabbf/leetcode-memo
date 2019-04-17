"""
设计一种类似HashMap的东西，但同时要记录item被加入的时间戳，查询的时候会给key和时间戳，要求快速返回给定时间戳之前、但离给定时间戳最近的value。

难点是要在查询的时候用二分搜索，如果不用二分搜索，会超时。
"""

from typing import *

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        temp = self.store.get(key, [])
        temp.append((value, timestamp)) # 存的时候就存一个tuple吧
        # temp.sort(key=lambda x: x[1]) # timestamp are stricly increasing
        self.store[key] = temp

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        else:
            array = self.store[key] # 这里必须用二分搜索，不然会超时
            left = 0
            right = len(array)

            while left < right:
                middle = (left + right) // 2
                if array[middle][1] < timestamp:
                    left = middle + 1
                elif array[middle][1] > timestamp:
                    right = middle
                else: # 可以加一行这个提前退出
                    return array[middle][0]

            if array[middle][1] <= timestamp: # 出来的时候还是要检查一下对不对的
                return array[middle][0]
            else:
                return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)