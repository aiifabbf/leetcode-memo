"""
给两个array，分别叫array1和array2，array2里面的元素都是不重复的，现在要按两个规则给array1

-   如果array1中的某个元素在array2出现过，就要把它们排成和array2中一样的顺序
-   如果array1中的某个元素没有在array2里出现过，把它们放到最后，按从小到大顺序排

还是用 ``sorted()`` 的自定义 ``key`` 函数的方法，想一种构造array1中元素“大小”的方法。需要注意的是，python里面不是只有数字才可以比大小的，tuple也是可以比大小的，tuple比大小的原则和字典顺序有点相似，就是先比较第一个元素的大小，如果第一个元素可以比较大小，就认为大的那个整个都大；如果第一个元素大小相等，就比较第二个元素……比如 ``(1, 2) < (1, 3), (2, 1) < (3, 0)`` 。所以这里可以把array1中的每个都映射到一个tuple上，第一维是元素在array2中的下标（如果array2中没有这个元素，就变成 ``float("inf")`` ，这样就可以间接实现如果不在array2中，自动放到最后），第二维是元素本身的值。

如果每次都用 ``array2.index()`` 来获得元素在array2中的下标就很慢，可以先遍历一遍array2，生成一个 ``dict`` ，其中key是元素的值、value是元素在array2中的下标。
"""

from typing import *

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        valuePositionMapping = dict() # 获得array2中每个元素的值和下标

        for i, v in enumerate(arr2):
            valuePositionMapping[v] = i # key是元素的值、value是元素的下标

        return sorted(arr1, key=lambda v: (valuePositionMapping.get(v, float("inf")), v)) # 按下标（如果不存在就inf）和值排序

# s = Solution()
# print(s.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
# print(s.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))