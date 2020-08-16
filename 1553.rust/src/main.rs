/*
.. default-role:: math

一开始有 `n` 个橘子，每天你都可以

-   要么只吃1个橘子
-   要么如果橘子数量是偶数，可以吃掉一半
-   要么如果橘子数量是3的倍数，可以吃掉 `2 / 3`

问最少几天能吃完。

非常容易写出递推式，设 `f(n)` 是 `n` 个橘子最少几天吃完，那么

.. math::

    f(n) = \begin{cases}
        \min\{1 + f(n - 1)\}, & n \mod 2 = 1, n \mod 3 = 1 \\
        \min\{1 + f(n - 1), 1 + f(n / 2)\}, & n \mod 2 = 0, n \mod 3 = 1 \\
        \min\{1 + f(n - 1), 1 + f(n / 3)\}, & n \mod 2 = 1, n \mod 3 = 0 \\
        \min\{1 + f(n - 1), 1 + f(n / 3), 1 + f(n / 2)\}, & n \mod 2 = 0, n \mod 3 = 0
    \end{cases}

初始条件是

.. math::

    f(0) = 0

直接用递推式会导致和斐波那契相同的问题，重复计算的问题，每个 `f(i)` 可能都被重复计算了很多次。

所以一个很自然的想法是用DP，把 `f(i), i \in [0, n]` 全算出来。到这里可以秒杀绝大部分 `n` 的规模是 `10^6` 级别的题目了。然而不能秒杀这道题，因为这题的 `n` 最大可能是 `2 \times 10^9` 。即使让 `f(i)` 的类型是u8，也要2 GB内存，可能会爆内存。时间上也会有问题，CPU时钟周期大概是1 ns，所以 `2 \times 10^9` 可能要花秒级别的时间。

终极大杀器登场！隆重介绍决策树BFS。假如第0天有 `n` 个橘子，并且 `n` 既是2的倍数、又是3的倍数，那么第1天的时候橘子的数量有三种情况。如果 `n` 只是2的倍数、或者只是3的倍数，那么只有两种情况。如果 `n` 既不是2的倍数，也不是3的倍数，那么就只有一种情况。所以根据每一天剩下的橘子，我们可以推算下一天可能剩下的橘子数量。

举个例子，假设最开始有6个橘子，那么决策树是这样的

::

            6
          / | \
        3   2   5
       /|   |   |
      1 2   1   4
      | |   |   | \
      0 1   0   2  3
        |       |  |\
        0       1  1 2
                |  | |
                0  0 1
                     |
                     0

我们的目标是找到6到0的最近距离。可以把值相同的节点合并起来，这样就得到了一张非常复杂的有向图。然后从6开始BFS一圈一圈向外扩展，直到遇到0为止。

总结一下心路历程，最开始的递归其实有两个问题

-   重复计算
-   含有min，有分支，不能确定走哪个分支，只能每个分支都一条路都走到黑

重复计算用DP可以解决，但是第二个分支的问题DP没法解决，因为 ``dp`` 数组里其实有大量数据是根本用不上的。如果能及早知道走这条分支没有希望，就不应该走下去了。这正是BFS的优势，它可以试探每个分支，到达终点就直接停止，不必像递归一样每条路都要走到底。有点像google搜索的工作原理：按下搜索的时候，其实请求被发给了很多很多个服务器，看谁最快出结果，一旦出了结果，其他服务器就不会再跑这个请求了。

顺便这个序列在OEIS上有 `记录 <https://oeis.org/A056796>`_ ，但是没什么信息。
*/

struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn min_days(n: i32) -> i32 {
        let n = n as usize;
        let mut queue = HashSet::new();
        queue.insert(n);
        let mut traveled = HashSet::new(); // 因为以前一直都是做树的BFS，所以从来不加这个set来记录已经遍历过的元素，其实这个set在BFS和DFS里应该是默认要加的，只有在绝对确定无环的图里才可以省略
        let mut depth = 0;

        while !queue.is_empty() {
            // 此时depth表示当前在第几层
            let mut levelQueue = HashSet::new();

            for node in queue.iter().cloned() {
                if node == 0 {
                    // 终于遇到0了
                    return depth;
                }

                if node % 3 == 0 {
                    if !traveled.contains(&(node / 3)) && !levelQueue.contains(&(node / 3)) {
                        // 已经遍历过的不用再次遍历
                        levelQueue.insert(node / 3);
                    }
                }
                if node % 2 == 0 {
                    if !traveled.contains(&(node / 2)) && !levelQueue.contains(&(node / 2)) {
                        // 同理
                        levelQueue.insert(node / 2);
                    }
                }
                if !traveled.contains(&(node - 1)) && !levelQueue.contains(&(node - 1)) {
                    levelQueue.insert(node - 1);
                }

                traveled.insert(node);
            }

            queue = levelQueue;
            // println!("{:?}", queue.len()); // queue并不会指数级增长，因为会遇到大量重复节点
            depth += 1;
        }

        return depth;
    }
}

fn main() {
    dbg!(Solution::min_days(10)); // 4
    dbg!(Solution::min_days(6)); // 3
    dbg!(Solution::min_days(56)); // 6
    dbg!(Solution::min_days(2 * 1000_000_000)); // 32
}
