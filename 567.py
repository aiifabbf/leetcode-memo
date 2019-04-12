"""
检查一个string是不是另一个string的某个substring的anagram。

和438题差不多，438题要求输出所有下标，这一题只要求判断是不是。所以这题的代码我也是直接从438里抄过来的。
"""

from typing import *

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p = s1
        s = s2
        lengthOfP = len(p)
        lengthOfS = len(s)
        if lengthOfP > lengthOfS:
            return False
        else:
            counterP = collections.Counter(p)
            counterS = collections.Counter(s[0: lengthOfP]) # 初始条件
            if counterP == counterS:
                return True

            for i in range(1, lengthOfS - lengthOfP + 1): # 判断[i, i + 1, i + 2, ..., i + lengthOfP - 1]之间的substring
                # counterS = collections.Counter(s[i: i + lengthOfP])
                # 这样每次都重新数一遍肯定是不行的，考虑缓存加速
                counterS[s[i - 1]] -= 1 # 把前一个字符删掉
                counterS[s[i + lengthOfP - 1]] += 1 # 加入最后一个字符
                if + counterS == + counterP: # +号的目的是去掉非正数
                    return True

            return False