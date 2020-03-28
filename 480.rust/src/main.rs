/*
.. default-role:: math

给一个长度是 `n` 的array，算出每个长度是 `k` 的窗口里的中位数。

别想复杂了，先从暴力开始。窗口里面的元素从小到大排序，每次移动窗口的时候，删掉旧元素、加入新元素，再取出中位数。这样复杂度是 `O(n k)` 。
*/

struct Solution;

use std::collections::BinaryHeap;
use std::collections::HashMap;

impl Solution {
    // 尝试用和295一样的做法
    #[cfg(feature = "heap")]
    pub fn median_sliding_window(nums: Vec<i32>, k: i32) -> Vec<f64> {}
    // 以后再说……做不来

    // 就用array的话，复杂度是O(n k)，也能过
    #[cfg(feature = "array")]
    pub fn median_sliding_window(nums: Vec<i32>, k: i32) -> Vec<f64> {
        let k = k as usize;
        let mut window: Vec<i32> = nums.iter().cloned().take(k).collect(); // 初始窗口
        window.sort();
        let mut res = vec![];

        if k % 2 == 1 {
            // 如果窗口大小是奇数
            res.push(window[k / 2] as f64); // 第k / 2个就是中位数
        } else {
            // 如果窗口大小是偶数
            res.push((window[k / 2 - 1] as f64 + window[k / 2] as f64) / 2_f64);
            // 第k / 2 - 1和第k / 2的平均是中位数
        }

        for i in 1..nums.len() - k + 1 {
            // 窗口左边界的范围是[1, n - k]
            let index = window.binary_search(&nums[i - 1]).unwrap(); // 虽然这里是二分搜索，但是后面会remove和insert，不可能做到ln k的
            window.remove(index); // 删掉上一个窗口的第一个元素。这一步复杂度就是O(k)了

            let index = match window.binary_search(&nums[i - 1 + k]) {
                Ok(i) => i,
                Err(i) => i, // 如果元素不在里面，Err(i)是插入后保持原序的位置
            };
            window.insert(index, nums[i - 1 + k]); // 加入新窗口的元素

            // 算出中位数
            if k % 2 == 1 {
                res.push(window[k / 2] as f64);
            } else {
                res.push((window[k / 2 - 1] as f64 + window[k / 2] as f64) / 2_f64);
            }
        }

        return res;
    }
}

fn main() {
    println!(
        "{:?}",
        Solution::median_sliding_window(vec![1, 3, -1, -3, 5, 3, 6, 7], 3)
    ); // [1, -1, -1, 3, 5, 6]
    println!("{:?}", Solution::median_sliding_window(vec![1, 4, 2, 3], 4)); // [2.5]
    println!(
        "{:?}",
        Solution::median_sliding_window(vec![2147483647, 1, 2, 3, 4, 5, 6, 7, 2147483647], 2)
    );
}
