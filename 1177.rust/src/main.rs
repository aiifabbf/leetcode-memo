/*
.. default-role:: math

给一个很长的、只含小写字母的字符串，反复问很多很多次：能否重新排列这个字符串的某个指定的substring（要连续），使得substring变成回文，并且最多可以把substring里的 `k` 个字母变成别的字母？

比如给 ``abcda`` ，第一次问能否把 ``d`` 这个substring变成回文，第二次问给你1次机会，能否把 ``abcd`` 变成回文。

先考虑什么样子的字符串，重排列之后可以变成回文。只要满足一个条件，就是字符串里面最多只能有 **1种** 字母出现了奇数次。

比如 ``aaabbccdd`` 是可以重排列变成回文 ``bcdaaadcb`` 的，因为 ``a`` 这种字母出现了3次，而且除了 ``a`` 以外，其他种类的字母 ``b, c, d`` 都是出现了偶数次。

比如 ``aaabbbccdd`` 就没办法重排列变成回文，因为 ``a, b`` 都出现了奇数次。

再考虑，给你最多 `k` 次把任意字母变成其他任意字母的机会（可以不用完），什么样子的字符串能变成回文和？首先本身就能凑成回文的字符串肯定没问题，比如刚才讲到的 ``aaabbccdd`` ，不需要改动就能重排列成回文字符串。那么有两种出现了奇数次的字母的字符串行不行呢？可以的，比如 ``aaabbbccdd`` ，只要把1个 ``a`` 改成 ``b`` ，字符串就变成了 ``aabbbccdd`` ，这样所有字母种类都是出现了偶数次了。

接着找规律

-   0种奇数次字母的字符串，不需要改动（也就是最少需要0次改动机会）
-   1种奇数次字母的字符串，不需要改动（也就是最少需要0次改动机会）
-   2种奇数次字母的字符串，最少需要改动1次
-   3种奇数次字母的字符串，最少需要改动1次

    为啥这个也是最少只要改动1次就可以了呢？因为出现了奇数次的字母，少一次就变成了出现偶数次，同时可以把这个字母改成另一个之前出现了奇数次的字母。
    比如 ``aaabbbcccdd`` ，如果把1个 ``a`` 改成 ``b`` ，那么字符串变成了 ``aabbbbcccdd`` 。注意不仅 ``a`` 出现的次数从奇数次变成了偶数次， ``b`` 出现的次数也从奇数次变成了偶数次，可谓是一箭双雕。

-   4种奇数次字母的字符串，最少需要改动2次
-   5种奇数次字母的字符串，最少需要改动2次
-   ...
-   `2k` 种奇数次字母的字符串，最少需要改动 `k` 次
-   `2k + 1` 种奇数次字母的字符串，最少需要改动 `k` 次

这样我们就知道了任意一个字符串最少需要给几次改动机会，才能变成一个重排之后能变成回文的字符串。

现在还剩下一个问题，如何快速知道任意一个substring里每个字母出现的次数呢？用向量前缀和，每个字母出现的次数是向量中的一维。 ``a`` 出现的次数就是向量的第一维， ``b`` 出现的是第二维。既然总共只有26个小写字母，那么这个向量做成26维就够了。

比如 ``aaabbbcccdd`` 的直方图可以表示成一个26维向量

.. math::

    \left(\begin{matrix}
        3 \\
        3 \\
        3 \\
        2 \\
        \vdots \\
        0 \\
    \end{matrix}\right)

假设 ``integrals[i]`` 是substring ``s[0..i]`` 的直方图向量，那么任意substring ``s[i..j]`` 的直方图向量就是 ``integrals[j] - integrals[i]`` 了。

再从直方图里面找到有多少个奇数，按照刚才的规则算一下给最多 `k` 次机会能不能重排列变成回文就好啦。
*/

struct Solution;

impl Solution {
    pub fn can_make_pali_queries(s: String, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let s: Vec<char> = s.chars().collect();
        let mut integrals = vec![[0; 26]; s.len() + 1]; // integrals[i]是s[0..i]的直方图，integrals[i][0]表示s[0..i]里面a出现的次数，integrals[i][1]表示s[0..i]里面b出现的次数，以此类推

        for i in 1..s.len() + 1 {
            integrals[i] = integrals[i - 1];
            integrals[i][s[i - 1] as usize - 'a' as usize] += 1;
        }

        let mut res = vec![];

        for v in queries.into_iter() {
            let left = (v[0] as usize).max(0).min(s.len()); // 把left和right限制在[0, len]区间之间
            let right = (v[1] as usize + 1).max(0).min(s.len());
            let budget = v[2] as usize; // 给多少次改变的机会
            let mut deltaCounter = [0; 26]; // s[left..right]的直方图

            for i in 0..26 {
                deltaCounter[i] = integrals[right][i] - integrals[left][i];
            }

            let oddCount = deltaCounter.iter().filter(|v| *v % 2 == 1).count(); // s[left..right]里面有多少种字母出现了奇数次
            if oddCount / 2 <= budget {
                res.push(true);
            } else {
                res.push(false);
            }
        }

        return res;
    }
}

fn main() {
    dbg!(Solution::can_make_pali_queries(
        "abcda".into(),
        vec![
            vec![3, 3, 0],
            vec![1, 2, 0],
            vec![0, 3, 1],
            vec![0, 3, 2],
            vec![0, 4, 1],
        ]
    )); // [true, false, false, true, true]
}
