"""
找到一个数组的所有递增（不是严格递增）subsequence。

中规中矩的动态规划，特别好做。把 ``dp[i]`` 记为以第i个元素结尾的所有递增subsequence，遍历到第i个元素的时候，再往前找有没有小于等于第i个元素的元素，如果有，假设是第j个元素小于等于第i个元素，把以这些元素结尾的所有递增subsequence，也就是 ``dp[j]`` 抄过来，逐个追加第i个元素上去。

因为题目要求不能重复，所以记录递增subsequence的时候可以用tuple，然后最后用一个set套一套，去重之后再map变成list。

此外题目还要求subsequence的长度要大于等于2，这个也非常好办，用一个filter过滤掉所有不满足要求的subsequence就好了。
"""

from typing import *

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if nums:
            dp = [
                [
                    (nums[0], ) # 以第0个元素结尾的所有递增subsequence，当然只有第0个元素自己啦
                ]
            ]

            for i, v in enumerate(nums[1: ], 1): # 遍历
                allIncreasingSubsequencesEndingHere = [
                    (v, )
                ] # 以第i个元素结尾的所有递增subsequence

                for j, w in enumerate(nums[: i]): # 往前遍历
                    if w <= v: # 如果第j个元素小于等于第i个元素
                        allIncreasingSubsequencesEndingHere += [subsequence + (v, ) for subsequence in dp[j]] # 把dp[j]抄过来，逐个追加上第i个元素

                dp.append(allIncreasingSubsequencesEndingHere)

            return list(filter(lambda v: len(v) > 1, map(list, set(sum(dp, []))))) # 先合并dp，然后去重，然后全部tuple变成list，然后过滤掉长度小于2的
        else:
            return []

# s = Solution()
# print(s.findSubsequences([4, 6, 7, 7]))