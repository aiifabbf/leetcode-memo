"""
wildcard匹配，只需要实现 ``*`` 和 ``?`` 。 ``*`` 表示匹配空字符串或者任意字符串， ``?`` 表示匹配任意一个字符。

发现这里的 ``*`` 其实等效于正则表达式里 ``.*`` ， ``?`` 等效于正则表达式里的 ``.`` 。可以直接用第10题的结果，把pattern里面的 ``*`` 替换成 ``.*`` 、``?`` 替换成 ``.`` 。

发现速度不太行，可能针对wildcard有特殊优化方法吧，因为wildcard不包括 ``a*, .*`` 这种情况。
"""

from typing import *

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.isMatchRegularExpression(s, p.replace("*", ".*").replace("?", "."))

    def isMatchRegularExpression(self, s: str, p: str) -> bool:
        p = p + "\x00" # 后面补一个dummy char，这样方便一点，不用判断越界
        transitions = {} # 状态转移表，transitions[state][input]表示在状态state时、输入是input时应该转到哪个状态
        default = True # 表示其他输入
        errorState = float("nan") # 错误态
        epsilon = -1 # 表示epsilon输入
        lastState = 0 # 构建转移图过程中的最后一个状态
        initialState = 0 # 初始状态

        for i, v in enumerate(p[: -1]): # 遍历pattern的每个字符，构建状态转移表
            if v == "*": # 我们选择把后面跟*的放在前一个字符里处理，所以如果当前字符是*的话，前一个字符已经处理过了，所以直接跳过不用处理了
                continue
            else:
                if p[i + 1] != "*": # 如果当前字符的后一个字符不是*，说明只匹配一个字符
                    # 只匹配一个字符的普通的状态转移图很简单，就是在最后一个状态后面追加一个状态，最后一个状态接受当前字符之后转移到新状态，接受其他字符时转移到错误态
                    transitions[lastState] = dict()
                    if v == ".": # 当前字符是`.`，匹配任何一个字符
                        transitions[lastState][default] = lastState + 1 # 接受default字符后转移到新状态
                    else: # 其他字符。只匹配那个具体的字符
                        transitions[lastState][v] = lastState + 1 # 接受当前字符后转移到新状态
                        transitions[lastState][default] = errorState # 接受其他字符后转移到错误态
                    lastState += 1 # 最后状态+1
                else: # 如果当前字符的后一个字符是`*`，说明可能匹配0或1或任意多个字符
                    # 匹配0或1或任意多个字符的状态转移图稍微复杂一点，会多出两个状态，还会包含有接受epsilon的状态转移
                    transitions[lastState] = dict()
                    transitions[lastState + 1] = dict()
                    if v == ".":
                        transitions[lastState][default] = lastState + 1
                        transitions[lastState][epsilon] = lastState + 2
                        transitions[lastState + 1][epsilon] = lastState
                        transitions[lastState + 1][default] = errorState
                    else:
                        transitions[lastState][v] = lastState + 1
                        transitions[lastState][epsilon] = lastState + 2
                        transitions[lastState][default] = errorState
                        transitions[lastState + 1][epsilon] = lastState
                        transitions[lastState + 1][default] = errorState
                    lastState += 2

        beforeState = float("-inf") # 搞一个虚状态，方便一点。因为初始状态也可能可以接受epsilon输入，如果不搞虚状态，在初始状态的时候还要克隆一遍
        transitions[beforeState] = dict()
        transitions[beforeState][default] = initialState # 虚状态接受任意输入后都转移到初始状态
        acceptingState = lastState # 状态转移图已经构建完了，因为题目要求是``cover the entire string``也就是string要完全匹配整个pattern，所以终止态就是状态转移图中的最后一个状态
        transitions[acceptingState] = dict()
        transitions[acceptingState][default] = errorState # 进入终止态之后就不应该接受任何输入了，但是为了方便，定义终止态接受任意输入之后转移到错误态
        transitions[errorState] = dict()
        transitions[errorState][default] = errorState # 进入错误态之后也不应该接受任何输入了，但是同样为了方便，定义错误态接受任意输入之后转移到自身
        # print(transitions)
        states = {beforeState} # 因为是NFA，所以可能会有多个同步的状态。用set可以防止重复

        for i, v in enumerate("\x00" + s): # 开始匹配
            nextStates = set() # 下一状态集合。输入当前字符之后、或者输入当前字符和任意多个epsilon之后进入的所有状态

            for state in states: # 遍历所有的状态机克隆体
                if v in transitions[state]: # 如果发现当前状态可以接受当前字符作为输入
                    nextState = transitions[state][v] # 就转移到那个状态
                else: # 当前状态不接受当前字符作为输入
                    nextState = transitions[state][default] # 转移到当前状态定义的接受其他字符时转移到的状态
                nextStates.add(nextState) # 转移后的状态加入到下一状态集合里

                # 如果转移之后的新状态可以接受epsilon，还要克隆出所有因epsilon转移的状态机
                while epsilon in transitions[nextState]: # 直到到某个不接受epsilon的状态为止
                    nextState = transitions[nextState][epsilon] # 接受epsilon输入之后进入的新状态
                    nextStates.add(nextState) # 新状态也要加入下一状态集合中

            states = nextStates # 转移状态
            # print(states)
            # if states == set() or all(state == errorState for state in states): # 如果还没遍历完整个字符串，所有的状态机就都进了错误态，因为状态机一旦进错误态就不可能再出来了，所以没有必要再遍历下去了
            if states == set() or (len(states) == 1 and errorState in states): # 这样写快一点
                return False # 直接表明不匹配
        else: # 遍历完整个字符串
            # if any(state == acceptingState for state in states): # 发现至少存在一个状态机是正好处在终止态的
            if acceptingState in states: # 直接判断终止态在不在集合中速度会快一点
                return True # 匹配成功
            else: # 不存在处在终止态的状态机
                return False # 匹配失败

# s = Solution()
# print(s.isMatch("aa", "a")) # false
# print(s.isMatch("aa", "*")) # true
# print(s.isMatch("cb", "?a")) # false
# print(s.isMatch("abceb", "*a*b")) # true
# print(s.isMatch("acdcb", "a*c?b")) # false