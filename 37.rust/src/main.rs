/*
.. default-role:: math

解数独

用回溯，找到一个需要填的格子，看一下这个格子所在的行、列、3x3小格，统计出能填的数字，把能填的数字都试一遍，再递归地填下一格。
*/

struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        let mut res = false;
        Self::backtrack(board, 0, &mut res);
    }

    fn backtrack(
        path: &mut Vec<Vec<char>>,
        start: usize,   // 现在将要填的格子的下标。81个格子从左到右、从上到下从0开始标
        res: &mut bool, // 是否已经解出来了
    ) {
        if *res == true {
            // 如果已经解出来了，那不管了
            return;
        }

        let mut rowIndex = 0;
        let mut columnIndex = 0;

        // 找到第一个需要填的格子
        if let Some(start) = (start..81)
            .filter(|v| {
                let (i, j) = (v / 9, v % 9); // 从start里提取第几行、第几列
                path[i][j] == '.'
            })
            .next()
        {
            rowIndex = start / 9;
            columnIndex = start % 9;
        } else {
            // 找不到需要填的格子了，说明已经全填完了
            *res = true; // 说明解出来了
            return;
        }

        let mut choices: HashSet<char> = "123456789".chars().collect(); // 这一格可用的数字

        // 去掉和这一格同一行的其他数字
        for j in 0..9 {
            if path[rowIndex][j] != '.' {
                choices.remove(&path[rowIndex][j]);
            }
        }

        // 去掉和这一格同一列的其他数字
        for i in 0..9 {
            if path[i][columnIndex] != '.' {
                choices.remove(&path[i][columnIndex]);
            }
        }

        // 去掉和这一格在同一个3x3小格的其他数字
        let groupRowIndex = rowIndex / 3 * 3; // 这一格所在的3x3小格左上角的位置
        let groupColumnIndex = columnIndex / 3 * 3;

        for i in groupRowIndex..groupRowIndex + 3 {
            for j in groupColumnIndex..groupColumnIndex + 3 {
                if path[i][j] != '.' {
                    choices.remove(&path[i][j]);
                }
            }
        }

        // 剩下的就是这一个可以填的数字了
        for choice in choices.iter() {
            path[rowIndex][columnIndex] = *choice; // 试着填这个数字
            Self::backtrack(path, start + 1, res); // 一个一个试
            if *res == true {
                return;
            }
            path[rowIndex][columnIndex] = '.'; // 撤销
        }
    }
}

fn main() {
    let mut board = vec![
        "53..7....".chars().collect(),
        "6..195...".chars().collect(),
        ".98....6.".chars().collect(),
        "8...6...3".chars().collect(),
        "4..8.3..1".chars().collect(),
        "7...2...6".chars().collect(),
        ".6....28.".chars().collect(),
        "...419..5".chars().collect(),
        "....8..79".chars().collect(),
    ];
    Solution::solve_sudoku(&mut board);

    for row in board.iter() {
        println!("{:?}", row);
    }
}
