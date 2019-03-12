# 从一个字符串组中，找到这样一个字符串，它的每个前缀都在字符串组中。如果有多个，返回最长的那个。如果最长的有多个，返回lexical顺序最小的。

from typing import *

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = set(words)
        q = set()
        for word in words:
            for right in range(1, len(word) + 1):
                if word[: right] not in words:
                    break
            else:
                q.add(word)

        results = sorted(q, key=len)
        for index, value in enumerate(results):
            if len(value) == len(results[-1]):
                break

        return sorted(results[index:])[0]

s = Solution()
assert s.longestWord(["w","wo","wor","worl", "world"])