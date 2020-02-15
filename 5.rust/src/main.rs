struct Solution;

impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let s: Vec<char> = s.chars().collect();
        let mut dp: Vec<Vec<bool>> = vec![vec![false; s.len() + 1]; s.len() + 1]; // dp[i][j] = true表示s[i..j]是回文substring
        let mut res: Vec<char> = Vec::new(); // 目前为止见到的最长的回文substring

        for i in 0..dp.len() { // 初始条件s[i..i]是空字符串，所以肯定是回文string
            dp[i][i] = true;
        }

        for i in 0..dp.len() - 1 { // 初始条件s[i..i+1]是只有一个字符的字符串，所以肯定也是回文的
            dp[i][i + 1] = true;
        }
        
        if s.len() > 0 {
            res.push(s[0]); // 目前为止见到的最长的回文substring就是其中一个
        }

        for i in (0..dp.len()).rev() { // i是倒过来、从下往上遍历的
            for j in i + 2..dp[0].len() { // s[i..i+1]已经是初始条件了，所以不用管了，直接从s[i..i+2]开始就行了
                if s[i] == s[j - 1] && dp[i + 1][j - 1] == true {
                    dp[i][j] = true;
                    if j - i > res.len() {
                        res.clear();
                        res.extend(s[i..j].iter());
                    }
                }
            }
        }

        return res.into_iter().collect::<String>(); // 很奇怪Vec<char>居然没有join方法
    }

    // 最长回文substring问题不能像最长回文subsequence转换到最长公共subsequence那样、转化到最长公共substring
    // 典型反例"aacdefcaa"
    // pub fn longestCommonSubstring<T: PartialEq + Clone>(s: &Vec<T>, t: &Vec<T>) -> Vec<T> {
    //     let mut dp: Vec<Vec<usize>> = vec![vec![0; t.len() + 1]; s.len() + 1];
    //     let mut res: Vec<T> = Vec::new();

    //     for i in 1..dp.len() {
    //         for j in 1..dp[0].len() {
    //             if s[i - 1] == t[j - 1] {
    //                 dp[i][j] = dp[i - 1][j - 1] + 1;
    //                 if dp[i][j] > res.len() {
    //                     res.clear();
    //                     res.extend(s[i - dp[i][j]..i].iter().cloned());
    //                 }
    //             }
    //         }
    //     }

    //     return res;
    // }
}

pub fn main() {
    println!("{:?}", Solution::longest_palindrome("babad".to_string())); // bab;
    println!("{:?}", Solution::longest_palindrome("cbbd".to_string())); // bb
    println!("{:?}", Solution::longest_palindrome("a".to_string())); // a
    println!(
        "{:?}",
        Solution::longest_palindrome("aacdefcaa".to_string())
    ); // aa
    // 这是最著名的反例
}
