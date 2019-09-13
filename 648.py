"""
把句子里的词语替换成字典里的前缀

最暴力的办法当然就是和字典里的前缀一个一个比较，好像也能过。
"""

from typing import *

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        res = []

        for word in sentence.split(" "): # 遍历每个词
            replacedBy = word # 如果词不匹配字典里的任意一个前缀，那就不替换

            for ref in dict: # 遍历字典里的每个前缀
                if word.startswith(ref): # 如果词以这个前缀开始
                    replacedBy = min((replacedBy, ref), key=len) # 就替换成这个前缀。根据提议，如果匹配多个前缀，选取最短的那个前缀来替换，所以这里的min用了一个custom key function

            res.append(replacedBy)

        return " ".join(res)

# s = Solution()
# print(s.replaceWords(dict = ["cat", "bat", "rat"], sentence = "the cattle was rattled by the battery"))