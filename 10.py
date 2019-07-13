r"""
.. default-role:: math

实现正则表达式匹配，通配符只要实现 ``.`` 和 ``*`` 就可以了。

.. 属于编译原理的基础内容吧……等我学了编译原理再来做
.. 好了我学会了

用NFA很好搞定，分两步

1.  构建NFA状态转移表
2.  执行NFA

因为只要实现两个特殊字符 ``*`` 和 ``.`` 所以构建状态转移表不是很复杂

-   遇到普通字符（不是 ``a*, .*, .`` 就是普通的 ``a``），最简单，直接在上一个状态后面接一个新状态，上一个状态输入 ``a`` 后转移到新状态、输入别的东西转移到错误态。
-   遇到单个的点 ``.`` （不是 ``a, a*, .*`` 就是单个 ``.``），也很简单，直接在上一个状态后面接一个新状态，上一个状态输入任意字符（不包括epsilon）后转移到新状态。
-   遇到普通字符加 ``*`` （也就是 ``a*`` ），稍微复杂一点，可以看 [ucb-cs164]_ 的课件，在lecture 4的ppt上有，需要接两个状态，还会涉及到输入 `\epsilon` 的情况。
-   遇到点加 ``*`` （也就是 ``.*`` ），和 ``a*`` 处理方法差不多，也是接两个状态。也会涉及到输入 `\epsilon` 的情况。

NFA里比较难理解的一个概念就是 `\epsilon` 。这个 `\epsilon` 表示 **没有输入** ，这个就很难理解，特别对我这种习惯了DFA的人，没有输入状态机怎么知道要不要转移状态。 [cooper2011]_ 书上第2章第44页讲到了这个问题，我比较倾向于第二种解释：当NFA转移到了某个可以接受 `\epsilon` 输入的状态的时候，NFA克隆了自己，就像UNIX里的 ``fork()`` 一样，变成了两个完全一模一样的NFA，假设叫NFA 1和NFA 2，这个时候，NFA 1待在原状态，NFA 2沿着 `\epsilon` 输入，进入下一个状态。极有可能NFA 2通过 `\epsilon` 转移、进入下一个状态之后，发现下一个状态也是可以接受 `\epsilon` 输入的，这时候NFA 2还会再次fork，变成NFA 2.1和NFA 2.2……这样一直fork，直到不再能fork出更多NFA为止。

需要注意的是，任意输入是 **不包括** `\epsilon` 输入的，因为 `\epsilon` 代表的是没有输入，只是表示一种分支、一种fork，而任意输入虽然是任意的，好歹是 **有输入** 的，这个和 `\epsilon` 的意义是不一样的。写的时候，任意输入可以用 `DefaultDict` 来写，但是 `\epsilon` 转移始终是需要用if单独判断的。

构建状态转移表的时候有一些技巧可以用一用，会节省很多代码

-   一开始NFA是在初始状态，这是很自然的想法，问题是，初始状态也有可能可以接受 `\epsilon` 输入，所以一开始就要fork，很麻烦，这时候可以搞一个dummy state放在初始状态前面，这个dummy state接受任意输入（但不包括 `\epsilon` 输入）后转移到初始状态。
-   可以搞一个错误态，可以极大地方便最终的判断。错误态接受任意输入（不包括 `\epsilon` 输入）后都转移到自身，这很自然没什么问题。问题是终止态的判断其实是一件麻烦事，要单独写一个if逐个判断每个NFA是否在终止态，既然题目要求的是匹配整个字符串（ ``cover the entire input string`` ），所以进入终止态之后，NFA其实不应该接受任何输入了，再接受输入就不对了，可以让终止态接受任意输入（不包括 `\epsilon` 输入）后转移到错误态。用了错误态的概念之后，还可以在遍历完成之前，提前判断还有没有必要继续遍历下去，因为NFA一旦进入错误态之后就永远没法再出来了，所以如果所有的NFA克隆体都进入错误态了，那也就没有必要继续执行下去了。

这题做完真的很爽啊_(:зゝ∠)_

.. [cooper2011] Keith Cooper, Linda Torczon写的教科书Engineering a Compiler
.. [ucb-cs164] `UC Berkeley CS164 Compilers and Programming Languages <http://www-inst.eecs.berkeley.edu/~cs164/sp19/>`_

写了篇解释

.. code:: markdown

    NFA stands for non-deterministic finite automata. If you are unfamiliar with NFA, better check out [UC Berkeley CS164 Compilers and Programming Languages](http://www-inst.eecs.berkeley.edu/~cs164/sp19/)'s Lecture 4 slides.

    The NFA approach consists of two stages

    1. construct the transition table from the pattern string: iterate over the pattern string `p`, and construct a transition table `transitions`, where `transition[state][input]` represents the state that the NFA should transfer into if it is currently in state `state` and received an input `input`. 
    2. execute the NFA with the string to match as input: iterate over the string `s`, and make NFA transfer to different states according to the transition table `transitions` that we have just constructed.

    Since it is an NFA not a DFA, which means some states can accept epsilon as input, and epsilon represents *no input* , there can be multiple *NFA clones* at some point.

    The idea of epsilon and *no input* can be hard to accept at first (IMHO). Whenever NFA reaches some state that can accept epsilon input, NFA *clones* itself once (it's like `fork()` function in UNIX). Now that we have two NFAs namely NFA 1 and NFA 2, both sitting on the same state, one NFA (suppose NFA 1) remains still on current state, and another NFA (suppose NFA 2) takes the epsilon input and transfers to the next state where the epsilon input points to. It is possible that when NFA 2 reaches the next state, it amazingly finds that the new state can accept epsilon too. So NFA 2 forks again, into NFA 2.1 and NFA 2.2 ...This forking process continues on and on until no more forks can be made.
    
    If you still can't get the idea, better check out Keith Cooper and Linda Torczon's book *Engineering a Compiler* Chapter 2, Page 44.

    ```python
    class Solution:
        def isMatch(self, s: str, p: str) -> bool:
            p = p + "\x00" # append a dummy character so we do not have to check out-of-bounds
            transitions = {} # transition table. `transition[state][input]` indicates which state the NFA should transfer into if it is current in state `state` and receives an input `input`
            default = True # the default input. When the current state does not accept some certain character as input, the NFA transfers into whatever the default input points to. The default input represents some kind of input (at least there *is* some input), so it does not cover the case of epsilon input.
            errorState = float("nan") # error state
            epsilon = -1 # epsilon input, or no input
            lastState = 0 # the last valid state in the transition table so far
            initialState = 0 # initial state

            for i, v in enumerate(p[: -1]): # iterate over the pattern string and construct the transition table
                if v == "*": # here I choose to process `a*` when we meet `a` so if current character is `*` that means it has been processed in the previous iteration
                    continue # so just skip
                else: # current character is a common character or `.`
                    if p[i + 1] != "*": # the character right after current character is not a `*`, so this pattern character only matches one character in the string
                        transitions[lastState] = dict()
                        if v == ".": # `.` matches any single character
                            transitions[lastState][default] = lastState + 1 # so just set the default input
                        else: # other than `.`
                            transitions[lastState][v] = lastState + 1
                            transitions[lastState][default] = errorState # otherwise go to error state
                        lastState += 1 # our transition table has a new state, so future states should be built upon it
                    else: # something like `a*`
                        # check lecture 4 slides to see how to construct states for a pattern like `a*`
                        transitions[lastState] = dict()
                        transitions[lastState + 1] = dict()
                        if v == ".": # something like `.*`
                            transitions[lastState][default] = lastState + 1
                            transitions[lastState][epsilon] = lastState + 2
                            transitions[lastState + 1][epsilon] = lastState
                            transitions[lastState + 1][default] = errorState
                        else: # `a*`
                            transitions[lastState][v] = lastState + 1
                            transitions[lastState][epsilon] = lastState + 2
                            transitions[lastState][default] = errorState
                            transitions[lastState + 1][epsilon] = lastState
                            transitions[lastState + 1][default] = errorState
                        lastState += 2

            beforeState = float("-inf") # insert a dummy state before initial state to make life easier, because initial state can probably accept epsilon input
            transitions[beforeState] = dict()
            transitions[beforeState][default] = initialState # points dummy state to initial state, make it transfer to initial state when it receives any input
            acceptingState = lastState # so far we have constructed the core part of our transition table. Since it is required to return match success when the pattern `covers the entire input string (not partial)`, there is only one acceptable state.
            transitions[acceptingState] = dict()
            transitions[acceptingState][default] = errorState # NFA should not accept any input when it reaches the final, acceptable state, so make it point to error state when it receives any input
            transitions[errorState] = dict()
            transitions[errorState][default] = errorState # NFA should either not accept any input when it reaches the error state, so make it point to itself
            # print(transitions)
            states = {beforeState} # use a set to avoid duplicate NFA clones

            for i, v in enumerate("\x00" + s): # execute NFA. Insert a dummy character to make dummy state accept it and transfer to initial state.
                nextStates = set()

                for state in states: # iterate over all NFA clones and make them transfer to next states (probably more clones)
                    if v in transitions[state]: # current state can accept current character as input
                        nextState = transitions[state][v] # make it transfer to next state
                    else: # oops, not an acceptable character
                        nextState = transitions[state][default] # transfer to default
                    nextStates.add(nextState)

                    # check whether current NFA should be forked to more clones
                    while epsilon in transitions[nextState]: # stop when some cloned version does not accept epsilon input any more
                        nextState = transitions[nextState][epsilon]
                        nextStates.add(nextState)

                states = nextStates # transfer to new states
                # print(states)
                # if states == set() or all(state == errorState for state in states): # If the string has not yet been exhausted and all clones have inevitably gone into error state, they will forever get stuck in error state and will never have a chance to go out, so there is no point to continue executing
                if states == set() or (len(states) == 1 and errorState in states): # make it faster using set's O(1) `in`
                    return False # the string must mismatch pattern
            else: # string exhausted
                if acceptingState in states: # at least one clone sits on the final, acceptable state
                    return True # it is a match!
                else: # oops
                    return False # mismatch

    # s = Solution()
    # print(s.isMatch("aa", "a")) # false
    # print(s.isMatch("aa", "aa")) # true
    # print(s.isMatch("aa", "a*")) # true
    # print(s.isMatch("ab", ".*")) # true
    # print(s.isMatch("aab", "c*a*b")) # true
    # print(s.isMatch("mississippi", "mis*is*p*.")) # false
    ```

    44ms beats 96.74%
"""

from typing import *

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
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
# print(s.isMatch("aa", "aa")) # true
# print(s.isMatch("aa", "a*")) # true
# print(s.isMatch("ab", ".*")) # true
# print(s.isMatch("aab", "c*a*b")) # true
# print(s.isMatch("mississippi", "mis*is*p*.")) # false