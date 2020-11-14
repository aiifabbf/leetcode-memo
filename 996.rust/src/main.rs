/*
.. default-role:: math

给一些数字，可能有重复数字，能使得任意相邻两个数字之和是完全平方数的排列方式有多少种？

比如给 ``1, 17, 8`` ，只有两种

::

    1, 8, 17
    17, 8, 1

比如给 ``2, 2, 2`` ，只有一种

::

    2, 2, 2

输入规模暗示这个题目复杂度可能是 `O(n!)` ……

第一想法是把数字当做节点，两个和能成为完全平方数的数字之间有一条边，然后从每个数字出发，找到从这个数字出发的、正好经过每个节点、每个节点都正好只经过一次的Hamilton回路有多少条。

试着写了一个，发现在 ``2, 2, 2, 2, 2, 2, 2, 2`` 这种重复数字特别多的情况很慢很慢。

然后用回溯秒做，先统计出每种数字出现的次数，这样如果是12个2的话，一次就走完了，非常节能。
*/

struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn num_squareful_perms(a: Vec<i32>) -> i32 {
        let mut path = vec![];
        let mut counter = HashMap::new(); // 每种数字出现的次数

        for v in a.iter() {
            *counter.entry(*v).or_insert(0) += 1;
        }

        let mut res = 0;
        Self::backtrack(&mut path, &counter, &mut res);
        return res as i32;
    }

    fn backtrack(path: &mut Vec<i32>, choices: &HashMap<i32, usize>, res: &mut usize) {
        if choices.is_empty() && path.len() >= 2 {
            *res += 1;
        } else {
            if let Some(last) = path.last().cloned() {
                for (k, v) in choices.iter() {
                    if Self::is_perfect_square((*k + last) as i64) {
                        path.push(*k); // 试着这里放k
                        let mut histogram = choices.clone(); // 不太节能，不过反正最多只有12个数字
                        match histogram.get_mut(k) {
                            Some(v) => {
                                if *v == 1 {
                                    histogram.remove(k);
                                } else {
                                    *v -= 1;
                                }
                            }
                            _ => {}
                        } // 因为刚才放了个k，所以可选的k少了一个
                        Self::backtrack(path, &histogram, res);
                        path.pop();
                    }
                }
            } else {
                for (k, v) in choices.iter() {
                    path.push(*k);
                    let mut histogram = choices.clone();
                    match histogram.get_mut(k) {
                        Some(v) => {
                            if *v == 1 {
                                histogram.remove(k);
                            } else {
                                *v -= 1;
                            }
                        }
                        _ => {}
                    }
                    Self::backtrack(path, &mut histogram, res);
                    path.pop();
                }
            }
        }
    }

    // 判断是否是完全平方数，用了二分可以精确判断，避免浮点数sqrt误差问题
    fn is_perfect_square(n: i64) -> bool {
        // 先用二分找到满足m^2 >= n的第一个m
        let f = |m: i64| -> bool { m.pow(2) >= n };

        let target = true;
        let mut left = 0;
        let mut right = n;

        while left < right {
            let middle = (left + right) / 2;
            let test = f(middle);
            if target > test {
                left = middle + 1;
            } else if target < test {
                right = middle;
            } else {
                right = middle;
            }
        }

        return left.pow(2) == n;
    }
}

fn main() {
    dbg!(Solution::num_squareful_perms(vec![1, 17, 8])); // 2
    dbg!(Solution::num_squareful_perms(vec![2, 2, 2])); // 1
    dbg!(Solution::num_squareful_perms(vec![2; 12])); // 1
    dbg!(Solution::num_squareful_perms(vec![
        566613866, 671149742, 807238901, 574105648, 573052576, 983549587
    ]));
}
