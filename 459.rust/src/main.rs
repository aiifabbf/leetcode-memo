/*
.. default-role:: math

给个string，问这个string能不能通过一个pattern重复多次（大于1次）生成。

比如给 ``abab`` ，可以用 ``ab`` 重复两次来生成； ``abcabcabc`` 可以用 ``abc`` 重复三次来生成；而 ``aba`` 无法通过某个pattern重复多次生成。

暴力做法能过。
*/

struct Solution;

impl Solution {
    pub fn repeated_substring_pattern(s: String) -> bool {
        let s = s.as_bytes(); // String -> &[u8]

        for length in 1..s.len() {
            // 模板的长度必须是原字符串长度的因数
            if s.len() % length == 0 {
                let mut chunks = (&s[..]).chunks_exact(length);
                // chunks_exact()把slice切成每个长度都是length的substring slice，不满length的忽略；如果是chunks()，不满length的会保留 // <https://doc.rust-lang.org/std/primitive.slice.html#method.chunks_exact>
                let pattern = chunks.next().unwrap();
                if chunks.all(|v| v == pattern) {
                    // 如果每个substring都和第一个substring相同
                    return true;
                }
            }
        }

        return false;
    }
}

fn main() {
    dbg!(Solution::repeated_substring_pattern("abab".into())); // true
    dbg!(Solution::repeated_substring_pattern("aba".into())); // false
    dbg!(Solution::repeated_substring_pattern("abcabcabcabc".into())); // true
}
