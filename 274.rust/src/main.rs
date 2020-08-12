/*
.. default-role:: math

计算H因子

H因子是一个衡量科学家影响力的东西，主要看这个科学家发的文章的被引数。如果一个科学家有至少 `h` 篇文章的被引数大于等于 `h` ，那么这个科学家的H因子就不小于 `h` 。

这样说还是很模糊、很难算。维基百科 <https://en.wikipedia.org/wiki/H-index> 上面有一张图非常清晰，下面就是用这张图算的

1.  先把所有的文章按被引数从高到低排序
2.  被引数最高的文章的下标从1开始，x轴是文章的下标，y轴是被引数，数有多少篇文章在 `y = x` 这条线上、或者左上方
*/

struct Solution;

use std::cmp::Reverse;

impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        let mut citations = citations;
        citations.sort_by_key(|v| Reverse(*v)); // 先按被引数从高到低排序
        return citations
            .into_iter()
            .enumerate()
            .filter(|(i, v)| *v as usize >= *i + 1) // 注意下标从1开始。可能还能用take_while，更快，因为只要遇见一篇文章在y = x右下方，之后的文章都不可能出现在目标区域了
            .count() as i32;
    }
}

fn main() {
    dbg!(Solution::h_index(vec![3, 0, 6, 1, 5])); // 3
    dbg!(Solution::h_index(vec![0])); // 0
    dbg!(Solution::h_index(vec![1, 1])); // 1
}
