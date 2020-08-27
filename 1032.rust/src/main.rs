/*
.. default-role:: math

先给一些单词，然后再一个一个给你字母，问至今为止、按先后顺序给你的所有字母是否存在一个后缀构成单词

比如给你

::

    cd, f, kl

然后每次给你一个字母

::

    a -> false，没见过a这个单词
    b -> false，没见过b、ab
    c -> false，没见过c、bc、abc
    d -> true，没见过d、bcd、abcd，但是见过cd

用trie比较好。先在trie里存单词颠倒过来的镜像，比如给 ``cd, f, kl`` 存 ``dc, f, lk`` 。

每次给一个字母，先存下来，然后倒着去trie里查询，比如到现在为止已经给了 ``abcd`` ，先反过来变成 ``dcba`` ，然后去trie里查 ``d, dc, dcb, dcba`` 。看起来要查4次，其实不用，查一次就够了

1.  从根节点开始，查有没有 ``d`` ，没有的话就是false，有的话看下 ``d`` 是不是终止符，如果是，直接就可以true，如果不是，继续
2.  到下一层节点，查有没有 ``c`` ，没有的话还是false，有的话看下 ``c`` 是不是终止符，如果是，直接true，如果不是，继续
3.  到下一层节点，查有没有 ``b`` ，没有的话还是false，有的话看下 ``b`` 是不是终止符，如果是，直接true，如果不是，继续
4.  到下一次节点，查有没有 ``a`` ，没有的话false，有的话看 ``a`` 是不是终止符，如果是，true，如果不是，继续
5.  如果到底了都没查到，那么false
*/

use std::collections::BTreeMap;

struct Trie {
    value: Option<char>,
    children: BTreeMap<char, Trie>,
}

impl Trie {
    pub fn new() -> Self {
        Self {
            value: None,
            children: BTreeMap::new(),
        }
    }

    pub fn insert(&mut self, word: String) {
        let mut head = self;

        for v in word.chars() {
            if !head.children.contains_key(&v) {
                head.children.insert(v, Trie::new());
            }
            head = head.children.get_mut(&v).unwrap();
        }

        head.value = Some('\0');
    }

    // 这里没用到。对每个后缀都单独查询太慢了。
    // pub fn contains(&self, word: String) -> bool {
    //     let mut head = self;

    //     for v in word.chars() {
    //         if !self.children.contains_key(&v) {
    //             return false;
    //         }
    //         head = head.children.get(&v).unwrap();
    //     }

    //     return head.value.is_some();
    // }
}

struct StreamChecker {
    trie: Trie,      // 存单词的镜像
    path: Vec<char>, // 至今见过的所有的字母，按先后顺序存
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StreamChecker {
    fn new(words: Vec<String>) -> Self {
        let mut trie = Trie::new();

        for word in words.into_iter() {
            let word: String = word.chars().rev().collect(); // cd -> dc
            trie.insert(word); // 存
        }

        return Self {
            trie: trie,
            path: vec![],
        };
    }

    fn query(&mut self, letter: char) -> bool {
        self.path.push(letter);

        let mut head = &self.trie;

        for v in self.path.iter().rev() {
            if !head.children.contains_key(v) {
                // 居然找不到下一个字母，路径到这里断了。只要有一个字母不在，那么更长的后缀更不可能在trie里了
                return false;
            } else {
                head = head.children.get(v).unwrap();
                if head.value.is_some() {
                    // 到此为止可以组成一个单词
                    return true; // 大功告成
                }
                // 目前还没组成一个单词，但有希望，所以继续往下看看能不能凑一个单词
            }
        }

        return head.value.is_some();
    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * let obj = StreamChecker::new(words);
 * let ret_1: bool = obj.query(letter);
 */
fn main() {
    let mut checker = StreamChecker::new(
        vec!["cd", "f", "kl"]
            .into_iter()
            .map(|v| v.to_string())
            .collect(),
    );
    dbg!(checker.query('a')); // false
    dbg!(checker.query('b')); // false
    dbg!(checker.query('c')); // false
    dbg!(checker.query('d')); // true，因为cd
    dbg!(checker.query('e')); // false
    dbg!(checker.query('f')); // true，因为f
    dbg!(checker.query('g')); // false
    dbg!(checker.query('h')); // false
    dbg!(checker.query('i')); // false
    dbg!(checker.query('j')); // false
    dbg!(checker.query('k')); // false
    dbg!(checker.query('l')); // true，因为kl
}
