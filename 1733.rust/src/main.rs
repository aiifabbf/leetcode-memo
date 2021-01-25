/*
.. default-role:: math

世界上有 `n` 种语言，分别是 `1, 2, ..., n` 。 ``languages[i]`` 是第 `i` 个用户会说的语言， ``friendship[k] = (i, j)`` 说明用户 `i, j` 是朋友，需要互相交流，他们必须要有至少一门共同语言才能交流。学校只能教授一种语言，问最少需要教多少个用户这门语言，每个用户才能和他的朋友愉快交流呢？

直接暴力，对于每一门语言 `l` ，对于每一对朋友 `i, j` ，如果 `i, j` 有至少一门共同语言，那么他们两个能互相交流，无需学习语言 `l` ；如果他们没有共同语言，那么需要学习语言 `l` 。所以对于每个语言 `l` ，统计出需要教多少个用户，取最小值就好了。

一定要注意

-   学校只能教一门语言
-   如果两个朋友之间有共同语言，他们不需要学学校教的那门语言
*/

struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn minimum_teachings(n: i32, languages: Vec<Vec<i32>>, friendships: Vec<Vec<i32>>) -> i32 {
        let languages: Vec<HashSet<i32>> = languages
            .into_iter()
            .map(|v| v.into_iter().collect())
            .collect(); // 把Vec转换成Set，快速判断用户a会不会说语言l

        (1..=n) // 假如教语言l
            .map(|language| {
                let mut targets = HashSet::new(); // 需要教哪些用户语言l。因为每个用户只要教一次，为了避免重复，所以这里用Set
                friendships.iter().for_each(|v| {
                    let a = v[0] as usize - 1;
                    let b = v[1] as usize - 1;
                    if languages[a].intersection(&languages[b]).next().is_none() {
                        // 如果两个用户没有共同语言，他们便没法交流
                        if !languages[a].contains(&language) {
                            // 如果用户a不会说语言l
                            targets.insert(a); // 教他
                        } // 如果用户a已经会说语言l了，就没必要教他了
                        if !languages[b].contains(&language) {
                            // 如果用户b不会说语言l
                            targets.insert(b); // 教他
                        }
                    } // 如果两个用户有共同语言，他们可以用共同语言交流，就没有必要强行给他们教语言l了。这是这题最坑的地方，而且给的例子里不能表明这种情况的存在
                });
                targets.len() // 如果教语言l，需要教多少个用户语言l
            })
            .min()
            .unwrap_or(0) as i32
    }
}

fn main() {
    dbg!(Solution::minimum_teachings(
        2,
        vec![vec![1], vec![2], vec![1, 2],],
        vec![vec![1, 2], vec![1, 3], vec![2, 3],]
    )); // 1
    dbg!(Solution::minimum_teachings(
        3,
        vec![vec![2], vec![1, 3], vec![1, 2], vec![3],],
        vec![vec![1, 4], vec![1, 2], vec![3, 4], vec![2, 3],]
    )); // 2
    dbg!(Solution::minimum_teachings(
        11,
        vec![
            vec![3, 11, 5, 10, 1, 4, 9, 7, 2, 8, 6],
            vec![5, 10, 6, 4, 8, 7],
            vec![6, 11, 7, 9],
            vec![11, 10, 4],
            vec![6, 2, 8, 4, 3],
            vec![9, 2, 8, 4, 6, 1, 5, 7, 3, 10],
            vec![7, 5, 11, 1, 3, 4],
            vec![3, 4, 11, 10, 6, 2, 1, 7, 5, 8, 9],
            vec![8, 6, 10, 2, 3, 1, 11, 5],
            vec![5, 11, 6, 4, 2]
        ],
        vec![
            vec![7, 9],
            vec![3, 7],
            vec![3, 4],
            vec![2, 9],
            vec![1, 8],
            vec![5, 9],
            vec![8, 9],
            vec![6, 9],
            vec![3, 5],
            vec![4, 5],
            vec![4, 9],
            vec![3, 6],
            vec![1, 7],
            vec![1, 3],
            vec![2, 8],
            vec![2, 6],
            vec![5, 7],
            vec![4, 6],
            vec![5, 8],
            vec![5, 6],
            vec![2, 7],
            vec![4, 8],
            vec![3, 8],
            vec![6, 8],
            vec![2, 5],
            vec![1, 4],
            vec![1, 9],
            vec![1, 6],
            vec![6, 7]
        ]
    )); // 0。这个例子反映了如果两个用户之间有共同语言就无需教他们新语言。
}
