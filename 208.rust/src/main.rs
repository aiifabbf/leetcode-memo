/*
.. default-role:: math

实现字典树（也叫前缀树）

字典树类似集合，用来判断某个序列（比如字符串）是否在其中。

你可能会想到说那用hash set或者tree set不行吗？可以是可以，但是有点浪费，特别是如果这些序列总是有相同的前缀，比如

::

    head
    headache
    headphone
    headquarter
    headset

如果用hash set的话，需要完整存下每个单词。然而如果用字典树的话，只需要

::

    head -ache
         -phone
         -quarter
         -set

存一次 ``head`` 。如果有更多的单词共享前缀，会更省空间。

时间复杂度和hash set也完全一样，甚至比hash set还要好，因为hash set判断的时候需要扫描一遍待判断的key，算出hash，再到表里面去找hash匹配的起点，可能还有hash碰撞发生，那么还要扫一遍所有hash相同的项目，一个一个比对。而字典树这里直接一次性从根节点往下走，一遍过，不会碰撞。

所以字典树各方面性能都比hash set优秀，为啥没有取代hash set和tree set呢……

主要就2个操作

-   插入

    使得字典树里存在一条从上到下的路径，并且最后一个字符对应的节点上要标记是终止字符。

    很简单，顺着单词里每个字符建一个新的节点。最后别忘记把最后一个节点用什么方法标记一下。

-   查找

    顺着单词里的每个字符能从根节点走下去，并且最后一个经过的节点是终止节点。

    也很简单，顺着单词里的每个字符，试着从根节点开始往下走，如果能走下去走到最后，并且最后经过的那个节点被标记了可终止，那么就说明单词存在。

为啥要有“终止字符”这么奇怪的要求呢？因为很多单词的前缀也是一个单词，比如 ``head`` 的前缀 ``he`` 也是个单词。如果没有终止字符标记的话，在插入 ``head`` 之后，不仅能查到 ``head`` 在字典树里， ``he`` 也在字典树里，这就不对了。

维基百科 <https://en.wikipedia.org/wiki/Trie> 有Python代码。
*/

use std::collections::BTreeMap;

struct Trie {
    value: Option<char>, // value是Some的话表示这个节点代表的字符可以是最后一个字符
    children: BTreeMap<char, Trie>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Trie {
    /** Initialize your data structure here. */
    fn new() -> Self {
        Self {
            value: None,
            children: BTreeMap::new(),
        }
    }

    /** Inserts a word into the trie. */
    fn insert(&mut self, word: String) {
        let mut head = self;

        for v in word.chars() {
            if !head.children.contains_key(&v) {
                head.children.insert(v, Trie::new());
            }
            head = head.children.get_mut(&v).unwrap();
        }

        head.value = Some('\0'); // 最后一个char上标记一下，表示这边可以终止
    }

    /** Returns if the word is in the trie. */
    fn search(&self, word: String) -> bool {
        let mut head = self;

        for v in word.chars() {
            // 顺着单词里的每个字符走下去
            if let Some(child) = head.children.get(&v) {
                head = child;
            } else {
                // 走不下去了
                return false;
            }
        }

        return head.value.is_some(); // 一定要正好在这个char上终止才算数
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    fn starts_with(&self, prefix: String) -> bool {
        let mut head = self;

        for v in prefix.chars() {
            if let Some(child) = head.children.get(&v) {
                head = child;
            } else {
                return false;
            }
        }

        return true; // 不需要一定在这里终止才算数
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie::new();
 * obj.insert(word);
 * let ret_2: bool = obj.search(word);
 * let ret_3: bool = obj.starts_with(prefix);
 */
fn main() {
    let mut obj = Trie::new();
    obj.insert("apple".into());
    dbg!(obj.search("apple".into())); // true
    dbg!(obj.search("app".into())); // false
    dbg!(obj.starts_with("apple".into())); // true
    obj.insert("app".into());
    dbg!(obj.search("app".into())); // true
}

// 开个脑洞，是不是甚至还可以像下面这样做个trie map呢？
// struct TrieMap {
//     value: Option<String>,
//     children: BTreeMap<char, TrieMap>,
// }

// impl TrieMap {
//     fn new() -> Self {
//         Self {
//             value: None,
//             children: BTreeMap::new(),
//         }
//     }

//     fn insert(&mut self, key: String, value: String) {
//         let mut head = self;

//         for v in key.chars() {
//             if !head.children.contains_key(&v) {
//                 head.children.insert(v, TrieMap::new());
//             }
//             head = head.children.get_mut(&v).unwrap();
//         }

//         head.value = Some(value);
//     }

//     fn get(&self, key: &String) -> Option<&String> {
//         let mut head = self;

//         for v in key.chars() {
//             if let Some(child) = head.children.get(&v) {
//                 head = child;
//             } else {
//                 return None;
//             }
//         }

//         return head.value.as_ref();
//     }
// }