/*
.. default-role:: math

简单的拆分单词、处理

-   如果单词第一个字母是元音字母 ``a, i, u, e, o`` ，单词后面加一个 ``ma``
-   如果第一个字母不是元音字母，把第一个字母放到单词的最后，再在后面加一个 ``ma``
-   第 `i` 个单词后面加 `i + 1` 个 ``a``
*/

struct Solution;

impl Solution {
    pub fn to_goat_latin(s: String) -> String {
        let mut res = String::new();

        for (i, v) in s.split_whitespace().enumerate() {
            if i != 0 {
                // 如果不是第0个单词
                res.extend(" ".chars()); // 前面先放个空格
            }

            // match挺好用的
            match &(&v[..1].to_ascii_lowercase())[..] {
                "a" | "i" | "u" | "e" | "o" => {
                    res.extend(v.chars());
                }
                _ => {
                    res.extend(v.chars().skip(1)); // 先放第1个字母起头的substring
                    res.extend(v.chars().take(1)); // 再放第0个字母
                }
            }
            res.extend("ma".chars()); // 每个单词后面都要加ma
            res.extend("a".chars().cycle().take(i + 1)); // 第i个单词放i + 1个a
        }

        return res;
    }
}

fn main() {
    dbg!(Solution::to_goat_latin("I speak Goat Latin".into())); // Imaa peaksmaaa oatGmaaaa atinLmaaaaa
    dbg!(Solution::to_goat_latin(
        "Each word consists of lowercase and uppercase letters only".into()
    )); // Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa
}
