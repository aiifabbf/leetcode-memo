import collections
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if nums == []:
            return 0
        
        counter = collections.Counter({
            nums[0]: 1,
        }) + collections.Counter({
            - nums[0]: 1
        })
        
        for i, num in enumerate(nums[1: ], 1):
            counter1 = collections.Counter()
            counter2 = collections.Counter()
            for summation, times in counter.items():
                counter1[summation + num] = counter.get(summation, 0)
                counter2[summation - num] = counter.get(summation, 0)

            counter = counter1 + counter2
        print(counter)
        return counter.get(S, 0)

Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1], 1)