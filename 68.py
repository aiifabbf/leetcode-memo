class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        rendered = []
#         lineBuffer = ""
        wordBuffer = []
        for i in range(len(words)):
#             print(wordBuffer)
#             print(rendered)
            if wordBuffer != [] and len(" ".join(wordBuffer) + " " + words[i]) >= maxWidth: # 这行加不下下一个词了
                totalSpace = maxWidth - len("".join(wordBuffer)) # 可用的空格个数
                spaceCount = len(wordBuffer) - 1 # 需要插多少个空格
                if spaceCount == 1: # 这行只能放一个单词
                    lineBuffer = wordBuffer[0] + " " * totalSpace
                    rendered.append(lineBuffer)
                elif totalSpace % spaceCount == 0: # 空格正好均匀分配
                    rendered.append((" " * (totalSpace // spaceCount)).join(wordBuffer))
                else:
                    bigSpaceCount = round(totalSpace / spaceCount) # 多出来的空格放在左边
                    normalSpaceCount = totalSpace - bigSpaceCount * (spaceCount - 1) # 其他空格放在最右边
                    lineBuffer = (" " * bigSpaceCount).join(wordBuffer[: -1])
                    lineBuffer += " " * normalSpaceCount + wordBuffer[-1]
                    rendered.append(lineBuffer)
                    
                wordBuffer = [] # 清空单词缓冲区
                
            wordBuffer.append(words[i]) # 把单词加入缓冲区
            
        totalSpace = maxWidth - len("".join(wordBuffer))
        rendered.append(" ".join(wordBuffer) + " " * totalSpace)
                
        return rendered

Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"], 20)