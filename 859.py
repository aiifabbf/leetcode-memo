"""
给两个字符串A、B，是否能通过调换A中的某两个字符的位置，使得A和B完全相等？注意必须要调换，不能不调换。

比如 ``ab`` 和 ``ab`` 虽然相等，但是没有办法选择某两个字符的位置调换一下然后两个还是相等，因为如果要选择两个字符，只能选择那两个仅有的字符，这样的话 ``ab`` 就变成了 ``ba`` ，就和 ``ab`` 不相等了。

但是 ``aa`` 和　``aa`` 就不一样，虽然也是相等的，但是因为如果选择调换 ``aa`` 中两个字符的位置， ``aa`` 还是变成 ``aa`` ，没有变化。
"""

from typing import *

import collections

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): # 长度不相等的肯定没机会
            return False
        elif A == B and A: # 遇到两个字符相等的也不能大意，想想ab和ab、aa和aa的情况
            counter = collections.Counter(A) # 用一个Counter统计一下直方图
            if counter.most_common(1)[0][1] >= 2: # 如果存在某个字符出现了两次及以上，就可以选择这个字符来调换，使得字符串根本没有变化，这样就可以达成题目的目标了
                return True
            else: # 不存在某个字符出现了两次及以上，也就是说，虽然两个字符串完全相等，但是一旦找两个字符调换位置，是没有办法让原字符串不变的，一定是会改变原字符串的，无法达到题目的要求
                return False
        else: # 如果两个字符串本来就不相等
            diffs = [] # 做一次diff

            for i in range(len(A)):
                if A[i] != B[i]:
                    diffs.append((A[i], B[i]))
            
            if len(diffs) != 2: # diff的次数不是2，可能是1或者3及以上，如果是1次，调换位置会导致两处字符变化，所以不行；如果是3次及以上，无法做到两次调换就抹平所有的不同，所以也是不行的
                return False
            else: # 正好是两处不同
                if diffs[0][0] == diffs[1][1] and diffs[0][1] == diffs[1][0]: # 如果两处不同是互补的，比如第一处是a和b，第二处是b和a
                    return True # 那就可以
                else: # 两处不同不是互补的，比如第一处是a和b，但是第二处是b和c
                    return False # 那么还是不行

# s = Solution()
# print(s.buddyStrings("ab", "ba")) # true
# print(s.buddyStrings("ab", "ab")) # false
# print(s.buddyStrings("aa", "aa")) # true
# print(s.buddyStrings("aaabc", "aaacb")) # true
# print(s.buddyStrings("", "aa")) # false
# print(s.buddyStrings("", "")) # false