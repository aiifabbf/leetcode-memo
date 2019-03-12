from typing import *

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # i = 0
        # counter = 0
        # while i < len(s) - 1:
        #     symmetricNumber = 1
        #     while symmetricNumber * 2 + i <= len(s):
        #         if "0" in s[i: i + symmetricNumber] and "1" in s[i: i + symmetricNumber]: # 保证模板里成分单一
        #             break
                
        #         if s[i] == "0":
        #             if symmetricNumber == s[i + symmetricNumber: i + symmetricNumber * 2].count("1"):
        #                 counter += 1
        #         elif s[i] == "1":
        #             if symmetricNumber == s[i + symmetricNumber: i + symmetricNumber * 2].count("0"):
        #                 counter += 1
                
        #         symmetricNumber += 1

        #     i += 1

        # return counter

        # 过不了，time limit exceeded

        buffer = [1 if s[0] == "0" else -1]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                # buffer[-1] = buffer[-1] + s[i] # 这个每次都要重新生成新的string，有点慢。改成了buffer里存最长肉块的数目，如果肉块是0，那么用正数存，如果肉块是1，用负数存。
                if s[i] == "0":
                    buffer[-1] += 1
                else:
                    buffer[-1] -= 1
            else:
                buffer.append(1 if s[i] == "0" else -1)

        if len(buffer) == 1:
            return 0

        counter = 0
        for i in range(1, len(buffer)):
            if buffer[i] * buffer[i - 1] > 0: # 同号，说明这组肉块都是0或者都是1，不成镜像
                continue

            counter += min(abs(buffer[i]), abs(buffer[i - 1])) # 0000和111可以成3对镜像

        return counter


s = Solution()
assert s.countBinarySubstrings("00110011") == 6
assert s.countBinarySubstrings("10101") == 4