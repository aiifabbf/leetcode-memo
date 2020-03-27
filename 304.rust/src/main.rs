/*
快速计算任意子矩阵的累加和

标准的2D前缀和（我喜欢叫积分）。定义 ``integrals[i][j]`` 表示 ``matrix[: i, : j]`` 这个子矩阵的累加和。这样任意子矩阵 ``matrix[i: j, a: b]`` 的累加和就是

::

    integrals[j][b] - integrals[i][b] - integrals[j][a] + integrals[i][a]

.. note:: `博客 <http://aiifabbf.github.com/prefix-sum>`_ 里详细讲了前缀和技巧，有图有推导，看看吧。

那这个 ``integrals[i][j]`` 一开始怎么生成呢？也很简单的，还是从刚才那个式子入手，如果子矩阵是个1x1的矩阵，里面只有一个元素，比如 ``matrix[i: j, a: b]`` 里面， `j = i + 1, b = a + 1` ，那么 ``matrix[i: j, a: b] == matrix[i, a]`` ，把刚才的式子改写

::

    matrix[i, a] = integrals[i + 1][a + 1] - integrals[i][a + 1] - integrals[i + 1][a] + integrals[i][a]

把 ``integrals[i + 1]]a + 1`` 移到前面来

::

    integrals[i + 1][a + 1] = matrix[i, a] + integrals[i][a + 1] + integrals[i + 1][a] - integrals[i][a]

这就是递推式啦。做下变量代换

::

    integrals[i][a] = matrix[i - 1, a - 1] + integrals[i - 1][a] + integrals[i][a - 1] - integrals[i - 1][a - 1]
*/

struct NumMatrix {
    integrals: Option<Vec<Vec<i32>>>, // 假如是空矩阵，就是None
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumMatrix {
    fn new(matrix: Vec<Vec<i32>>) -> Self {
        let rowCount = matrix.len();
        if rowCount == 0 {
            return Self { integrals: None };
        }
        let columnCount = matrix[0].len();
        if columnCount == 0 {
            return Self { integrals: None };
        }

        let mut integrals = vec![vec![0; columnCount + 1]; rowCount + 1]; // integrals[i][j]表示matrix[: i, : j]的和

        for i in 1..rowCount + 1 {
            for j in 1..columnCount + 1 {
                integrals[i][j] = matrix[i - 1][j - 1] + integrals[i - 1][j] + integrals[i][j - 1]
                    - integrals[i - 1][j - 1]; // 这就是刚才的递推式
            }
        }

        return Self {
            integrals: Some(integrals),
        };
    }

    fn sum_region(&self, row1: i32, col1: i32, row2: i32, col2: i32) -> i32 {
        let i = row1 as usize;
        let j = row2 as usize + 1;
        let a = col1 as usize;
        let b = col2 as usize + 1;

        match &self.integrals {
            Some(integrals) => {
                return integrals[j][b] - integrals[j][a] - integrals[i][b] + integrals[i][a];
            }
            None => {
                return 0;
            }
        }
    }
}

fn main() {
    let matrix = NumMatrix::new(vec![
        vec![3, 0, 1, 4, 2],
        vec![5, 6, 3, 2, 1],
        vec![1, 2, 0, 1, 5],
        vec![4, 1, 0, 1, 7],
        vec![1, 0, 3, 0, 5],
    ]);
    println!("{:?}", matrix.sum_region(2, 1, 4, 3)); // 8
    println!("{:?}", matrix.sum_region(1, 1, 2, 2)); // 11
    println!("{:?}", matrix.sum_region(1, 2, 2, 4)); //12

    let matrix = NumMatrix::new(vec![vec![]]); // 这算什么屑case
    println!("{:?}", matrix.sum_region(0, 0, 0, 0)); // 0

    let matrix = NumMatrix::new(vec![]); // 这算什么屑case
    println!("{:?}", matrix.sum_region(0, 0, 0, 0)); // 0
}
