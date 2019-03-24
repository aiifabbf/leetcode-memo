"""
给许多域名的访问次数，问你每个域名及其上级域名、上上级域名的访问总次数。

例如访问 ``discuss.leetcode.com`` 一次，其实算作

-   访问了 ``discuss.leetcode.com`` 1次
-   访问了 ``leetcode.com`` 1次
-   访问了 ``com`` 1次

最后要每个层级全都分别列出来。
"""

from typing import *

import collections

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = collections.Counter()

        for v in cpdomains:
            times, domains = v.split(" ") # 输入字符串是times_domain这样的格式，所以要先分离出来
            times = int(times)
            counter[domains] += times # 统计discuss.leetcode.com的次数
            domains = domains.split(".")
            if len(domains) == 3: # 还有可能出现mail.com这种二级域名
                counter[domains[-1]] += times # com
                counter[domains[-2] + "." + domains[-1]] += times # leetcode.com
            else: # 还有可能出现com这种？为了完整性就放在这里吧
                counter[domains[-1]] += times

        return [f"{v} {i}" for i, v in counter.items()]