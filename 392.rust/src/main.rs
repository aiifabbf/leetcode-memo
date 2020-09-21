/*
.. default-role:: math

判断s是不是t的subsequence（可以不连续）

这个比判断s是不是t的substring简单太多了。想一想如果人手动做这件事情好不好做，很好做：拿着s的第0个字符，去t里面找 ``s[0]`` 第一次出现的位置，如果没找到，说明s不是t的subsequence；如果找到了，再拿着s的第1个字符

用非对称双指针来做，搞一个指向s的 ``seek`` 指针，保证 ``s[..seek]`` 任何时候都是t的subsequence。 ``seek`` 一开始是0。然后遍历t里的每个字符，看等不等于 ``s[seek]`` ，如果等于，那么 ``seek`` 自增1。

因为 ``s[..seek]`` 一定是t的subsequence，如果最后seek指到了s的最后，说明整个s都是t的subsequence。

这题还有点greedy的感觉。为啥只要第一次在t里遇到和 ``s[seek]`` 相等的字符的时候就要让 ``seek`` 自增1呢？为什么不是下一次遇到相同的字符再自增1呢？
*/

struct Solution;

impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let mut seek = 0;
        let s = s.as_bytes();

        for v in t.bytes() {
            if seek == s.len() {
                // seek已经指向s最后了，根据定义，s[..seek]一定是t的subsequence
                return true; // 所以s是t的subsequence
            } else {
                if v == s[seek] {
                    // 当前字符等于s[seek]
                    seek += 1; // 那么s[..seek + 1]是t的subsequence
                } // 如果不等于也不要紧，继续看下一个
            }
        }

        return seek == s.len(); // 最后出去的时候还要判断一下
    }
}

pub fn main() {
    println!(
        "{:?}",
        Solution::is_subsequence("abc".to_string(), "ahbgdc".to_string())
    ); // true
    println!(
        "{:?}",
        Solution::is_subsequence("axc".to_string(), "ahbgdc".to_string())
    ); // false
}
