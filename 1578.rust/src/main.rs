/*
.. default-role:: math

给个字符串，删掉一些字符，使得字符串里不存在连续相同的字符。删除位于 `i` 的字符的花费是 ``cost[i]`` ，问最小花费是多少。

比如给

::

    a b a a c
    1 2 3 4 5

必须删掉第2个或第3个 ``a`` 才能使得字符串里没有两个相邻的 ``a`` 。删掉第2个 ``a`` 只要花费3，而删掉第3个 ``a`` 要花费4，所以删掉第2个 ``a`` 更合算。

挺简单的，搞一个stack，存放将要保留的字符。然后遍历字符串里的每个字符，依次放入stack。放入之前看一下stack顶端的字符和现在要放入的字符是不是相等，如果不相等，那么放心大胆地放进去。

比如假设stack现在是 ``[a, b]`` ，现在要放入 ``a`` ，那么放心加进去就好了。

如果stack顶端的字符和现在要放入的字符相等，就有点麻烦，因为不允许两个相邻的字符相同，所以要判断保留stack顶端字符、还是保留现在要放入的字符。因为是要减少 **删除字符的花费** ，所以保留价格较高的那个字符。

比如现在有 ``2, 1, 3`` 三个数字，要删掉两个数字、并且花费最少，那么肯定是删掉 ``2, 1`` 、留下最大的 ``3`` 花费最少。
*/

struct Solution;

impl Solution {
    pub fn min_cost(s: String, cost: Vec<i32>) -> i32 {
        let mut stack = vec![]; // 保留哪些字符，存的是那些字符的下标、字符

        for (i, v) in s.chars().enumerate() {
            if let Some((j, w)) = stack.last().cloned() {
                // 如果stack不空，对比一下stack顶端的字符和当前要添加的字符是否相等
                if w != v {
                    // 如果和前面一个字符根本就不同
                    stack.push((i, v)); // 反正不冲突，放心地加进去
                } else {
                    // 如果和前面一个字符相同，就要动下脑筋了，就要想一想是保留前一个字符、还是保留这个字符
                    stack.pop();
                    if cost[j] < cost[i] {
                        stack.push((i, v)); // 保留价值大的字符
                    } else {
                        stack.push((j, w));
                    }
                }
            } else {
                // 如果stack空
                stack.push((i, v)); // 放心加
            }
        }

        return cost.iter().sum::<i32>() - stack.iter().map(|v| cost[v.0]).sum::<i32>();
        // 最后花费是删掉字符的花费，等于总花费减去留下的字符的价格
    }
}

fn main() {
    dbg!(Solution::min_cost("abaac".into(), vec![1, 2, 3, 4, 5])); // 3
    dbg!(Solution::min_cost("abc".into(), vec![1, 2, 3])); // 0
    dbg!(Solution::min_cost("aabaa".into(), vec![1, 2, 3, 4, 1])); // 2
}
