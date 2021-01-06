/*
单词前半部分和后半部分是否有相同数量的元音字母？
*/

struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn halves_are_alike(s: String) -> bool {
        let vowels: HashSet<char> = "aiueo".chars().collect();
        let is_vowel = |v: &char| -> bool { vowels.contains(&v.to_ascii_lowercase()) }; // 是否是元音字母
        return s.chars().take(s.len() / 2).filter(is_vowel).count()
            == s.chars().skip(s.len() / 2).filter(is_vowel).count();
    }
}

fn main() {
    dbg!(Solution::halves_are_alike("book".to_owned())); // true
    dbg!(Solution::halves_are_alike("textbook".to_owned())); // false
    dbg!(Solution::halves_are_alike("MerryChristmas".to_owned())); // false
    dbg!(Solution::halves_are_alike("AbCdEfGh".to_owned())); // true
}
