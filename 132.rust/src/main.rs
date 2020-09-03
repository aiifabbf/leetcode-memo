/*
.. default-role:: math

给个字符串，问最少切多少次，可以把字符串切成全是回文的substring（要连续）？

比如给 ``aaa`` ，因为它本身就是回文，所以不用切；比如给 ``aab`` ，可以切一次切成 ``aa, b`` ，也可以切两次切成 ``a, a, b`` ，因为切成 ``aa, b`` 只要切一次，所以答案是1。

条件反射想到动态规划……设 ``dp[j]`` 是 ``s[0..j]`` 最少切多少次。那么 ``dp[j]`` 怎么用前面的项算出来呢？

-   如果 ``s[0..j]`` 本身就已经是回文了，那么根本不用切， ``dp[j] == 0``
-   如果 ``s[0..j]`` 不是回文，那么有两种选择

    -   把 ``s[0..j]`` 切成单字符，需要切 `j - 1` 次。因为单字符一定是回文，所以这么做肯定可行，但是不一定切的次数最少
    -   在 `j` 的前面找到一个 `i` 使得 ``s[i..j]`` 正好是回文，那么可以在 `i` 这里切一刀，所以总共切的次数就是 ``s[0..i]`` 里切的次数加上在 `i` 处切的一次，也就是 ``dp[i] + 1``

        ::

            s[0..i]里最少切了dp[i]次
            v------v
            [      |aabbaa)
            0      i      j
                   ^------^ s[i..j]是回文
*/

struct Solution;

impl Solution {
    pub fn min_cut(s: String) -> i32 {
        // 为了快速判断s[i..j]是不是回文，先传统艺能一下，用一次O(n^2)的DP算出每个substring是不是回文
        let s: Vec<char> = s.chars().collect();
        let mut palindromic = vec![vec![false; s.len() + 1]; s.len() + 1]; // palindromic[i][j] == true表示s[i..j]是回文

        // 初始条件
        for i in 0..s.len() + 1 {
            palindromic[i][i] = true; // 空字符肯定是回文
        }

        // 初始条件
        for i in 0..s.len() {
            palindromic[i][i + 1] = true; // 单字符也是回文
        }

        for gap in 2..s.len() + 1 {
            for i in 0..s.len() - gap + 1 {
                let j = i + gap;
                if s[i] == s[j - 1] && palindromic[i + 1][j - 1] == true {
                    palindromic[i][j] = true;
                }
            }
        }

        let mut dp = vec![0; s.len() + 1]; // dp[j]表示s[0..j]最少要切多少次

        // 初始条件
        for j in 1..s.len() + 1 {
            dp[j] = j as i32 - 1; // s[0..j]最多切j - 1下、全部切成单字符，因为单字符一定是回文，所以一定能保证substring全是回文
        }

        for j in 2..s.len() + 1 {
            if palindromic[0][j] == true {
                // 如果s[0..j]本身就是个回文
                dp[j] = 0; // 那根本不用切
            } else {
                // 如果不是，去j的前面找一个i
                for i in 0..j {
                    if palindromic[i][j] == true {
                        // 使得s[i..j]正好是回文
                        dp[j] = dp[j].min(1 + dp[i]); // 这样切的次数等于在i处切一次、加上s[0..i]里切的次数
                    }
                }
            }
        }

        return *dp.last().unwrap(); // 原问题的答案是s[0..n]切多少次，正好就是dp[n]
    }
}

fn main() {
    dbg!(Solution::min_cut("aab".into())); // 1
    dbg!(Solution::min_cut("a".into())); // 0
    dbg!(Solution::min_cut("ab".into())); // 1
}
