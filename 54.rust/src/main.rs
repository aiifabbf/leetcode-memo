/*
.. default-role:: math

螺旋遍历矩阵。从左上角开始、顺时针一圈，像剥洋葱一样。

挺简单的，用递归。这一层函数只剥一层，里面的丢给下一层函数。

头条三面的时候被问了这道题，秒做。然而follow up问螺旋遍历的最后一个点的坐标是啥。搞了很久，也没有写出闭式解，只写出了递推式。

定义 `\vec{f}(m, n)` 是 `m \times n` 矩阵螺旋遍历的最后一个点的坐标。发现

.. math::

    \vec{f}(m, n) = (1, 1) + \vec{f}(m - 2, n - 2)

还有四个初始条件

.. math::

    \begin{aligned}
        &\forall m \geq 1, \qquad \vec{f}(m, 1) = (m - 1, 0) \\
        &\forall n \geq 1, \qquad \vec{f}(1, n) = (0, n - 1) \\
        &\forall m \geq 2, \qquad \vec{f}(m, 2) = (1, 0) \\
        &\forall n \geq 2, \qquad \vec{f}(2, n) = (1, 0) \\
    \end{aligned}

闭式解不知道怎么算。多元递推方程好像没有特别好的解决方法。
*/

struct Solution;

impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut matrix = matrix;
        if matrix.is_empty() {
            return vec![];
        }
        if matrix[0].is_empty() {
            return vec![];
        }
        if matrix.len() == 1 {
            return matrix.pop().unwrap();
        }
        if matrix[0].len() == 1 {
            return matrix.into_iter().map(|v| v[0]).collect();
        }

        let mut res = vec![];
        let rowCount = matrix.len();
        let columnCount = matrix[0].len();

        // 为什么indices不需要mut呢……明明它是个Iterator
        let indices = (0..columnCount - 1)
            .map(|i| (0, i)) // 第一行从左到右
            .chain((0..rowCount - 1).map(|i| (i, columnCount - 1))) // 最后一列从上到下
            .chain((1..columnCount).rev().map(|i| (rowCount - 1, i))) // 最后一行从右到左
            .chain((1..rowCount).rev().map(|i| (i, 0))); // 第一列从下到上

        for v in indices {
            // 这里会move indices，所以不需要indices是mut的
            let (i, j) = v;
            res.push(matrix[i][j].clone());
        }

        matrix.pop();
        matrix.remove(0);

        for row in matrix.iter_mut() {
            row.pop();
            row.remove(0);
        }

        res.extend(Solution::spiral_order(matrix).into_iter());

        return res;
    }
}

fn main() {
    println!(
        "{:?}",
        Solution::spiral_order(vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9],])
    ); // 1, 2, 3, 6, 9, 8, 7, 4, 5
    println!("{:?}", Solution::spiral_order(vec![])); // []
    println!("{:?}", Solution::spiral_order(vec![vec![]])); // []
    println!("{:?}", Solution::spiral_order(vec![vec![1, 2, 3]])); // 1, 2, 3
    println!(
        "{:?}",
        Solution::spiral_order(vec![vec![1], vec![2], vec![3],])
    ); // 1, 2, 3
}
