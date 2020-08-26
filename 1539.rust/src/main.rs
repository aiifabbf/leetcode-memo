/*
.. default-role:: math

给个从小到大排好序、无重复的、全是正整数的array，问其中漏掉的第 `k` 小的正整数是什么。

比如给 ``[2, 3, 4, 7, 11]`` 要找到第5个漏掉的正整数，所有不在这个array里的正整数从小到大是

::

    1, 5, 6, 8, 9, 10, 12, 13, 14, ...
                ^

第5个正整数是9。

暴力做法就是从1一直往上遍历，遇到一个不在array里的数字，就把 `k` 减1，直到 `k` 是0为止。但是这种做法在 ``[1, 2, 3], 1000000000`` 的时候就不太好。

所以换一种方法，检测两个数之间的间隙，如果间隙里面数字的数量大于等于k的话，那么目标数字就在当前这个间隙里。

比如3, 5之间只有4这一个数字，此时假如k正好是1，那么目标数字就是3 + 1 = 4。

如果间隙里面的数字的数量小于k，那么目标数字不在当前间隙里，在后面的间隙里。

比如3, 5之间只有4这个一个数字，此时假如k是3，那么目标数字应该是下一个间隙的第3 - 1 = 2个数字。
*/

struct Solution;

impl Solution {
    pub fn find_kth_positive(arr: Vec<i32>, k: i32) -> i32 {
        // 暴力做法
        // use std::collections::HashSet;

        // let seen: HashSet<i32> = arr.into_iter().collect();
        // let mut k = k;

        // for i in 1.. {
        //     if !seen.contains(&i) {
        //         k -= 1;
        //     }

        //     if k == 0 {
        //         return i;
        //     }
        // }

        // return 0;

        if arr.is_empty() {
            return k;
        }

        let mut k = k;
        let mut last = 0;

        for v in arr.into_iter() {
            if v - last - 1 >= k {
                // 两个数之间的间隙里的数的数量如果大于等于k的话，比如3, 5之间只有一个数，如果这时候k正好是1，那么就返回3 + 1，如果这时候k是2，那么在下一个间隙里面
                return last + k;
            } else {
                // 两个数之间的间隙里的数的数量小于k，比如3, 5之间只有一个数，但是这时候k = 3，那么目标数字在是下一个间隙里的第3 - 1 = 2个数字
                k = k - (v - last - 1);
                last = v;
            }
        }

        return last + k;
    }
}

fn main() {
    dbg!(Solution::find_kth_positive(vec![2, 3, 4, 7, 11], 5)); // 9
    dbg!(Solution::find_kth_positive(vec![1, 2, 3, 4], 2)); // 6
    dbg!(Solution::find_kth_positive(vec![1, 2], 1)); // 3
}
