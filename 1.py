r"""
.. default-role:: math

著名的two sum。

从数列 `\{a_n\}` 里找到一对 `a_i, a_j` 使得 `a_i + a_j = \text{target}` ，返回 `(i, j)` 。

暴力做法就是遍历每一对 `(i, j)` ，看 ``a[i] + a[j]`` 是否等于 ``target`` 。复杂度 `O(n^2)` 。

可以用hash table来加速查找，因为判断一个元素是否在hash table里的复杂度是 `O(1)` 。
"""

from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict() # key存之前遇到的元素的值，value存这个元素的下标

        for i, v in enumerate(nums):
            if target - v in seen: # 如果target - v见过了，那么v + (target - v)一定能凑一个target
                return [seen[target - v], i]
            else: # 暂时没有找到能和v凑一对的数字
                seen[v] = i # 记录一下v的值和位置，继续往后找

# s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))