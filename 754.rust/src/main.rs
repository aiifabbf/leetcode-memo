/*
.. default-role:: math

一开始在0，第1步可以选择往左或者往右走1步，第2步可以选择往左或者往右走2步……问最少需要几步才能走到 `n` 这个数

比如需要走到3，那么可以

1.  往右走一步，0到1
2.  往右走两步，1到3

比如需要走到2，可以

1.  往右走一步，0到1
2.  往左走两步，1到-1
3.  往右走三步，-1到2

所以最暴力的做法就是把 `n` 步之后能到达的所有数字都存在hash set里，然后看目标数字在不在hash set里，如果不在，就往前走一步看看在不在。

`n` 步之后会产生多少个数字呢？不仔细想会觉得是 `O(2^n)` 。但是找一下规律就会发现其实是 `O(n^2)` 。

1.  第一步之后，产生 ``-1, 1``
2.  第二步之后，产生 ``-3, -1, 1, 3``
3.  第三步之后，产生 ``-6, -4, -2, 0, 2, 4, 6``
4.  第四步之后，产生 ``-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10``
5.  第五步之后，产生 ``-15, -13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15``

发现第 `n` 步之后，产生的数字只有 `- {n (n + 1) \over 2}` 到 `{n (n + 1) \over 2}` 之间的那么多数字，而且非常有规律，以2为间隔。

所以原理就很简单了，找到一个最小的步数 `n` ，使得

.. math::

    t \in \{-{n (n + 1) \over 2}, -{n (n + 1) \over 2} + 2, -{n (n + 1) \over 2} + 4, ..., {n (n + 1) \over 2} - 2, {n (n + 1) \over 2}\}

注意一个坑，不能简单认为是找到一个最小的 `n` 使得 `{n (n + 1) \over 2} \geq |t|` 就完事了，不一定的。 `{n (n + 1) \over 2} \geq |t|` 只能保证 `|t|` 集合的最小数到最大数的范围内，不能保证 `|t|` 一定在集合里。因为集合里面要么全是偶数、要么全是奇数，如果 `|t|` 和 `{n (n + 1) \over 2}` 奇偶性不同， `t` 是不会在集合里面的。举个反例，问最少需要多少步到7，满足 `{n (n + 1) \over 2} \geq 7` 的最小的 `n` 是4，四步之后产生的范围是 `[-10, 10]` ，产生的数字是 ``-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10`` ，然而这些数字里没有7。

所以找到那个最小的 `n` 之后，还要看一看集合里面到底有没有target，即看一看 `{n (n + 1) \over 2}` 和target的奇偶是否一致，如果不一致，要给 `n` 加1，直到奇偶一致。

那怎么找到最小的 `n` 使得 `{n (n + 1) \over 2} \geq |t|` 呢？可以直接 `n` 从1开始往上找，这样复杂度是 `O(\sqrt(t))` ，也可以二分，复杂度是 `O(\ln t)` 。
*/

struct Solution;

impl Solution {
    // 一开始想的naive做法
    // pub fn reach_number(target: i32) -> i32 {
    //     if target == 1 || target == -1 {
    //         return 1;
    //     }

    //     let mut i = 2;
    //     let mut seen = HashSet::new();
    //     seen.insert(1);
    //     seen.insert(-1);
    //     let target = target as i64;

    //     while true {
    //         let mut newSet = HashSet::new();

    //         for v in seen.iter() {
    //             newSet.insert(v + i);
    //             newSet.insert(v - i);
    //         }

    //         seen = newSet;

    //         if seen.contains(&target) {
    //             return i as i32;
    //         } else {
    //             i += 1;
    //         }
    //     }

    //     return i as i32;
    // }

    pub fn reach_number(target: i32) -> i32 {
        // 首先找到一个最小的n使得n (n + 1) / 2 >= abs(target)
        // 这里用了二分，非常快，即使是10^9，也只要30步左右就能找到
        let target = target.abs() as i64;
        let mut left = 0 as i64;
        let mut right = target as i64;

        while left < right {
            let middle = left + (right - left) / 2;
            if middle * (middle + 1) / 2 < target {
                left = middle + 1;
            } else if middle * (middle + 1) / 2 > target {
                right = middle;
            } else {
                // 因为是要找到最小的，所以相等的时候，应该收紧右边界
                right = middle;
            }
        }

        // 然而target可能并不在[-n (n + 1) / 2, n (n + 1) / 2]范围内，有可能target是奇数，然而n (n + 1) / 2却是偶数
        // 所以其实本质上是找到一个最小的n使得n (n + 1) / 2 >= abs(target)同时n (n + 1) / 2和abs(target)奇偶性相同
        while (left * (left + 1) / 2) % 2 != target % 2 {
            // 不断加1，直到n (n + 1) / 2和abs(target)奇偶性相同，这样才能保证abs(target)确实在[-n (n + 1) / 2, n (n + 1) / 2]、间隔为2的区间里
            left += 1;
        }

        return left as i32;
    }
}

fn main() {
    dbg!(Solution::reach_number(3)); // 2
    dbg!(Solution::reach_number(2)); // 3
    dbg!(Solution::reach_number(5)); // 5
    dbg!(Solution::reach_number(50)); // 11
    dbg!(Solution::reach_number(-1000000000)); // 44723
}
