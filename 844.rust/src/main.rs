/*
给两串键位序列， ``#`` 表示退格，问最终这两组键位打出的句子是否相同。

很简单，用个stack保存现在输入的东西。遇到 ``#`` 就pop。最后比较一下两个键位打出来的句子是否一样就好了。
*/

struct Solution;

impl Solution {
    pub fn backspace_compare(s: String, t: String) -> bool {
        return Solution::editorResult(s) == Solution::editorResult(t);
    }

    fn editorResult(s: String) -> String {
        let mut stack = vec![];

        for v in s.chars() {
            match v {
                '#' => {
                    stack.pop(); // 空的句子按退格没作用
                }
                v => {
                    stack.push(v);
                }
            }
        }

        return stack.iter().collect();
    }
}

fn main() {
    println!(
        "{:?}",
        Solution::backspace_compare("ab#c".to_string(), "ad#c".to_string())
    ); // true
    println!(
        "{:?}",
        Solution::backspace_compare("ab##".to_string(), "c#d#".to_string())
    ); // true
    println!(
        "{:?}",
        Solution::backspace_compare("a##c".to_string(), "#a#c".to_string())
    ); // true
    println!(
        "{:?}",
        Solution::backspace_compare("a#c".to_string(), "b".to_string())
    ); // true
}
