/*
给 `n` 门课，课程之间有依赖关系，按怎样的顺序学习才能满足依赖关系

典型拓扑排序。这里有一篇很好的文章 <https://www.cnblogs.com/bigsai/p/11489260.html> 。和BFS的实现方法差不多，都是用queue。

详细题解见python版。
*/

struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::VecDeque;

impl Solution {
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let mut outs: HashMap<i32, HashSet<i32>> = HashMap::new();
        let mut ins: HashMap<i32, HashSet<i32>> = HashMap::new();

        for i in 0..num_courses {
            outs.insert(i, HashSet::new());
            ins.insert(i, HashSet::new());
        }

        for edge in prerequisites.iter() {
            let b = edge[0];
            let a = edge[1];

            if let Some(targets) = outs.get_mut(&a) {
                // unwrap()可能会panic，所以尽量少用吧
                targets.insert(b);
            }
            if let Some(origins) = ins.get_mut(&b) {
                origins.insert(a);
            }
        }

        let mut queue: VecDeque<i32> = ins
            .iter()
            .filter(|(k, v)| v.is_empty())
            .map(|(k, v)| k)
            .cloned()
            .collect(); // 筛选出所有不依赖其他课程的课
        let mut res = vec![];

        while let Some(node) = queue.pop_front() {
            // 不停地从queue的最前面取出课，假设叫课程node，比如线性代数
            if let Some(targets) = outs.get(&node) {
                // targets是所有依赖课程node的其他课，这里面可能就包括图形学、矩阵论等等
                for neighbor in targets.iter() {
                    if let Some(origins) = ins.get_mut(&neighbor) {
                        origins.remove(&node); // 把图形学对线性代数的依赖删掉
                        if origins.is_empty() {
                            // 发现图形学不依赖任何课了
                            queue.push_back(*neighbor); // 之后就可以选图形学了
                        }
                    }
                }
            }

            res.push(node); // 上这门课
            outs.remove(&node); // 把线性代数这门课从图里删掉
            ins.remove(&node); // 把线性代数这门课从图里删掉
        }

        // 看下是否能上完所有的课
        if res.len() != num_courses as usize {
            return vec![];
        } else {
            return res;
        }
    }
}

fn main() {
    dbg!(Solution::find_order(2, vec![vec![1, 0]])); // [0, 1]
    dbg!(Solution::find_order(
        4,
        vec![vec![1, 0], vec![2, 0], vec![3, 1], vec![3, 2],]
    )); // [0, 1, 2, 3]
}
