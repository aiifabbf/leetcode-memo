# 统计出words里有多少个元素是S的subarray

# 判断一个数列是不是另一个数列的subarray有点难。好吧其实也不难

from typing import *

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        count = 0
        for i in words:
            pos = -1
            # if len(i) > len(S):
            #     continue
            # stringView = S
            for char in i:
                try:
                    # pos = stringView.index(char) # 在后续的数列里找
                    # stringView = stringView[pos + 1: ] # 找到的话，这个元素之前的部分都不用看了，直接从这个元素的下一个位置开始找下一个元素
                    # 一改：str.index其实还有两个参数是start和end，速度超快

                    pos = S.index(char, pos + 1)
                except: # 没找到的话就一定不是subarray
                    break
            else: # for循环没有break，意思是每个元素都按序在原数列里找到了
                # print(i)
                count += 1

        return count

s = Solution()
assert s.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]) == 3
assert s.numMatchingSubseq("rwpddkvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvjubjgloeofnpjqlkdsqvruvabjrikfwronbrdyyjnakstqjac", ["wpddkvbnn","lnagtva","kvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvju","rwpddkvbnnugln","gloeofnpjqlkdsqvruvabjrikfwronbrdyyj","vbgeinupkvgmgxeaaiuiyojmoqkahwvbpwugdainxciedbdkos","mspuhbykmmumtveoighlcgpcapzczomshiblnvhjzqjlfkpina","rgmliajkiknongrofpugfgajedxicdhxinzjakwnifvxwlokip","fhepktaipapyrbylskxddypwmuuxyoivcewzrdwwlrlhqwzikq","qatithxifaaiwyszlkgoljzkkweqkjjzvymedvclfxwcezqebx"]) == 5