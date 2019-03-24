"""
给一个set，里面的元素都是数对 :math:`(a_i, b_i)` ，其中 :math:`a_i` 是人的高度、 :math:`b_i` 是这个人前面身高大于等于他的人数。把这个set排好序，使得里面的每个数对都放对位置。
"""

from typing import *

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        