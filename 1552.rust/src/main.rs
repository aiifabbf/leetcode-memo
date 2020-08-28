/*
.. default-role:: math

数轴上有一些桶，你手里有 `m` 个球，要把球全部放到桶里，每个桶里只能放一个球，任意两个球之间的距离的最小值最大是多少？

暴力做法肯定是从1开始试。先试试距离为1的时候行不行，行的话试试2，还是可以的话再试试3……眼力好的话马上发现，如果发现距离为 `k` 的时候可以，那么距离 `k - 1` 的时候一定也可以。

所以又是二分，找到最大的满足条件的 `k` 。
*/

struct Solution;

impl Solution {
    pub fn max_distance(position: Vec<i32>, m: i32) -> i32 {
        let mut positions = position;
        positions.sort();
        let count = m as usize;

        if positions.len() == 0 || count == 0 || count == 1 || positions.len() < m as usize {
            // 这几种情况应该是未定义吧
            return 0;
        }

        let mut left = 1; // 最小距离是1，这绝对是可行的，找前m个桶放下所有的球
        let mut right = (positions.last().cloned().unwrap() - positions.first().cloned().unwrap())
            / (count as i32 - 1); // 最大距离是完全平均放置，第一个桶和最后一个桶的距离内均匀放下m个球，不一定可行

        // 然后二分，找到满足条件的
        while left < right {
            let middle = (left + right) / 2;
            if Self::feasible(&positions[..], middle, count) {
                // 如果可行，试试距离能不能更大一点
                left = middle + 1; // 收紧左边界
            } else {
                // 如果不可行，试试距离更小一点
                right = middle; // 收紧右边界
            }
        }

        // 这里我也不确定
        if Self::feasible(&positions[..], left, count) {
            // 如果left可行
            return left; // 那就left
        } else {
            // 如果不可行
            return left - 1; // 那就-1
        }
    }

    // 试一下最少每隔gap米放一个球能不能放完
    // 我还是和1011运货一样的问题，为什么尽可能早放球，最终就能尽快放完手里的球呢
    fn feasible(positions: &[i32], gap: i32, count: usize) -> bool {
        if count == 0 {
            // 根本就没有球需要放
            return true;
        } else {
            // 有球
            if positions.len() == 0 {
                // 但没有桶
                return false; // 放不了
            } else {
                // 有球也有桶

                // 初始条件，第一个球放在第一个桶里
                let mut last = positions.first().unwrap(); // 上一个球放的位置
                let mut count = count - 1; // 还要放多少个球

                for v in positions.iter().skip(1) {
                    if v - last >= gap {
                        // 如果这个桶离前一个桶的距离大于等于最小距离
                        count -= 1; // 那么这个球就放在这个桶里
                        last = v;
                    }
                    // 如果小于最小距离，继续往后看

                    if count == 0 {
                        // 放完这个球之后，手里没球了，全部放完了
                        return true; // 可行
                    }
                }

                if count == 0 {
                    return true;
                } else {
                    // 遍历完所有的桶，结果手里还是剩球
                    return false; // 说明不可行
                }
            }
        }
    }
}

fn main() {
    dbg!(Solution::max_distance(vec![1, 2, 3, 4, 7], 3)); // 3
    dbg!(Solution::max_distance(
        vec![5, 4, 3, 2, 1, 1_000_000_000],
        2
    )); // 999_999_999
}
