/*
.. default-role:: math

在一个很有规律的 `m \times n` 矩阵里面找某个数字存不存在。这个矩阵的规律之处在于

-   每一行都是单调（不一定严格）递增的
-   下一行的第一个数字大于等于这一行的最后一个数字

看到递增，很容易想到二分搜索。如果直接忽略掉第二个性质，对每一行都做一次二分搜索，那么复杂度也不是很大，仅仅只是 `O(m \ln n)` 而已，已经很可以了。

如果想用一下性质二，也很容易想到。因为下一行的第一个数字大于等于这一行的最后一个数字，那么如果把整个矩阵拍扁（或者叫flatten），那么得到的一维array仍然是单调递增的。比如

::

    1 2 3 4
    5 6 7 8

拍扁之后变成了

::

    1 2 3 4 5 6 7 8

仍然是单调递增的。这时候就像和普通的二分一样做就好了。
*/

struct Solution;

use std::cmp::Ordering;

impl Solution {
    // 虽然O(m ln n)，但是实在是太优雅了
    #[cfg(feature = "simple")]
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        matrix.iter().any(|row| row.binary_search(&target).is_ok())
    }

    // O(ln (mn))，写起来有点长
    #[cfg(feature = "fast")]
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let row_count = matrix.len();
        if row_count == 0 {
            return false;
        }
        let column_count = matrix[0].len();
        if column_count == 0 {
            return false;
        }

        // let (row_count, column_count) = match matrix.get(0) {
        //     Some(row) => match row.len() {
        //         0 => (0, 0),
        //         b => (matrix.len(), b),
        //     },
        //     None => (0, 0),
        // };
        // 不知道怎么才能优雅地处理空矩阵的情况

        let mut left = 0;
        let mut right = row_count * column_count;

        while left < right {
            let middle = (left + right) / 2; // 拍扁之后的一维坐标
            let row_index = middle / column_count; // 把一维坐标转换成二维坐标
            let column_index = middle % column_count;
            match target.cmp(&matrix[row_index][column_index]) {
                Ordering::Equal => right = middle,
                Ordering::Greater => left = middle + 1,
                Ordering::Less => right = middle,
            }
        }

        // 因为找的是最靠左的插入位置，所以还要检测一下插入位置的右边是不是target
        let row_index = left / column_count;
        let column_index = left % column_count;
        if row_index < row_count {
            if column_index < column_count {
                if matrix[row_index][column_index] == target {
                    return true;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
}

fn main() {
    dbg!(Solution::search_matrix(vec![vec![1, 1]], 0)); // true
    dbg!(Solution::search_matrix(vec![], 0)); // false
    dbg!(Solution::search_matrix(vec![vec![]], 0)); // false
}
