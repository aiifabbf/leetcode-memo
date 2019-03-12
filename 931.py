class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if A == [] or A == [[]]:
            return 0
        if len(A) == 1:
            return A[0][0]
        lastRowCost = A[0]
        for index, row in enumerate(A[1: ], 1):
            leftCost = [row[0] + min(lastRowCost[0], lastRowCost[1])]
            rightCost = [row[-1] + min(lastRowCost[-1], lastRowCost[-2])]
            middleCost = []
            for i, value in enumerate(row[1: -1], 1):
                middleCost.append(value + min(lastRowCost[i - 1: i + 2]))
            lastRowCost = leftCost + middleCost + rightCost
        return min(lastRowCost)