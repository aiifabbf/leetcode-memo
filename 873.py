class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [
            [],
            [2]
        ]
        s = set(A)
        res = 2
        for i in range(2, len(A)):
            dp.append([])
            for j in range(0, i):
                if A[i] - A[j] in s and A[i] - A[j] < A[j]:
                    temp = dp[j][A.index(A[i] - A[j])] + 1
                    dp[i].append(temp)
                    res = max(res, temp)
                else:
                    dp[i].append(2)
        print(dp)
        return res if res > 2 else 0

Solution().lenLongestFibSubseq([1,2,3,4,5,6,7,8])