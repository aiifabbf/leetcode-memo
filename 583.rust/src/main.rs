/*
.. default-role:: math

给两个字符串，每次能删除任意一个字符，问最少删多少次可以让两个字符串相等。

归约到最长公共subsequence的问题。其实就是求两个字符串的最长公共subsequence的长度，那么第一个字符串需要删除的次数就是原来的长度减去最长公共subsequence的长度、第二个字符串同理。
*/

struct Solution;

impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let s1: Vec<char> = word1.chars().collect();
        let s2: Vec<char> = word2.chars().collect();
        let mut dp = vec![vec![0; s2.len() + 1]; s1.len() + 1]; // dp[i][j]是s1[..i]和s2[..j]的最长公共subsequence的长度。这样定义可以省去设置初始条件

        for i in 1..s1.len() + 1 {
            for j in 1..s2.len() + 1 {
                if s1[i - 1] == s2[j - 1] {
                    // 如果s1[i - 1]和s2[j - 1]相等
                    dp[i][j] = dp[i - 1][j - 1] + 1; // 那么s1[..i]和s2[..j]的最长公共subsequence就是s1[..i - 1]和s2[..j - 1]的最长公共subsequence加上这个字符
                } else {
                    // 如果不相等
                    dp[i][j] = dp[i - 1][j].max(dp[i][j - 1]); // 是s1[..i - 1]和s2[..j]、或者s1[..i]和s2[..j - 1]的最长公共subsequence
                }
            }
        }

        // 这个递推式理解起来真的挺难的 <https://en.wikipedia.org/wiki/Longest_common_subsequence_problem> 我还没有完全想通，总之先背下来了

        return (s1.len() + s2.len() - dp[s1.len()][s2.len()] * 2) as i32; // 最后结果是第一个字符串的长度减去subsequence长度、加上第二个字符串长度减去subsequence的长度
    }
}

fn main() {
    dbg!(Solution::min_distance("sea".into(), "eat".into())); // 2
}
