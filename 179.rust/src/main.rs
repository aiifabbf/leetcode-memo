/*
.. default-role:: math

给一些数字，能凑成的最大十进制数字是多少？

比如给 ``3, 30, 34, 5, 9`` ，能凑出的最大数字是9534330。

隐隐感觉是和排序有关，要给数字定义一种ordering。在上面的例子里

.. math::

    9 < 5 < 34 < 3 < 30

几个观察（heuristic？）

-   暂时不管0，不管怎么排，最后产生的数字位数都相等
-   肯定是希望首位数字越大的放在最前面，比如 ``9, 5`` ，肯定是9排在5的前面
-   如果首位相同，情况就有点复杂了，同样是一位数对两位数，凭什么34就排在3的前面，可是30却排在3的后面呢？

最后一个观察比较难，想不通就算了，不如不要想了，直接两种都试试不就好了？比如给了 ``3, 34`` ，那么就试试334大还是343大，选最大的那种排序不就搞定了吗？

这里有 `证明 <https://leetcode.com/problems/largest-number/discuss/291988/A-Proof-of-the-Concatenation-Comparator's-Transtivity>`_ ordering是存在的。
*/

struct Solution;

use std::cmp::Ordering;

impl Solution {
    pub fn largest_number(nums: Vec<i32>) -> String {
        let mut res: Vec<String> = nums.into_iter().map(|v| v.to_string()).collect();
        res.sort_by(|v, w| {
            // 传进来3和34
            if format!("{}{}", v, w) < format!("{}{}", w, v) {
                // 试试334大还是343大。注意这里不用把string转换成数字再去比较，直接比较string就可以，为啥呢？因为对于长度相等的两个string，字典序就是数字序
                return Ordering::Greater; // v > w，所以最后会变成wv
            } else {
                return Ordering::Less;
            }
        });
        // 最后处理一下恶心的前缀0
        return match res.join("").trim_start_matches("0") {
            "" => "0",
            v => v,
        }
        .to_string();
    }
}

fn main() {
    dbg!(Solution::largest_number(vec![10, 2])); // 210
    dbg!(Solution::largest_number(vec![3, 30, 34, 5, 9])); // 9534330
    dbg!(Solution::largest_number(vec![1])); // 1
    dbg!(Solution::largest_number(vec![10])); // 10
    dbg!(Solution::largest_number(vec![0, 0])); // 0
}
