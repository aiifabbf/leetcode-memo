/*
.. default-role:: math

给个数列，每次操作可以随便选一个数字给它加1，最少多少次操作之后能使数列严格单调递增？

最近在学函数式，所以看到什么都想用递归来做……设 ``f(array, lower)`` 是使得array严格单调递增、同时array里面任意一个元素都大于等于lower所需要的最小操作次数。

首先想初始条件，当然是array是空的情况，那么 ``f([], _) = 0`` ，因为空数列本身就是严格单调递增的。

然后想递推式。一个数列如果想做到所有元素都大于等于lower、同时自己还是严格单调递增的充要条件是啥呢？

-   数列的第0个元素肯定要大于等于lower

    因为数列是严格单调递增的，所以如果第0个元素大于等于lower，那么因为第1个元素大于第0个元素，所以第1个元素肯定也是大于等于lower的，第2个元素大于等于第1个元素……

-   ``array[1..]`` 要严格单调递增，并且 ``array[1..]`` 里每个元素都要大于等于 ``max(array[0], lower) + 1``

那么为了做到这两件事情，最少需要多少次操作呢？

-   为了使得数列的第0个元素大于等于lower

    首先要看第0个元素是不是本身已经大于等于lower了，如果是的，那么啥也不用做。

    如果不是，那么需要花费的操作是 ``lower - array[0]`` 。比如假设现在lower是5，而 ``array[0] = 2`` ，那么2到5需要3次操作。

-   为了使得 ``array[1..]`` 严格单调递增，并且 ``array[1..]`` 里每个元素大于等于 ``max(array[0], lower) + 1``

    发现需要的操作次数竟然可以写成 ``f`` 自身: ``f(array[1..], max(array[0], lower) + 1)`` 。
*/

struct Solution;

impl Solution {
    #[cfg(feature = "recursive")]
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        // 使得array严格单调递增、同时array里任意一个元素大于等于lower所需的最少操作次数
        fn f(array: &[i32], lower: i32) -> i32 {
            if let Some(v) = array.first() {
                // 取array第一个元素
                let cost1 = if *v >= lower {
                    // 如果本身就已经大于等于lower了
                    0 // 啥也不用做
                } else {
                    // 如果小于lower
                    lower - *v // 要经过这么多次操作把自己提升到lower
                }; // 第一个条件的花费
                let cost2 = f(&array[1..], v.max(&lower) + 1); // 第二个条件的花费
                cost1 + cost2
            } else {
                // array是空的
                0
            }
        }

        f(&nums[..], std::i32::MIN) // 原问题只要单调递增，不需要大于等于lower，所以等于f(array, -oo)
    }

    // 这就和普通的for差不多，只不过用了fold
    #[cfg(feature = "fold")]
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        nums.into_iter()
            .fold((0, std::i32::MIN), |acc, v| {
                let (res, lower) = acc;
                if v >= lower {
                    (res, v + 1)
                } else {
                    (res + lower - v, lower + 1)
                }
            })
            .0
    }
}

fn main() {
    dbg!(Solution::min_operations(vec![1, 1, 1])); // 3
    dbg!(Solution::min_operations(vec![1, 5, 2, 4, 1])); // 14
}
