/*
给一个字符串，选择其中尽可能多的字符，每个字符只能用一次，组成一个尽可能长的回文字符串，这个回文字符串最长能有多长？

用贪心秒做。想一下作为人类怎么做这件事情。现在你面前有一堆字母卡片，你怎么选出这些字母卡片，组成最长的回文字符串？肯定是统计出每个字母出现的次数。如果某个字母出现了偶数次，很幸运，这个字母的那几张卡片可以全部拿来组成回文字符串的一部分；如果出现了奇数次，就不行了，只能取偶数张、剩一张在桌上。

如果最后偶数的全取完了，比如构成了 ``acbbca`` ，桌面上还有剩的一张 ``k`` ，那么可以把这一张插到最中间去，变成 ``acbkbca`` 。
*/

struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let mut counter = HashMap::new(); // 统计每种字母出现的次数

        for v in s.chars() {
            *counter.entry(v).or_insert(0) += 1;
        }

        let mut residualExists = false; // 桌面上有没有落单的卡片
        let mut res = 0;

        for (k, v) in counter.iter() {
            if v % 2 == 0 {
                // 如果这种字母出现了偶数次
                res += v; // lucky！全部拿来
            } else {
                // 如果这种字母出现了奇数次
                res += v - 1; // 那么只能全抽完剩一张
                residualExists = true;
            }
        }

        return res
            + match residualExists {
                false => 0,
                true => 1,
            }; // 到最后如果桌面上有剩的，可以插到最中间。如果没有剩的，那也没了
    }
}

fn main() {
    println!("{:?}", Solution::longest_palindrome("abccccdd".to_string())); // 7
}
