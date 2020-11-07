/*
.. default-role:: math

在矩阵里寻找从左上角走到右下角最省力的路径。所谓最省力不是传统的路径上节点值的和最小，而是路径上任意两个相邻节点的差值的最大值最小。

比如

::

    1 2 2
    3 8 2
    5 3 5

最省力的路径是

::

    1 2 2
    |
    3 8 2
    |
    5-3-5

花费的力气是2，因为路径上任意两个相邻节点的差值的最大值是2。

详细解释在Python写的版本里。大致是归约的思路，把极值表述归约到判定表述。
*/

struct Solution;

use std::cmp::Ordering;
use std::collections::HashSet;

impl Solution {
    pub fn minimum_effort_path(heights: Vec<Vec<i32>>) -> i32 {
        let matrix = heights;
        let row_count = matrix.len();
        if row_count == 0 {
            return 0;
        }
        let column_count = matrix[0].len();

        if row_count == 1 && column_count == 1 {
            return 0;
        }

        // 写成了closure，可以捕捉外面的matrix，省得传进去
        let feasible = |threshold: i32| -> bool {
            let mut queue: HashSet<(usize, usize)> = HashSet::new();
            queue.insert((0, 0));
            let mut traveled: HashSet<(usize, usize)> = HashSet::new();

            while !queue.is_empty() {
                let mut level_queue: HashSet<(usize, usize)> = HashSet::new();

                for node in queue.iter().cloned() {
                    if node == (row_count - 1, column_count - 1) {
                        return true;
                    }

                    let (i, j) = (node.0 as i64, node.1 as i64); // 这里挺恶心的……rust要求下标一定是usize，怎么优雅地判断上下左右四个邻居有没有超出地图边界呢？如果是0_usize，减去1的话会overflow panic

                    for neighbor in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
                        .iter()
                        .cloned()
                    {
                        if 0 <= neighbor.0
                            && neighbor.0 < row_count as i64
                            && 0 <= neighbor.1
                            && neighbor.1 < column_count as i64
                        {
                            let (i, j) = (node.0, node.1);
                            let neighbor = (neighbor.0 as usize, neighbor.1 as usize);
                            if !traveled.contains(&neighbor)
                                && !level_queue.contains(&neighbor)
                                && (matrix[neighbor.0][neighbor.1] - matrix[i][j]).abs()
                                    <= threshold
                            {
                                level_queue.insert(neighbor);
                            }
                        }
                    }

                    traveled.insert(node);
                }

                queue = level_queue;
            }

            return false;
        };

        // 把f(n)当做0, 0, ..., 0, 1, 1, ...这样单调递增的array，我们只不过是要找到1第一次出现的位置罢了
        let target = true;
        let mut left = 0;
        let mut right = (1..column_count)
            .map(|j| (matrix[0][j] - matrix[0][j - 1]).abs())
            .chain((1..row_count).map(|i| (matrix[i][0] - matrix[i - 1][0]).abs()))
            .max()
            .unwrap()
            + 1;

        while left < right {
            let middle = (left + right) / 2;
            match target.cmp(&feasible(middle)) {
                // 很神奇，false < true
                Ordering::Less => right = middle,
                Ordering::Greater => left = middle + 1,
                Ordering::Equal => right = middle,
            }
        }

        return left;
    }
}

fn main() {
    dbg!(Solution::minimum_effort_path(vec![
        vec![1, 2, 2],
        vec![3, 8, 2],
        vec![5, 3, 5],
    ])); // 2
}
