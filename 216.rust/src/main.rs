/*
.. default-role:: math

`[1, 9] \cap Z` 里取一个大小 `k` 的子集，使得这些数字加起来正好等于 `n` 的取法有哪些？

比如取出3个数字，要得到和为7，总共只有 `1 + 2 + 4` 这1种取法。

用回溯秒做。
*/

struct Solution;

impl Solution {
    pub fn combination_sum3(k: i32, n: i32) -> Vec<Vec<i32>> {
        let mut path = vec![];
        let mut res = vec![];

        Self::backtrack(&mut path, k as usize, n, &mut res);
        return res;
    }

    fn backtrack(path: &mut Vec<i32>, length: usize, target: i32, res: &mut Vec<Vec<i32>>) {
        if length == 0 {
            return;
        } else if path.len() == length && path.iter().sum::<i32>() == target {
            // 总共取了length个数字，并且这些数字加起来等于target
            res.push(path.clone()); // 说明path这种取法是可行的，加入结果集
        } else {
            let last = path.last().cloned().unwrap_or(0); // 如果最后一步取了last，因为不允许重复，这一次应该从[last + 1, 9]里取数字。顺便也处理了path为空的情况

            for i in last + 1..10 {
                path.push(i);
                Self::backtrack(path, length, target, res);
                path.pop();
            }

            // 还可以做点优化，比如在发现剩下还要取7个数字、但是可取的数字不满7个的时候提前退出
        }
    }
}

fn main() {
    dbg!(Solution::combination_sum3(3, 7)); // [1, 2, 4]
    dbg!(Solution::combination_sum3(3, 9)); // [1, 2, 6], [1, 3, 5], [2, 3, 4]
}
