# 题目大概意思是，pushed和popped有没有可能是对一个stack的合法操作历史。

# 意思是，到某一步时，如果pushed和popped都不为空，那么可以采取的操作是pushed[0]或者popped[0]；如果pushed空但popped不为空，那么下一步只能pop，但是也不一定就是pop，因为如果popped[0]和当前stack最后一个元素不一样，说明pop这一步也是不对的，所以这不是合法历史；还有可能stack在此时是空的，所以下一步根本不可能pop，所以这也不是合法历史；如果pushed不为空但popped为空，那么下一步只能……我写不下去了。

# 应该这样考虑，先考虑能不能pop，再考虑能不能push，如果都不能，即既不能pop也不能push，考虑是不是操作都已经结束了，如果操作都结束了，那么一切OK，如果是半途中出现既不能pop也不能push的情况，那么说明这不是合法历史。这里也体现一种贪婪的思想，因为pop的条件相对push来说苛刻一点。

# pop的条件是什么呢？

# -   stack不能空

#     如果stack空了，就不能pop了，所以stack此时一定不能空

# -   popped不能空

#     如果popped空了，说明所有的pop操作都做完了，根本不能再pop了

# -   popped[0] == stack[-1]

#     上面两个条件都满足以后，再看stack的顶端和popped的第一个元素是否相同。如果相同，说明可以pop。

#     此时就放心pop吧。

# 如果不能pop，那就只能考虑能不能push。push的条件是什么呢？

# -   pushed不能空

# 所以push的条件非常简单，只要pushed不空就可以。此时放心地push就好了，其他的事情下一步再说。

# 还可能出现既不能pop也不能push的情况，这可能说明下列两种情况中的一种

# -   ``popped == [] and pushed == []`` 操作已经结束

#     此时应该能观察到poppped和pushed都为空。历史都已经顺利结束了，当然既不能pop也不能push。此时说明一切OK，这是个合法的历史轨迹。

# -   ``popped or pushed`` 不是合法的历史

#     此时应该能观察到popped或pushed不为空，说明历史继续不下去了，那么这当然不是合法的历史。

from typing import *

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped): # push和pop操作次数不等
            return False
        if pushed == [] and popped == []: # 全空当然是可以的
            return True
        
        # # 从这里开始保证了push和pop操作次数相等并且不为零
        # stack = [pushed.pop(0)]
        # while True:
        #     if popped: # 可能pop
        #         if stack: # 并且stack不为空，更可能pop了
        #             if stack[-1] != popped[0]: # 但是发现如果pop，出来的东西却不对，所以这一步操作一定不是pop，只能是push
        #                 if pushed: # 可以push
        #                     stack.append(pushed.pop(0)) # 那就只能push了
        #                     continue
        #                 else: # 但是也有可能已经全push完了，不能push
        #                     return False # 所以这一步既不是pop也不是push，只能是出错了
        #             else: # 可以pop，并且pop出来的东西也是对的，所以就尽量pop
        #                 stack.pop()
        #                 popped.pop(0)
        #                 continue
        #         else: # stack为空，所以没法pop，只可能是push
        #             if pushed: # push非空，可以push
        #                 stack.append(pushed.pop(0)) # 所以只能push
        #                 continue
        #             else: # push空
        #                 return False # 所以这一步既不是pop也不是push，只能出错
        #     else: # pop操作已经完了，所以不可能是pop
        #         if pushed: # push非空，可以push
        #             stack.append(pushed.pop(0)) # 只能先试试push了
        #             continue
        #         else: # push操作也完了，所以也不可能是push
        #             # return stack == [] # 这个主要是防止push和pop的元素不同
        #             return True # 但是题目已经说了push和pop包含元素完全相同

        # 一改：上面代码真的太乱了……修改一下
        stack = []
        while True:
            if stack and popped and popped[0] == stack[-1]:
                stack.pop()
                popped.pop(0)
                continue
            elif pushed:
                stack.append(pushed.pop(0))
                continue
            elif pushed == [] and popped == []:
                return True
            else:
                return False

s = Solution()
assert s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
assert not s.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
assert s.validateStackSequences([2, 1, 0], [1, 2, 0])