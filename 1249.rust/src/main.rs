/*
.. default-role:: math

删掉字符串里面的一些括号，使得括号合法。删掉最少的括号之后剩下的字符串是怎样的？

比如 ``lee(t(c)o)de)`` 只要删掉最后一个右括号变成 ``lee(t(c)o)de`` 之后就能使得括号合法。

判断括号合法的代码稍加改动就可以了。搞一个stack，每次

-   遇到左括号，就放入stack
-   遇到右括号，看一下stack是否为空

    如果stack为空，说明到这里没有左括号和这个右括号匹配，那么这个右括号只能删掉。

    如果stack不空，说明可以匹配。

最后不要忘了stack里剩下的没有能匹配的左括号，也要全部删掉。因为有可能出现 ``((((()`` 这种情况。
*/

struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn min_remove_to_make_valid(s: String) -> String {
        let mut stack = vec![];
        let mut indexes = HashSet::new(); // 要删掉的下标

        for (i, v) in s.chars().enumerate() {
            match v {
                '(' => {
                    // 默认所有左括号都合法
                    stack.push(i);
                }
                ')' => {
                    // 遇到右括号的时候
                    if stack.is_empty() {
                        // 如果此时没有左括号和它匹配
                        indexes.insert(i); // 那么只能忍痛删掉这个右括号
                    } else {
                        // 如果此时有左括号和它匹配
                        stack.pop(); // 那么匹配
                    }
                }
                _ => {}
            }
        }

        indexes.extend(stack.into_iter()); // 最后不要忘了加上所有没匹配的左括号，也要全部删掉，比如出现((((()这种情况

        return s
            .chars()
            .enumerate()
            .filter(|(i, v)| !indexes.contains(&i)) // 筛选出不需要删的字符
            .map(|(i, v)| v)
            .collect();
    }
}

fn main() {
    dbg!(Solution::min_remove_to_make_valid("lee(t(c)o)de)".into())); // lee(t(c)o)de
    dbg!(Solution::min_remove_to_make_valid("a)b(c)d".into())); // ab(c)d
}
