class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#'
        dp = [1]
        argmaxRadius = 0
        maxRadius = 1
        for i in range(1, len(s)):
            if i < argmaxRadius + maxRadius:
                radius = dp[2 * argmaxRadius - i]
            else:
                radius = 1
            searchRange = range(radius, min(i, len(s) - i - 1) + 1)
            for j in searchRange: # 从中心开始往两边逐个检查
                if s[i - j] == s[i + j]: # 遇到一样的
                    radius += 1
                else: # 遇到不一样的
                    break
            dp.append(radius)
            if radius > maxRadius:
                maxRadius = radius
                argmaxRadius = i
            
        s1 = argmaxRadius - maxRadius + 1 # 左边界
        s2 = argmaxRadius + maxRadius # 右边界
        return s[s1: s2].replace("#", "")

Solution().longestPalindrome("banana")