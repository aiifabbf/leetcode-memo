/*
.. default-role:: math

给一个全是0和1的array，最多有 `k` 次把0变成1的修改机会，这样能凑成的最长的全1 substring（要连续）的长度是多少？

比如给

::

    1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0

给2次修改机会，我们可以把

::

    1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0
                ^  ^

这两个0变成1

::

                v  v
    1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0
               |                 |

这样就能凑一个长度为6的全1 substring了。

还是考虑动态规划吧。设 ``dp[j]`` 是以第 `j - 1` 个元素结尾的、最多只含两个0的substring（好绕口啊）。

那怎么从 ``dp[j - 1]`` 到 ``dp[j]`` 呢？从 ``dp[j - 1]`` 到 ``dp[j]`` 多出了 ``array[j - 1]`` 这个元素，所以有两种情况

-   ``array[j - 1]`` 是1

    没问题，直接接在前面就可以了。

-   ``array[j - 1]`` 是0

    有点麻烦。暴力做法是从 `j` 往前看，找到一个 `i` ，使得 ``array[i..j]`` 里0的数量不超过k、同时 `j - i` 又要最大。

    所以这里可以用双指针来优化，用另一个指针 `i` 来标记substring的左边界。如果 ``array[i..j]`` 里面0的数量超过 `k` 了，就需要右移指针 `i` ，直到 ``array[i..j]`` 里面0的数量不超过 `k` 。

    如果 ``array[i..j]`` 里面0的数量不超过 `k` ，那无所谓，不用右移。

    但是你怎么知道 ``array[i..j]`` 里面有多少个0呢？这时候就需要另一个变量来存 ``array[i..j]`` 里面有多少个0。
*/

struct Solution;

impl Solution {
    pub fn longest_ones(a: Vec<i32>, k: i32) -> i32 {
        let array = a;
        let k = k as usize;

        let mut i = 0;
        let mut res = 0;
        let mut lastDp = 0; // 因为dp[j]只和dp[j - 1]有关，所以只要保留前一项就可以了，不用全部保留
        let mut replacementCount = 0; // array[i..j]里面0的数量

        for j in 1..array.len() + 1 {
            if array[j - 1] == 1 {
                lastDp += 1; // 直接接在前面就可以了
            } else {
                replacementCount += 1;

                while replacementCount > k {
                    // 如果0的数量大于k的话，要右移i，直到array[i..j]里面0的数量不超过k
                    if array[i] == 1 {
                        i += 1;
                    } else {
                        i += 1;
                        replacementCount -= 1; // 终于少一个0
                    }
                }
                // array[i..j]里面0的数量不超过k就可以停了

                lastDp = j - i;
            }
            res = res.max(lastDp);
        }

        return res as i32;
    }
}

fn main() {
    println!(
        "{:?}",
        Solution::longest_ones(vec![1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
    ); // 6
    println!(
        "{:?}",
        Solution::longest_ones(
            vec![0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
            3
        )
    ); // 10
    println!("{:?}", Solution::longest_ones(vec![], 3)); // 0
}
