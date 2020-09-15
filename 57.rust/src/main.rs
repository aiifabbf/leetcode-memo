/*
.. default-role:: math

给一个按开始时间从小到大排好序的区间数组，现在要插入一个新的区间，插入之后，再精简区间。

.. 要吐了，精简区间的题目怎么这么多啊。

直接归约到之前做过的精简区间的题目。先二分搜索，找到新的区间插入的位置，使得新区间插入之后，原数组保持有序，然后直接插入。插入之后再按之前的做法做就好了。
*/

struct Solution;

impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut intervals = intervals;
        let index = match intervals.binary_search(&new_interval) {
            Ok(v) => v,
            Err(v) => v,
        }; // 找到new_interval插入的位置，使得new_interval插入到intervals之后，intervals仍然是以开始时间从小到大有序的
        intervals.insert(index, new_interval);

        // 然后这个问题就归约到了我们以前解决过的精简区间的问题了
        let mut stack = vec![];

        for v in intervals.into_iter() {
            if stack.is_empty() {
                stack.push(v);
            } else {
                if stack.last().unwrap()[1] < v[0] {
                    // [1, 2)和[2, 3)要合并成[1, 3)，所以用小于号
                    stack.push(v);
                } else {
                    let mut merged = stack.pop().unwrap();
                    merged[0] = merged[0].min(v[0]);
                    merged[1] = merged[1].max(v[1]);
                    stack.push(merged);
                }
            }
        }

        return stack;
    }
}

fn main() {
    dbg!(Solution::insert(vec![vec![1, 3], vec![6, 9],], vec![2, 5])); // [1, 5], [6, 9]
    dbg!(Solution::insert(
        vec![
            vec![1, 2],
            vec![3, 5],
            vec![6, 7],
            vec![8, 10],
            vec![12, 16],
        ],
        vec![4, 8]
    )); // [1, 2], [3, 10], [12, 16]
}
