/*
.. default-role:: math

句子能否和模板一一对应。

比如给句子 ``dog cat cat dog`` 和模板 ``abba`` ，可以建立

::

    dog <-- a
    cat <-- b

一一对应的映射。

但是给句子 ``dog cat cat fish`` 和同样的模板 ``abba`` ，不能建立一一对应的映射

::

    fish <---
            |
    dog <-- a
    cat <-- b

因为模板 ``a`` 映射到了两个不同的单词。

同样，给句子 ``dog dog dog dog`` 和模板 ``abba`` 也不行

::

    dog <-- a
     ^
     |
     ------ b

单词 ``dog`` 和两个不同的模板产生了关联。

我的做法是转换成图中节点出度入度的问题。从模板节点出去的边只能有一条、进入单词节点的边也只能有一条。
*/

struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn word_pattern(pattern: String, string: String) -> bool {
        let mut outs = HashMap::new(); // outs[p] = w表示p -> w
        let mut ins = HashMap::new(); // ins[w] = p表示w <- p

        if pattern.chars().count() != string.split_whitespace().count() {
            // 长度不同的时候无法建立联系
            return false;
        }

        for (pattern, word) in pattern.chars().zip(string.split_whitespace()) {
            // 扫描每一条边，建立outs和ins
            match outs.get(&pattern) {
                Some(to) => {
                    // 从p已经有一条边p -> v了
                    if *to != word {
                        // 然而这里居然又有一条从p出去的边p -> w
                        return false; // 不能忍
                    }
                }
                None => {
                    // 之前从来没见过p -> w这条边
                    outs.insert(pattern, word);
                }
            }

            match ins.get(&word) {
                Some(from) => {
                    // 进入w已经有一条边w <- p了
                    if *from != pattern {
                        // 结果这里居然又有一条进入w的边w <- q
                        return false;
                    }
                }
                None => {
                    ins.insert(word, pattern);
                }
            }
        }

        return true;
    }
}

fn main() {
    dbg!(Solution::word_pattern(
        "abba".into(),
        "dog cat cat dog".into()
    )); // true
    dbg!(Solution::word_pattern(
        "abba".into(),
        "dog cat cat fish".into()
    )); // false
    dbg!(Solution::word_pattern(
        "abba".into(),
        "dog dog dog dog".into()
    )); // false
}
