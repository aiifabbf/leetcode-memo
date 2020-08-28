/*
.. default-role:: math

一批货要按顺序依次送出，每天只能派一艘船出去，要在 `d` 天内运完，这艘货船的载重量最小必须是多少？

比如给 ``1, 2, 3, 4, 5, 6, 7, 8, 9, 10`` ，要在5天内运完，只需要一艘载重量是15的船就够了：

#.  第1天运 ``1, 2, 3, 4, 5``
#.  第2天运 ``6, 7``
#.  第3天运 ``8``
#.  第4天运 ``9``
#.  第5天运 ``10``

如果是14就不够

#.  第1天运 ``1, 2, 3, 4``
#.  第2天运 ``5, 6``
#.  第3天运 ``7``
#.  第4天运 ``8``
#.  第5天运 ``9``
#.  第6天运 ``10``

要6天。

如果是16，还是5天。

.. 为什么每天尽量塞满货船效率最高呢？有没有可能我今天少运一点，反而用的时间少呢？

用二分。因为问题的解满足单调性，如果测试发现货船的载重量是 `k` 的时候能在 `d` 天内运完，那么当货船的载重量是 `k + 1` 的时候，也必定能在 `d` 天内运完（说不定用的时间更少）。相当于是在找满足条件的最小的 `k` 。

有点278 first bad version的味道了。
*/

struct Solution;

impl Solution {
    pub fn ship_within_days(weights: Vec<i32>, d: i32) -> i32 {
        let mut left = weights.iter().max().cloned().unwrap_or(0); // 货船最小可能的载货量是最重的那个货物的重量，因为不能拆货物
        let mut right = weights.iter().sum(); // 最大可能载货量是所有货物重量总和，超过这个也没用

        while left < right {
            let middle = (left + right) / 2;
            if Self::feasible(middle, &weights[..], d) {
                // 如果可行
                right = middle; // 收紧右边界
            } else {
                // 如果不可行
                left = middle + 1; // 收紧左边界
            }
        }

        // 保险起见，最后出去的时候再测试一下可不可行
        if Self::feasible(left, &weights[..], d) {
            return left;
        } else {
            // 如果不可行，就再加一吨，一定可行了
            return left + 1;
        }
        // 虽然测试发现都是可行，但我也没法证明
        // 其实是没问题的，如果可行空间是[l, +oo)，你去找可行空间的左边界，是没问题的，如果可行空间是(-oo, r)，找可行空间的右边界，那就可能有问题
    }

    // 验证每艘船载重量是capacity的时候，能不能在n天内运完
    // 我不理解为什么每天尽量多装，就能在最短时间内运完。这里的greedy条件要证明
    fn feasible(capacity: i32, weights: &[i32], maxDayCount: i32) -> bool {
        let mut dayCount = 0;
        let mut loaded = 0; // 现在这艘货船上已经装了loaded吨东西

        for v in weights.iter() {
            if loaded + v > capacity {
                // 装不下了
                dayCount += 1; // 上一条船出发
                loaded = *v; // 新的一条船
            } else {
                // 装的下
                loaded += v;
            }
        }

        if loaded != 0 {
            // 还剩点东西
            dayCount += 1; // 最后一条船
        }

        return dayCount <= maxDayCount;
    }
}

fn main() {
    dbg!(Solution::ship_within_days(
        vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        5
    )); // 15
    dbg!(Solution::ship_within_days(vec![3, 2, 2, 4, 1, 4], 3)); // 6
    dbg!(Solution::ship_within_days(vec![1, 2, 3, 1, 1], 4)); // 3
}
