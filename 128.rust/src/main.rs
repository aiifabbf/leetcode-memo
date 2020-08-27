/*
.. default-role:: math

给个array（可能有重复数字），从里面挑数字出来，最长能组成多长的连续整数序列？

比如给 ``100, 4, 200, 1, 3, 2`` ，可以组成3个连续整数序列

::

    100
    200
    1, 2, 3, 4

其中 ``1, 2, 3, 4`` 是最大的，所以答案是4。

和1562题的做法一模一样。遇到一个数 `i` ，其实是标记了 `[i, i + 1)` 这个区间。这时候需要知道是否存在一个 `[l, i)` 区间、 `[i + 1, r)` 区间。如果存在， `[i, i + 1)` 区间可能可以和它们合并成 `[l, r)` 、 `[l, i + 1)` 、 `[i, r)` ，如果都不存在，那么只能保持不变。

如何快速知道是否存在 `[l, i)` 和 `[i + 1, r)` 呢？用hash map就行了。搞一个 ``leftRightMapping`` ，key是区间的左边界、value是区间的右边界，那么就能快速知道 `[i + 1, r)` 存不存在了；搞一个 ``rightLeftMapping`` ，key是区间的右边界、value是区间的左边界，就能快速知道 `[l, i)` 是否存在。
*/

struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut leftRightMapping: HashMap<i32, i32> = HashMap::new(); // leftRightMapping[left] = right表示之前见过一个[left, right)区间。这样可以O(1)快速定位到以某个数为左边界的区间
        let mut rightLeftMapping: HashMap<i32, i32> = HashMap::new(); // rightLeftMapping[right] = left表示之前见过一个[left, right)区间。这样可以O(1)快速定位到以某个数为右边界的区间
        let mut counter: HashMap<i32, usize> = HashMap::new(); // counter[length] = count表示长度为length的区间有count个
        let mut seen = HashSet::new(); // 去重

        for v in nums.into_iter() {
            if seen.contains(&v) {
                continue;
            }

            // 现在来了个一个数字v，如果v左右两边没有相邻的数字的话，它自己形成一个单独的区间[v, v + 1)
            let mut mergedLeft = v;
            let mut mergedRight = v + 1;

            if let Some(left) = rightLeftMapping.get(&v).cloned() {
                // 如果v左边有一个相邻的[l, v)区间的话，和它合并起来
                let right = v;
                mergedLeft = left; // 合并后的新区间是[l, v + 1)

                // 先把旧区间的记录全部删掉
                leftRightMapping.remove(&left);
                rightLeftMapping.remove(&right);

                match counter.get_mut(&left) {
                    Some(times) => {
                        if *times > 1 {
                            *times -= 1;
                        } else {
                            counter.remove(&left);
                        }
                    }
                    _ => {}
                }
            }

            if let Some(right) = leftRightMapping.get(&(v + 1)).cloned() {
                // 同理，如果v的右边有个相邻的区间[v + 1, r)，也可以和它合并起来
                let left = v + 1;
                mergedRight = right; // 合并后的新区间是[l, r)

                // 也要把旧区间的记录全部删掉
                leftRightMapping.remove(&left);
                rightLeftMapping.remove(&right);

                match counter.get_mut(&left) {
                    Some(times) => {
                        if *times > 1 {
                            *times -= 1;
                        } else {
                            counter.remove(&left);
                        }
                    }
                    _ => {}
                }
            }

            // 加入合并后的新区间的记录
            leftRightMapping.insert(mergedLeft, mergedRight);
            rightLeftMapping.insert(mergedRight, mergedLeft);
            *counter.entry(mergedRight - mergedLeft).or_insert(0) += 1;

            seen.insert(v);
        }

        return counter.into_iter().map(|(k, v)| k).max().unwrap_or(0);
    }
}

fn main() {
    dbg!(Solution::longest_consecutive(vec![100, 4, 200, 1, 3, 2])); // 4
    dbg!(Solution::longest_consecutive(vec![
        -7, -1, 3, -9, -4, 7, -3, 2, 4, 9, 4, -9, 8, -7, 5, -1, -7
    ])); // 4
}
