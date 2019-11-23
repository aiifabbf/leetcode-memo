"""
给一个字符array、一个target字符，从字符array里面找出第一个比target字符字典序大的字符。如果不存在，返回字符array的第一个字符
"""

from typing import *

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        for letter in letters: # 遍历字符array
            if letter > target: # 发现了第一个比target大的字符
                return letter
        else: # 没有发现比target大的字符
            return letters[0]

        # 感觉也可以用二分搜索做

# s = Solution()
# print(s.nextGreatestLetter(list("cfj"), "a")) # c
# print(s.nextGreatestLetter(list("cfj"), "c")) # f