/*
.. default-role:: math

Stone game最新力作！这次的规则是，Alice选一个切点 `i` ，计算出 ``array[..i]`` 的累加和、 ``array[i..]`` 的累加和，Bob会拿走累加和大的那一堆，然后Alice的分数是小的那堆的累加和，然后比赛继续在小的那堆里进行。具体来说，

-   如果 ``array[..i]`` 的累加和比较大，那么Bob会拿走 ``array[..i]`` ，留下 ``array[i..]`` 给Alice，Alice的分数就加上 ``array[i..]`` 的累加和，然后游戏继续在 ``array[i..]`` 里进行。
-   如果 ``array[i..]`` 的累加和比较大，那么Bob会拿走 ``array[i..]`` ，留下 ``array[..i]`` 给Alice，Alice的分数就加上 ``array[..i]`` 的累加和，然后游戏继续在 ``array[..i]`` 里进行。
-   如果一样大，那么Alice来选择留下 ``array[..i]`` 还是 ``array[i..]`` 。
-   如果 ``array`` 已经只剩下一个元素了，那么Alice不得分，游戏结束。

问Alice最多能拿多少分。

递推式很容易写出来，但是计算图里有很多重复节点，所以再加个cache就搞定了。
*/

struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn stone_game_v(stone_value: Vec<i32>) -> i32 {
        let mut cache = HashMap::new();
        let integrals: Vec<i32> = [0]
            .iter()
            .cloned()
            .chain(stone_value.iter().scan(0, |state, v| {
                *state = *state + *v;
                return Some(*state);
            }))
            .collect();
        return Self::opt(0, stone_value.len(), &integrals[..], &mut cache);
    }

    fn opt(
        left: usize,
        right: usize,
        integrals: &[i32],
        cache: &mut HashMap<(usize, usize), i32>,
    ) -> i32 {
        if cache.contains_key(&(left, right)) {
            return cache[&(left, right)];
        } else {
            if right - left == 1 {
                cache.insert((left, right), 0);
                return 0;
            } else {
                let mut res = 0;

                for middle in left + 1..right {
                    let a = integrals[right] - integrals[middle];
                    let b = integrals[middle] - integrals[left];
                    if a < b {
                        res = (a + Self::opt(middle, right, integrals, cache)).max(res);
                    } else if a > b {
                        res = (b + Self::opt(left, middle, integrals, cache)).max(res);
                    } else {
                        res = (a + Self::opt(middle, right, integrals, cache))
                            .max(b + Self::opt(left, middle, integrals, cache))
                            .max(res);
                    }
                }

                cache.insert((left, right), res);
                return res;
            }
        }
    }
}

fn main() {
    dbg!(Solution::stone_game_v(vec![6, 2, 3, 4, 5, 5])); // 18
    dbg!(Solution::stone_game_v(vec![7, 7, 7, 7, 7, 7, 7])); // 28
    dbg!(Solution::stone_game_v(vec![4])); // 0
}
