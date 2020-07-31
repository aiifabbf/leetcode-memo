/*
.. default-role:: math

给一个array，从array里先后取三个数字、取完不放回，问这三个数字加起来的和离target最近是多少

比如 ``[-1, 2, 1, -4]`` ，目标和是1，总共有3种取法

::

    -1 + 2 + 1 = 2
    -1 + 2 - 4 = -3
    2 + 1 - 4 = -1

其中，取-1、2、1的时候和是2，离target最近。

最暴力的做法就是遍历每个 `(i, j, k)` ，其中 `i < j < k` ，算出每个 `a_i + a_j + a_k` 和target的差值的绝对值，找到那个使差值的绝对值最小的一组 `(i, j, k)` 。这样复杂度是 `O(n^3)` 。

我觉得比较容易理解的做法是固定 `i, j` ，然后用二分找到 `k` ，这样的话复杂度是 `O(n^2 \ln n)` 。对于每个 `i` ，对于每个 `j > i` ，用二分找到能使差值绝对值最小的 `k > j` 。

那么怎样的 `k` 能够使得 `a_i + a_j + a_k` 和target的差值的绝对值最小呢？最理想的肯定是 `t - a_i - a_j` 。如果存在一个 `a_k = t - a_i - a_j` ，那么 `a_i + a_j + a_k` 对target的差值的绝对值直接就是0。

可惜这样的数可能不存在，所以我们要找个在 `j` 后面找个尽量接近 `t - a_i - a_j` 的数字。怎么找呢？当然是假装将要插入这个数字，二分搜索把它插入后、仍然能保持array有序的位置。这个位置左右两边的数就是整个数列里最接近 `t - a_i - a_j` 的两个数字了。取这两个数字作为 `a_k` ，能够使 `a_i + a_j + a_k` 尽量接近target。
*/

struct Solution;

impl Solution {
    pub fn three_sum_closest(nums: Vec<i32>, target: i32) -> i32 {
        if nums.len() < 3 {
            return nums.into_iter().sum();
        }

        let mut array = nums;
        array.sort();

        let mut res: i32 = array.iter().take(3).sum();

        for (i, v) in array.iter().enumerate() {
            for (j, w) in array.iter().enumerate().take(array.len() - 1).skip(i + 1) {
                // 找到一个k使得a[i] + a[j] + a[k]最接近target
                // 怎么找呢？假设有一个a[k]正好就等于target - a[i] - a[j]，那么a[k]会在哪个位置呢？
                let mut left = j + 1; // 限定k >= j + 1
                let mut right = array.len(); // 限定k <= len

                while left < right {
                    let middle = (left + right) / 2;
                    if array[middle] < target - v - w {
                        left = middle + 1;
                    } else if array[middle] > target - v - w {
                        right = middle;
                    } else {
                        // 如果相等就找到最靠左的
                        right = middle;
                    }
                }

                // 到这里，left就是target - a[i] - a[j]的最佳插入位置。取这个位置左右两边的数字能够使a[i] + a[j] + a[k]最接近target

                // 先试试取右边的数字
                if left < array.len() {
                    // 注意越界
                    if (v + w + array[left] - target).abs() < (res - target).abs() {
                        res = v + w + array[left];
                    }
                }

                // 再试试取左边的数字
                if left - 1 < array.len() && left - 1 > j {
                    if (v + w + array[left - 1] - target).abs() < (res - target).abs() {
                        res = v + w + array[left - 1];
                    }
                }
            }
        }

        return res;
    }
}

fn main() {
    dbg!(Solution::three_sum_closest(vec![-1, 2, 1, -4], 1)); // 2
    dbg!(Solution::three_sum_closest(vec![1, 1, 1, 0], 100)); // 3
}
