"""
过滤出array中所有符合pattern的元素。

比如pattern是 ``abb`` 的话，就是要从array里找到所有第二第三个字母一样、第一个字母不一样的字符串，比如 ``abc`` 就不符合这个patter； ``mee`` 就符合这个pattern。

这道题有似曾相识的感觉，所以我马上就想到了做法，先把pattern转换成数字list，这个list里面的元素是pattern里面每个字母第一次出现在pattern里的下标 [#]_ ，然后再遍历array，用同样的方法，把array里每个字符串里面的每个字符都替换成这个字符在这个字符串里第一次出现的下标，和pattern比较就可以了。

.. [#] 比如 ``abb`` 就会变成 ``[0, 1, 1]``。这样如果遇到array里的某个字符串 ``mee`` 的时候， ``mee``也首先变成 ``[0, 1, 1]`` ，再比较一下就可以了。
"""

from typing import *

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        pattern = map(pattern.index, pattern) # abb -> 011
        return list(filter(lambda word: pattern == [word.index(j) for j in word], words))