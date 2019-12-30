"""
给一个数组，如果要使它变成一串等差数列，需要在数组中间（不会插在两边）插入哪个数字？
"""

from typing import *

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if arr[1] - arr[0] != arr[2] - arr[1]: # 如果前三个数字的差分不相等，需要区分出整个数列的公差是多少
            if len(arr) == 3: # 如果数组里总共就这个三个数字
                if abs(arr[1] - arr[0]) > abs(arr[2] - arr[1]): # 比较一下两个差分
                    return (arr[1] + arr[0]) // 2
                else:
                    return (arr[2] + arr[1]) // 2
            else: # 如果不止这三个数字
                if arr[3] - arr[2] != arr[1] - arr[0]: # 再往后看，看哪个差分值出现的次数多，出现多次的那个差分值就是这个数列的公差
                    return (arr[1] + arr[0]) // 2
                else:
                    return (arr[2] + arr[1]) // 2
        else: # 如果前三个数字的差分相等
            delta = arr[1] - arr[0] # 那么整个数列的公差就是这个差分

            for i, v in enumerate(arr[2: ], 2):
                if v - arr[i - 1] != delta: # 看一下哪两个数字之间的差分不等于这个公差
                    return (v + arr[i - 1]) // 2

            return arr[0] # 还要考虑一下公差为0的时候的事情

# s = Solution()
# print(s.missingNumber([5, 7, 11, 13])) # 9
# print(s.missingNumber([15, 13, 12])) # 14
# print(s.missingNumber([1, 2, 4])) # 3
# print(s.missingNumber([0, 0, 0])) # 0
# print(s.missingNumber([1, 1, 1, 1])) # 1