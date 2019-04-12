"""
问一个字符串能不能匹配另一个模板字符串，并且之间全是小写字母。

其实就是问pattern是不是queries里面每个query的subsequence（可以不连续）、并且之间的元素是不是全是小写的。
"""

from typing import *

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []

        for v in queries:
            pos = -1

            for patternCharacter in pattern:
                try:
                    thisPosition = v.index(patternCharacter, pos + 1) # 从query中找到下一个模板字符
                    if v[pos + 1: thisPosition] == "": # 上一个模板字符和这一个模板字符之间没有间隔
                        pos = thisPosition
                        continue
                    else: # 上一个模板字符和这个模板字符之间有其他字符，这时候就需要看这些字符是不是都是小写字母
                        if v[pos + 1: thisPosition].islower() == False: # 不全是小写字母
                            res.append(False) # 说明不匹配
                            break # 直接break
                        else: # 全是小写字母
                            pos = thisPosition # 当无事发生
                            continue
                except: # 找不到
                    res.append(False) # 说明不匹配，直接break
                    break
            else: # 每个模板字符都找到了，并且是按顺序的，但是此时最后一段还没有判断是不是全是小写字母
                if v[pos + 1: ] == "": # 最后一段是空的
                    res.append(True)
                else: # 最后一段不空
                    if v[pos + 1: ].islower(): # 全是小写字母
                        res.append(True)
                    else: # 不全是小写字母
                        res.append(False)

        return res

# s = Solution()
# print(s.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"))
# print(s.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa"))
# print(s.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT"))

# print(s.isSubArray("FB", "FooBar"))