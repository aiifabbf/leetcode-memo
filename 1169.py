"""
.. default-role:: math

列出所有无效的交易。一笔交易被视为无效有两种情况

-   数额大于1000
-   或者和另一笔由同一个人、在不同城市发起的交易的间隔时间不超过60 min

`O(n^2)` 搞搞吧，不烦了。
"""

from typing import *

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactionsIndexedByName = {}
        invalidTransactions = set()

        for transaction in transactions: # 筛选出第一种情况：所有数额大于1000的交易
            name, time, amount, city = self.parseTransaction(transaction)
            if amount > 1000:
                invalidTransactions.add(transaction)

            if name not in transactionsIndexedByName:
                transactionsIndexedByName[name] = [transaction]
            else:
                transactionsIndexedByName[name].append(transaction)

        for name, transactions in transactionsIndexedByName.items(): # 筛选出第二种情况

            for i, v in enumerate(transactions):
                
                for j, w in enumerate(transactions):
                    thisTransaction = self.parseTransaction(v)
                    thatTransaction = self.parseTransaction(w)
                    thisTime = thisTransaction[1]
                    thisCity = thisTransaction[3]
                    thatTime = thatTransaction[1]
                    thatCity = thatTransaction[3]

                    if abs(thatTime - thisTime) <= 60 and thatCity != thisCity: # 发生间隔时间不超过60 min、发生在不同城市
                        invalidTransactions.add(v)
                        invalidTransactions.add(w)

        return list(invalidTransactions)

    def parseTransaction(self, transaction: str) -> tuple:
        name, time, amount, city = transaction.split(",")
        time = int(time)
        amount = int(amount)
        return (name, time, amount, city)

# s = Solution()
# print(s.invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,100,beijing"]))
# print(s.invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]))
# print(s.invalidTransactions(transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]))
# print(s.invalidTransactions(["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]))