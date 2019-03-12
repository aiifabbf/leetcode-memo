class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        n = 1
        a = abs(dividend)
        b = abs(divisor)
        while n * b <= a:
            n += 1
        
        n -= 1
        if dividend * divisor > 0:
            return n
        else:
            return -n


s = Solution()
print(s.divide(7, -3))
print(s.divide(-7, 3))
print(s.divide(1, -3))
print(s.divide(1, 1))