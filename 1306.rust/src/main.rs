/*
.. default-role:: math

给个array，在第 `i` 个元素上的时候，可以选择跳到 `i - a_i` 或者 `i + a_i` ，但不能跳出array。问从 ``start`` 起跳，能否跳到某个 ``array[i] == 0`` 的地方？

经典BFS。用一个queue，里面一开始放 ``start`` ，然后不停从queue的前面pop出来，跳到下一个地方，下一个下标放到queue的最后。
*/

struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn can_reach(arr: Vec<i32>, start: i32) -> bool {
        let mut queue = HashSet::with_capacity(arr.len());
        queue.insert(start); // 一开始放起跳的下标
        let mut traveled = HashSet::with_capacity(arr.len()); // 记录一下已经遍历过的下标

        while !queue.is_empty() {
            let mut level_queue = HashSet::with_capacity(arr.len());

            for node in queue.iter().cloned() {
                if arr[node as usize] == 0 {
                    // 跳到了某个值是0的位置
                    return true;
                }

                for target in [node - arr[node as usize], node + arr[node as usize]]
                    .iter()
                    .cloned()
                {
                    if arr.get(target as usize).is_some() {
                        // 不能跳到array的外面
                        if !traveled.contains(&target) && !level_queue.contains(&target) {
                            level_queue.insert(target);
                        }
                    }
                }

                traveled.insert(node);
            }

            queue = level_queue;
        }

        return false;
    }
}

fn main() {
    dbg!(Solution::can_reach(vec![4, 2, 3, 0, 3, 1, 2], 5)); // true
    dbg!(Solution::can_reach(vec![4, 2, 3, 0, 3, 1, 2], 0)); // true
    dbg!(Solution::can_reach(vec![3, 0, 2, 1, 2], 2)); // false
}
