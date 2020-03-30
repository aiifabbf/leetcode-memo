struct Solution;

use std::collections::HashSet;

impl Solution {
    #[cfg(feature = "kmp")]
    pub fn longest_prefix(s: String) -> String {
        let mut next = vec![0, 0]; // next[j]表示如果s[i] != p[j]，把j回退到next[j]，也就是令j = next[j]，再试一次s[i]和p[j]是否相等。如果回退之后仍然不对，再退。如果退到j = 0之后，还是s[i] != p[0]，就只能把i加1了。
        let p: Vec<char> = s.chars().collect();
        let mut i = 0;

        for j in 2..p.len() + 1 {
            if p[j - 1] == p[i] {
                // 可以接着前一个后缀继续下去
                i += 1;
            } else {
                // 接不下去了
                // next.push(0); // 千万要记得这里不是直接变成0，一个反例是ABABCABAA，如果到ABABCABA，现在来了个A，应该是回退到状态1，而不是状态0，因为ABABCABAA的最长公共前后缀是A
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

        return p.into_iter().take(next.last().cloned().unwrap()).collect();
    }

    #[cfg(feature = "rolling-hash")]
    pub fn longest_prefix(s: String) -> String {
        let s: Vec<char> = s.chars().collect();
        let mut prefixes = HashSet::new();
        let mut rolling = 0u64;

        for i in 1..s.len() + 1 {
            rolling = rolling.wrapping_mul(26).wrapping_add(s[i - 1] as u64 - 97); // 不用modulo，wrapping就好了
            prefixes.insert(rolling);
        }

        let mut res: &[char] = &[]; // 这里不能省略type hint，不然会认为是一个0长度的slice……
        let mut rolling = 0;
        let mut exponent = 0;

        for i in (1..s.len()).rev() {
            rolling = (s[i] as u64 - 97)
                .wrapping_mul(26u64.wrapping_pow(exponent))
                .wrapping_add(rolling);
            exponent += 1;
            if prefixes.contains(&rolling) && &s[i..] == &s[..s.len() - i] {
                res = &s[i..];
            }
        }

        return res.into_iter().collect();
    }
}

fn main() {
    println!("{:?}", Solution::longest_prefix("level".to_string())); // l
    println!("{:?}", Solution::longest_prefix("ababab".to_string())); // abab
    println!("{:?}", Solution::longest_prefix("leetcodeleet".to_string())); // leet
    println!("{:?}", Solution::longest_prefix("a".to_string())); // ""
    println!(
        "{:?}",
        Solution::longest_prefix("babbbbcaaabbbaabbabacbabbbbcaaabbbaa".to_string())
    ); // babbbbcaaabbbaa
    println!("{:?}", Solution::longest_prefix("bba".to_string())); // ""
    println!("{:?}", Solution::longest_prefix("aaaaa".to_string())); // aaaa
    println!(
        "{:?}",
        Solution::longest_prefix("acccbaaacccbaac".to_string())
    ); // ac
    println!(
        "{:?}",
        Solution::longest_prefix("ccabcbbacbcbbacccabaabcccabcbbacbcbbac".to_string())
    ); // ccabcbbacbcbbac
}
