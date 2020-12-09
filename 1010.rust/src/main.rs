/*
.. default-role:: math

给个array，有多少对 `(i, j), i < j` 使得 `(a_i + a_j) \bmod 60 = 0` ？

暴力做法是两个for循环，复杂度是 `O(n^2)` 。

观察一下，59和1能凑一对，59和61也能凑一对……说明啥呢？59可以和 `60k + 1` 凑一对。

所以只要把每个数都对60取余数，然后看前面见过多少次60减去这个余数就可以了，比如现在到59，那么只要看前面出现了多少个对60取余数得到1的数字（比如1、61、121、……）就可以了。用hash map或者array也行，来保存前面出现过多少个对60取余数之后得到1的数字。

推广一下，遇到 `a_j` 的时候，去看前面出现了多少个 `60 - a_j \bmod 60` 。hash map里的key是前面出现了多少个 `a_i \bmod 6 = k` 的 `i` 。

有个小陷阱，出现在正好是60的倍数的时候。比如60和60能凑一对，60能和120凑一对，可是60和120对60取余数都得到0，那么 `60 - 60 \bmod 60 = 60` ，需要去看前面出现了多少个对60取余数之后得到60的数字，显然是没有的，任何数字对60取余数都不可能超过59。

这时候就特殊处理一下，去看前面出现了多少个对60取余数之后得到0的数字。
*/

struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn num_pairs_divisible_by60(time: Vec<i32>) -> i32 {
        let mut counter: HashMap<i32, usize> = HashMap::new(); // counter[k] = v表示前面出现了v个对60取余数得到k的数字，比如counter[1] = 2表示前面出现了2个对60取余数得到1的数字（可能是61、121之类的数字）
        let mut res = 0;

        for v in time.into_iter() {
            let target = if v % 60 == 0 { 0 } else { 60 - v % 60 }; // 假设a[j]是59，那么只要看前面出现过多少个对60取余数是1的数字；假设a[j]正好是60，那么只要看前面出现过多少个对60取余数是0的数字
            res += counter.get(&target).cloned().unwrap_or(0);
            *counter.entry(v % 60).or_insert(0) += 1;
        }

        return res as i32;
    }
}

fn main() {
    dbg!(Solution::num_pairs_divisible_by60(vec![
        30, 20, 150, 100, 40
    ])); // 3
    dbg!(Solution::num_pairs_divisible_by60(vec![60, 60, 60])); // 3
}
