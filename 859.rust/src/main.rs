/*
给两个array，能否调换第一个array里的两个元素，使得第一个array和第二个array相等。

注意一定要调换，并且只能调换一次。

很简单，有这几种情况

-   如果长度不相等

    那么不可能。

-   如果长度相等

    两个array做一次diff，继续细分，有这几种情况

    -   如果两个array已经完全相等了

        但是规定必须调换一次，那怎么办呢？看一下第一个array里有没有哪个元素出现了两次，那么调换这两个相同的元素，array看上去没变。所以这种情况下是可以的。

        如果第一个array里所有元素都没有重复出现，就没办法了。

    -   如果两个array只有一处不同

        无论如何都不可能。

        比如 ``aa, ab`` 。无论怎么调换都不可能。

    -   如果有两处不同

        要看这两处不同具体怎么不同法，如果是 ``ab, ba`` 这种不同，那么是可以的，如果是 ``ab, ca`` 这种，就不行。

    -   如果有大于两处不同

        无论如何都不可能。
*/

struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn buddy_strings(a: String, b: String) -> bool {
        let a: Vec<char> = a.chars().collect();
        let b: Vec<char> = b.chars().collect();
        if a.len() != b.len() {
            // 如果长度不同，无论如何都不可能
            return false;
        } else {
            let diffs: Vec<usize> = a
                .iter()
                .zip(b.iter())
                .enumerate()
                .filter(|(i, (v, w))| v != w) // 把a[i] != b[i]的i挑出来
                .map(|(i, (v, w))| i)
                .collect();
            return match diffs.len() {
                0 => a.iter().cloned().collect::<HashSet<char>>().len() != a.len(),
                1 => false,
                2 => a[diffs[0]] == b[diffs[1]] && a[diffs[1]] == b[diffs[0]],
                _ => false,
            };
        }
    }
}

fn main() {
    dbg!(Solution::buddy_strings("ab".into(), "ba".into())); // true
    dbg!(Solution::buddy_strings("ab".into(), "ab".into())); // false
    dbg!(Solution::buddy_strings("aa".into(), "aa".into())); // true
    dbg!(Solution::buddy_strings(
        "aaaaaaabc".into(),
        "aaaaaaacb".into()
    )); // true
    dbg!(Solution::buddy_strings("".into(), "aa".into())); // false
}
