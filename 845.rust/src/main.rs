/*
.. default-role:: math

给个array，找到这样一个substring，它长度大于等于3，并且是“山形”的，前半段单调严格递增、后半段严格单调递减。最长的这样的substring长度是多少？

比如给 ``2, 1, 4, 7, 3, 2, 5`` 就能发现

::

    2, 1, 4, 7, 3, 2, 5
     |--------------|
     |-----------|
        |-----------|
        |--------|

这4个substring都是山形的，但是 ``1, 4, 7, 3, 2`` 是最长的。

按传统DP的点到为止……这题算不上DP。因为是substring，所以非常自然，求出以每个 ``a[j]`` 结尾的最长山形substring的长度

-   求出以 ``a[0]`` 结尾的最长山形substring的长度（如果不存在就是0）
-   求出以 ``a[1]`` 结尾的最长山形substring的长度
-   求出以 ``a[2]`` 结尾的最长山形substring的长度
-   ...
-   求出以 ``a[n - 1]`` 结尾的最长山形substring的长度

能包括一切可能的情况，然后再从这里面取最大就好了。还是以上面的例子为例

::

    2, 1, 4, 7, 3, 2, 5
     |                  以2结尾的长度是0
        |               以1结尾的长度是0
           |            以4结尾的长度是0
              |         以7结尾的长度是0
     |-----------|      以3结尾的长度是4
     |--------------|   以2结尾的长度是5
                       |以5结尾的长度是0

怎么求出以 ``a[j]`` 结尾的最长山形substring的长度呢？非常简单，从 ``a[j]`` 往前看，先找到那个顶峰，然后再从顶峰往前看，一路往下找到山谷。

比如假设现在在 ``2`` 的位置，以 ``2`` 结尾的最长严格单调递减substring是 ``7, 3, 2`` 。再从顶峰 ``7`` 的位置往前看，以 ``7`` 结尾的最长严格单调递增substring是 ``1, 4, 7`` 。所以以 ``2`` 结尾的最长山形substring是 ``1, 4, 7, 3, 2`` 。

::

    0 1  2  3  4  5  6  7
     2, 1, 4, 7, 3, 2, 5
            |vvvvvvvv|  <- decreasing[6]
      |^^^^^^^^|        <- increasing[4]
            ^---- 6 - decreasing[6]

这图就挺明显了。

这样我们就知道了每个以 ``a[j]`` 结尾的最长山形substring的长度了，整个array最长的substring就是这些substring里最长的那个。
*/

struct Solution;

impl Solution {
    pub fn longest_mountain(a: Vec<i32>) -> i32 {
        if a.len() < 3 {
            return 0;
        } else {
            let mut increasing = vec![1; a.len() + 1]; // 右边界正好是j、以a[j - 1]为最后一个元素的最长严格单调递增substring（要连续）的长度是多少
            increasing[0] = 0;
            increasing[1] = 1;

            for j in 2..a.len() + 1 {
                if a[j - 2] < a[j - 1] {
                    // 如果a[j - 1]比a[j - 2]大，那么a[j - 1]可以接在以a[j - 2]结尾的最长严格单调递增substring后面
                    increasing[j] = increasing[j - 1] + 1;
                } else {
                    increasing[j] = 1;
                }
            }

            let mut decreasing = vec![1; a.len() + 1]; // 右边界正好是j、以a[j - 1]为最后一个元素的最长严格单调递减substring（要连续）的长度是多少
            decreasing[0] = 0;
            decreasing[1] = 1;

            for j in 2..a.len() + 1 {
                if a[j - 2] > a[j - 1] {
                    // 如果a[j - 1]比a[j - 2]小，那么a[j - 1]可以接在a[j - 2]结尾的最长严格单调递减substring后面
                    decreasing[j] = decreasing[j - 1] + 1;
                } else {
                    decreasing[j] = 1;
                }
            }

            return (3..a.len() + 1) // 右边界正好是j的最长山形substring的长度是多少呢
                .map(|j| {
                    if decreasing[j] >= 2 && increasing[j - decreasing[j] + 1] >= 2 {
                        // j - decreasing[j]是顶峰的下标
                        decreasing[j] + increasing[j - decreasing[j] + 1] - 1 // 右边界正好是j的最长山形substring的长度
                    } else {
                        0
                    }
                })
                .max()
                .unwrap_or(0) as i32;
        }
    }
}

fn main() {
    dbg!(Solution::longest_mountain(vec![2, 1, 4, 7, 3, 2, 5])); // 5
    dbg!(Solution::longest_mountain(vec![2, 2, 2])); // 0
    dbg!(Solution::longest_mountain(vec![
        9, 8, 7, 6, 5, 4, 3, 2, 1, 0
    ])); // 0
    dbg!(Solution::longest_mountain(vec![
        0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0
    ])); // 11
}
