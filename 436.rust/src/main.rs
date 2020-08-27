/*
.. default-role:: math

给一个全是区间的array，对于其中每个区间 `i` ，找到一个最小的 `j` ，使得区间 `j` 的起始时间大于等于区间 `i` 的结束时间。

比如给

::

    [1, 4), [2, 3), [3, 4)

对于 ``[1, 4)`` ，找不到一个区间的起始时间大于等于4；对于 ``[2, 3)`` ，第一个起始时间大于等于3的区间是下标为2的 ``[3, 4)`` ；对于 ``[3, 4)`` ，同样找不到一个区间的起始时间大于等于4。所以答案是

::

    -1, 2, -1

典型二分搜索。先记下所有的区间和它们的下标，比如

::

    (0, [1, 4)), (1, [2, 3)), (2, [3, 4))

再按开始时间从小到大、下标从小到大排序，因为是要找最小的 `j` 。上面的例子按这个规则排序之后是

::

    (0, [1, 4)), (1, [2, 3)), (2, [3, 4))

然后就简单了，对于每个区间，把它的结束时间作为目标数字，去区间里找它的插入位置。比如现在假设要找 `[1, 4)` 的插入位置，那么

::

    (0, [1, 4))
            ^-- target是这个

    (0, [1, 4)), (1, [2, 3)), (2, [3, 4))
         ^            ^            ^-- 比较对象是这个

比较之后

::

    (0, [1, 4))
            ^------------------------------
                                          v
    (0, [1, 4)), (1, [2, 3)), (2, [3, 4)) |
         ^            ^            ^      ^-- 似乎应该放在这里

说明对于 `[1, 4)` ，找不到一个区间 `j` 使得区间 `j` 的开始时间大于等于 `[1, 4)` 的结束时间。
*/

struct Solution;

impl Solution {
    pub fn find_right_interval(intervals: Vec<Vec<i32>>) -> Vec<i32> {
        let mut intervals: Vec<(usize, Vec<i32>)> = intervals.into_iter().enumerate().collect(); // 把intervals变成[(下标，区间)]
        intervals.sort_by_key(|v| (v.1[0], v.0)); // 按照区间的起始时间从小到大、下标从小到大排序

        let mut res = vec![-1; intervals.len()];

        for v in intervals.iter() {
            // 然后对于每个区间i都去二分搜索
            // let start = v.1[0];
            let end = v.1[1];
            let index = v.0; // 记住现在是区间i，要找区间j

            let target = end; // 目标数字是当前区间的结束时间

            let mut left = 0;
            let mut right = intervals.len();

            while left < right {
                let middle = (left + right) / 2;
                if target > intervals[middle].1[0] {
                    // 比较对象是另一个区间的起始时间
                    left = middle + 1;
                } else if target < intervals[middle].1[0] {
                    right = middle;
                } else {
                    right = middle;
                }
            }

            if left == intervals.len() {
                // 没找到
                res[index] = -1;
            } else {
                res[index] = intervals[left].0 as i32;
            }
        }

        return res;
    }
}

fn main() {
    dbg!(Solution::find_right_interval(vec![vec![1, 2],])); // [-1]
    dbg!(Solution::find_right_interval(vec![
        vec![3, 4],
        vec![2, 3],
        vec![1, 2],
    ])); // [-1, 0, 1]
    dbg!(Solution::find_right_interval(vec![
        vec![1, 4],
        vec![2, 3],
        vec![3, 4],
    ])); // [-1, 2, -1]
}
