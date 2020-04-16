/*
.. default-role:: math

给一个array里面都是数字， ``array[i]`` 表示这个位置有多少个石块，现在下雨了，问这个array表示的这堆石头可以盛多少格水。

比如给

::

    0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1

表示这堆石头大概是这样的

::
           o
       o   oo o
     o oo oooooo
    ------------
    012345678901

如果盛满雨水应该是这样的

::
           o
       oxxxooxo
     oxooxoooooo
    ------------
    012345678901

可以盛6个 ``x`` 所以是6格雨水。题目描述里的那张图更明显。

时隔一年半我终于把这道题做出来了……看了 <https://zhuanlan.zhihu.com/p/107792266> 这篇之后马上就知道怎么写了。

很简单，从局部入手，第 `i` 堆石头能盛多少水取决于什么？想象一下你就是水，你怎么保证自己不流出去？肯定是你的左右两边有足够高的石头挡住你啦。
*/

struct Solution;

use std::cmp::min;

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let maximumBefore: Vec<i32> = vec![0]
            .iter()
            .chain(height.iter())
            .scan(0, |state, v| {
                if v > state {
                    *state = *v;
                }
                return Some(*state);
            })
            .collect(); // maximumBefore[i]的意思是height[..i]的最大值

        let mut maximumAfter: Vec<i32> = vec![0]
            .iter()
            .chain(height.iter().rev())
            .scan(0, |state, v| {
                if v > state {
                    *state = *v;
                }
                return Some(*state);
            })
            .collect();

        maximumAfter.reverse(); // maximumAfter[i]的意思是height[i..]的最大值

        let mut res = 0;

        for (i, v) in height.into_iter().enumerate() {
            let left = maximumBefore[i]; // 从这里往左边看，看到的最高的石头是多高呢
            let right = maximumAfter[i + 1]; // 从这里往右边看，看到的最高的石头是多高呢
            let sideHeight = min(left, right); // 因为有短板效应，所以这里能盛的水不可能超过两边矮的那块石头

            if sideHeight > v {
                res += sideHeight - v;
            } // 当然如果本身就比两边高的话，根本不可能盛的了水
        }

        return res;
    }
}

pub fn main() {
    println!(
        "{:?}",
        Solution::trap(vec![0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    ); // 6
}
