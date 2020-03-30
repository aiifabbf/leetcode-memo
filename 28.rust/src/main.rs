/*
.. default-role:: math

实现 ``indexOf()`` ，给出某个substring在array中的最左起始下标。

这个问题真的是花了巨多时间。我觉得我的智力极限能想到rolling hash……

假设string的长度是 `n` ，substring的长度（也即是pattern）的长度是 `k` 。

暴力就是定位string里面每个长度为 `k` 的substring，然后一个一个比较，注意一个一个字符比较的话，比较一次就是 `O(k)` ，所以整个复杂度是 `O((n - k) k) = O(n k)` 。

稍微优化一点的就是rolling hash。能不能不要一个一个字符比较？能不能让比较一次的复杂度降低到 `O(1)` ？可以的。搞一个叫做hash的东西。可是传统的hash要计算那个substring的hash还是至少要扫描一遍substring的，复杂度还是 `O(k)` 。那有没有办法，
*/

struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        let s: Vec<char> = haystack.chars().collect();
        let p: Vec<char> = needle.chars().collect();

        return match Solution::indexOf(&s[..], &p[..]) {
            Some(i) => i as i32,
            None => -1,
        };
    }

    // KMP的一种版本，用next数组
    #[cfg(feature = "kmp-next")]
    pub fn indexOf(s: &[char], p: &[char]) -> Option<usize> {
        // 先排除两种trivial的情况
        if p.is_empty() {
            // pattern是空的
            return Some(0); // 空字符串是任何字符串的substring
        }
        if p.len() > s.len() {
            // pattern比原字符串还长
            return None; // 根本不可能
        }

        let mut next = vec![0, 0]; // next[j]表示，如果当前s[i] != p[j]的话，j要回退到next[j]，再试一次s[i]是否等于p[j]。如果j回退到0之后，s[i]仍然不等于p[0]，那么说明从第一个字符开始就不匹配，只能i += 1了
        let mut i = 0;

        for j in 2..p.len() + 1 {
            if p[j - 1] == p[i] {
                i += 1;
            } else {

                while i != 0 {
                    i = next[i];
                    if p[j - 1] == p[i] {
                        i += 1;
                        break;
                    }
                }

            }
            next.push(i);
        }

        let mut i = 0; // i是s上的指针
        let mut j = 0; // j是p上的指针

        while i != s.len() {
            // 将要比较s[i]和p[j]
            if s[i] == p[j] {
                // 如果相等
                i += 1;
                j += 1; // 两个指针同时往下一格移动
                if j == p.len() {
                    // j已经移动到pattern的最后了
                    return Some(i - p.len()); // 说明找到了substring
                }
            } else {
                // 不相等，试图把j回退到next[j]
                if j == 0 {
                    // 但是如果j本身已经是0了，s[i]还是不等于p[0]
                    i += 1; // 那么只能比较下一个字符了
                } else {
                    // j不是0
                    j = next[j]; // 试着回退一次
                }
            }
        }

        return None; // i已经指到最后了，s全部比较完了，都没能找到相同的substring，说明根本不存在
    }

    // KMP的一种版本，状态机
    // 没写完
    #[cfg(feature = "kmp-dfa")]
    pub fn indexOf(s: &[char], p: &[char]) -> Option<usize> {
        let mut automata = HashMap::new();
        let mut x = 0;

        for (i, v) in p.iter().enumerate() {
            let mut subAutomata = HashMap::new();
            subAutomata.insert(v, i + 1);
            automata.insert(i, subAutomata); // 这样automata[s][i]就是在状态s、遇到输入i之后的目标状态了
            match automata[&x].get(&p[i]) {
                Some(v) => x = *v,
                None => x = 0,
            };
        }

        let startState = 0; // 初始状态
        let endState = p.len(); // 终止状态
        let errorState = 0; // 遇到错误回到初始状态

        println!("{:?}", automata);
        return None;
    }

    // rolling hash实现的indexOf
    #[cfg(feature = "rolling-hash")]
    pub fn indexOf(s: &[char], p: &[char]) -> Option<usize> {
        if p.is_empty() {
            // pattern居然是空字符串
            return Some(0);
        } else if p.len() > s.len() {
            // pattern居然比string还长
            return None; // 那pattern绝对不可能是string的某个substring的
        }

        let mut patternHash: u128 = 0; // 用u128表示这个hash，这样不会溢出……

        for (i, v) in p.iter().enumerate() {
            patternHash += (*v as u128) * 256_u128.pow(i as u32); // 算出pattern的hash
        }

        let mut windowHash: u128 = 0;

        for (i, v) in s.iter().take(p.len()).enumerate() {
            windowHash += (*v as u128) * 256_u128.pow(i as u32);
        }

        if windowHash == patternHash && &p[..] == &s[0..p.len()] {
            return Some(0);
        }

        for i in 1..s.len() - p.len() + 1 {
            windowHash = windowHash / 256;
            windowHash += (s[p.len() + i - 1] as u128) * 256_u128.pow(p.len() as u32 - 1);
            if windowHash == patternHash {
                // hash相同了，两个substring大概率能相等，但是也有可能不等的
                if &p[..] == &s[i..p.len() + i] {
                    // 所以还要再一个一个比较一下
                    return Some(i);
                }
            }
        }

        return None;
    }
}

pub fn main() {
    println!(
        "{:?}",
        Solution::str_str("hello".to_string(), "ll".to_string())
    ); // 2
    println!(
        "{:?}",
        Solution::str_str("aaaaa".to_string(), "bba".to_string())
    ); // -1
    println!(
        "{:?}",
        Solution::str_str("mississippi".to_string(), "pi".to_string())
    ); // 9
    println!(
        "{:?}",
        Solution::str_str("ababcaababcaabc".to_string(), "ababcaabc".to_string())
    ); // 6
    println!(
        "{:?}",
        Solution::str_str("abababc".to_string(), "ababc".to_string())
    ); // 2
    println!("{:?}", Solution::str_str("".to_string(), "".to_string())); // 0
    println!("{:?}", Solution::str_str("a".to_string(), "".to_string())); // 0
    println!("{:?}", Solution::str_str("".to_string(), "aa".to_string())); // -1
}
