/*
.. default-role:: math

给个array，当青蛙在第 `i` 个格子的时候，他有三种跳法

-   跳到 `i + 1`
-   跳到 `i - 1`
-   跳到随便一个 `j` ，前提是 ``array[i] == array[j]``

青蛙任何时候都不能跳出数组。问最少跳多少跳能从第0个格子跳到最后一个格子。

看到这种array里跳来跳去的我就想到BFS……但是题目标了个hard，怪吓人的，估计会在什么地方阴你一下。

跳到 `i + 1` 和 `i - 1` 都没啥问题，用个hash set记录已经遍历过的下标就可以避免重复遍历。

Hard的地方在于第三种情况。当我们当前在下标 `i` 的时候，肯定希望快速知道有哪些 `j` 满足 ``array[i] == array[j]`` 这样我们下一跳可以跳过去。这很好办，先扫描一遍array，建立一个hash map，key是值，假设是v，value是个hash set，存满足 ``array[i] == v`` 的所有的 `i` 。比如假设 ``map[12] == {0, 3, 4}`` ，说明array里只有0、3、4这几个格子的值是12。这样当我们在下标0的时候，马上就知道下一跳可以跳到3或者4去。这是第一个可优化的地方，不算最关键的地方。

设想一种极端情况，array是10000个7，这样 ``map == {7: {0, 1, 2, ..., 9999}}`` 。问题来了，在每个格子里，都要遍历一遍 ``7: {0, 1, 2, ..., 9999}`` 这个entry，直接把复杂度拉满到了 `O(n^2)` 。

1.  在下标0的时候，遍历一遍，把1、2、……、9999全部放到了队列里
2.  在下标1的时候，又遍历了一遍，但啥也没有放到队列里，因为发现已经在队列里了
3.  在下标2的时候，又遍历了一遍，但啥也没有放到队列里，因为发现已经在队列里了
4.  ...

所以第一次遍历完 ``7: {0, 1, 2, ..., 9999}`` 这个entry之后，不如就直接把这个entry删了，因为所有能跳的目标都在队列里了，这个entry以后再也不会被读到了。
*/

struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn min_jumps(arr: Vec<i32>) -> i32 {
        let array = arr;
        let mut jumps: HashMap<i32, HashSet<usize>> = HashMap::new(); // key是v，value是所有满足array[i] == v的i。比如，jumps[12] == {0, 3, 4}说明array[0] == array[3] == array[4] == 12

        for (i, v) in array.iter().cloned().enumerate() {
            match jumps.get_mut(&v) {
                Some(indices) => {
                    indices.insert(i);
                }
                None => {
                    jumps.insert(v, [i].iter().cloned().collect());
                }
            }
        }

        let mut queue = HashSet::new(); // 然后开始BFS
        queue.insert(0); // 一开始在下标为0的格子里
        let mut traveled: HashSet<usize> = HashSet::new(); // 避免重复跳。第一次跳到某个格子的时候，此时的跳数一定是跳到这个格子所需的最小跳数
        let mut depth = 0; // 跳了多少跳

        while !queue.is_empty() {
            let mut level_queue = HashSet::new(); // 下一跳的目标

            for node in queue.iter().cloned() {
                if node == array.len() - 1 {
                    // 如果已经跳到最后一个格子了
                    return depth; // 这一定是第一次跳到最后一个格子，否则上一轮一定已经return了。而根据分析，第一次跳到某个格子经历的跳数，一定是跳到这个格子所需的最小的跳数，不可能存在跳数更少的情况
                }

                let target = node + 1; // 第一种情况是跳到i + 1
                if target < array.len() {
                    // 注意不能跳出数组
                    if !traveled.contains(&target)
                        && !level_queue.contains(&target)
                        && !queue.contains(&target)
                    {
                        // 如果之前跳过、或者已经在下一跳的目标里了、或者即将遍历，那么忽略
                        level_queue.insert(target);
                    }
                }

                // 第二种情况是跳到i - 1
                if let Some(target) = node.checked_sub(1) {
                    // 如果当前在0_usize，0_usize - 1会panic
                    if !traveled.contains(&target)
                        && !level_queue.contains(&target)
                        && !queue.contains(&target)
                    {
                        level_queue.insert(target);
                    }
                }

                // 第三种情况是跳到任意满足array[i] == array[j]的j
                if let Some(targets) = jumps.get(&array[node]) {
                    for target in targets.iter().cloned() {
                        if !traveled.contains(&target)
                            && !level_queue.contains(&target)
                            && !queue.contains(&target)
                            && target != node
                        {
                            // 如果之前已经跳过、或者已经在下一跳的目标里、或者即将遍历、或者等于自身，就忽略
                            level_queue.insert(target);
                        }
                    }
                }

                traveled.insert(node);
                jumps.remove(&array[node]); // 这是这道题之所以为hard的原因……设想假如array == [7, 7, 7, ..., 7]一万个7，那么在最开始在下标0的时候，会把9999个格子全部加到level_queue里，可是在下一步跳到下标1的时候，又会在上面的代码里扫描一遍10000个格子（虽然不会真的加入level_queue）。每个格子都扫描一遍10000，复杂度就变成了O(n^2)了。所以反正所有值是7的格子都加到level_queue里面了，在下一轮都会遍历一遍，就没必要再保留7: {0, 1, 2, ..., 9999}这个记录了
            }

            queue = level_queue;
            depth += 1;
        }

        unreachable!(); // 不管怎样都一定能跳到最后一格，最坏最坏每次都跳到i + 1，也能到最后一格，所以绝对不会跑到这里
    }
}

fn main() {
    dbg!(Solution::min_jumps(vec![
        100, -23, -23, 404, 100, 23, 23, 23, 3, 404
    ])); // 3
    dbg!(Solution::min_jumps(vec![7])); // 0
    dbg!(Solution::min_jumps(vec![7, 6, 9, 6, 9, 6, 9, 7])); // 1
    dbg!(Solution::min_jumps(vec![6, 1, 9])); // 2
    dbg!(Solution::min_jumps(vec![
        11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13
    ])); // 3
    dbg!(Solution::min_jumps({
        let mut array = vec![7; 10000];
        array.extend(vec![11]);
        array
    })); // 2
}
