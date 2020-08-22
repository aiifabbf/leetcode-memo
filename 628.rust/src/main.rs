/*
.. default-role:: math

给个array，从中不重复挑出3个数字，问3个数字的乘积的最大值是多少。

数字有正有负，所以其实还挺麻烦的。评论区的做法都是先排序，然后挑最大的三个正数、或者挑最大的正数乘以两个最小的负数，但是这里面有各种问题，有可能根本没有负数，有可能根本没有正数。

所以想了个 `O(n)` 的DP做法。因为问的是3个数字，所以可以先固定最右边的那个数，再在这个固定好的数字的前面找两个数字，使得这三个数字的乘积最大。你可能会觉得最大乘积就是 ``array[i]`` 直接乘以 ``array[0..i]`` 里面挑两个数字的最大乘积，但是其实不是，如果 ``array[i]`` 是个负数的话，这样可能凑出的是最小乘积！比如

::

    -1, 2, 3, -4

比如到-4的时候，前面的最大两数乘积是 `2 \time 3 = 6` ，可是 `-4 \times 6 = -24` ，并不是最大的三数乘积，最大的应该是 `-4 \time -1 \time 3 = 12` ，反而是-4乘以 ``-1, 2, 3`` 里最小的两数乘积。

所以除了要知道 ``array[0..i]`` 里最大的两数乘积以外，还需要知道最小的两数乘积。

那么设 ``maxDp[i]`` 是 ``array[0..i]`` 里面最大的两数乘积， ``minDp[i]`` 是 ``array[0..i]`` 里面最小的两数乘积。 ``maxDp[i]`` 、 ``minDp[i]`` 分别和前面的项有什么关系呢？ ``array[i - 1]`` 有可能是凑成最大两数乘积的其中一个乘数，那么此时能凑出的最大两数乘积是

-   ``array[i - 1]`` 乘以 ``array[0..i - 1]`` 里面最小的数
-   或者 ``array[i - 1]`` 乘以 ``array[0..i - 1]`` 里面最大的数

当然 ``array[i - 1]`` 也有可能不是乘数之一，那么此时最大的乘积仍然是 ``array[0..i - 1]`` 能凑出的最大乘积，即 ``maxDp[i - 1]`` 。

所以递推式是 ``maxDp[i] = max(array[i - 1] * max, array[i - 1] * min, maxDp[i - 1])`` 。

同理 ``minDp[i] = min(array[i - 1] * min, array[i - 1] * max, minDp[i - 1])`` 。

最终的答案就是

.. math::

    \max\{a_i \times \text{maxDp}_i, a_i \times \text{minDp}_i\}

.. 面拼多多被问了这道题。
*/

struct Solution;

impl Solution {
    pub fn maximum_product(nums: Vec<i32>) -> i32 {
        if nums.len() < 3 {
            return 0;
        }

        let mut maxDp = vec![std::i32::MIN; nums.len() + 1]; // maxDp[i]是nums[0..i]里任意挑两个数字、能达成的最大乘积
        let mut minDp = vec![std::i32::MAX; nums.len() + 1]; // minDp[i]是nums[0..i]里任意挑两个数字、能达成的最小乘积

        maxDp[2] = nums[0] * nums[1]; // 初始条件，nums[0..2]里只有两个数字，所以当然能达成的最大乘积只能是这两个数字的乘积
        minDp[2] = nums[0] * nums[1]; // 同理
        let mut maximum = nums[0].max(nums[1]); // 目前见过的最大的数字
        let mut minimum = nums[0].min(nums[1]); // 目前见过的最小的数字

        for i in 3..nums.len() + 1 {
            maxDp[i] = (nums[i - 1] * maximum)
                .max(nums[i - 1] * minimum)
                .max(maxDp[i - 1]); // maxDp[i]要么是nums[i - 1]乘以前面见过的最大的数字、要么是nums[i - 1]乘以前面见过的最小的数字（因为有可能nums[i - 1]是负数，前面见过的最小的数字也是个很小的负数，这样它们乘起来可能很大）、要么比不过maxDp[i - 1]
            minDp[i] = (nums[i - 1] * maximum)
                .min(nums[i - 1] * minimum)
                .min(minDp[i - 1]); // 同理

            maximum = maximum.max(nums[i - 1]); // 更新一下目前见过的最大的数字
            minimum = minimum.min(nums[i - 1]);
        }

        let mut res = std::i32::MIN;

        for (i, v) in nums.iter().enumerate().skip(2) {
            res = res.max(v * maxDp[i]).max(v * minDp[i]);
        }

        return res;
    }
}

fn main() {
    dbg!(Solution::maximum_product(vec![1, 2, 3])); // 6
    dbg!(Solution::maximum_product(vec![1, 2, 3, 4])); // 24
    dbg!(Solution::maximum_product(vec![-5, -4, -3, -2, -1, 0])); // 0
    dbg!(Solution::maximum_product(vec![
        652, -516, -492, 108, 492, -20, -104, 904, -681, -505, -616, -732, 25, 132, -657, 40, 566,
        -779, -676, 566, 52, -799, 783, -639, -188, 707, 187, -879, 901, 803, 719, 577, 771, -642,
        911, 597, -670, 710, 30, -422, 310, 619, 874, 632, 126, -657, -694, 800, 81, 290, 163,
        -835, -810, -839, -151, 829, 942, -343, -984, 726, 764, -751, -189, -169, 386, -371, -105,
        -823, -594, -42, -627, 369, -198, -72, -889, -572, -904, 354, -546, -46, -422, 855, 980,
        815, 494, 169, 700, -440, -322, 820, 999, 904, 887, -295, -633, -252, -979, -375, -837,
        590
    ])); // 962372664
}
