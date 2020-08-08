/*
给一个二维矩阵，里面是字母，再给一个字符串，问矩阵里面存不存在一条不自交的路径，经过这个路径正好得到那个字符串

比如给

::

    ABCE
    SFCS
    ADEE

存在一条路径 ``ABFD`` 。但是不能是 ``ABFDASFCS`` ，因为交叉了。

我想到两种做法，回溯和DFS，写起来都差不多，原理也都差不多。感觉回溯更直观一点。

比如要找 ``ABFD`` ，那么首先去矩阵里定位所有 ``A`` ，再试着从每个 ``A`` 的位置开始往周边走，找 ``B`` 。如果找不到，就放弃这条路径。找到 ``B`` 之后再找 ``F`` ……以此类推。
*/

struct Solution;

use std::collections::BTreeSet;

impl Solution {
    #[cfg(feature = "backtrack")]
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let pattern: Vec<char> = word.chars().collect();
        let mut res = false;
        let mut path = vec![];
        let mut seen = BTreeSet::new();

        Self::backtrack(&mut path, &mut seen, &pattern[..], &board, &mut res);

        return res;
    }

    fn backtrack(
        path: &mut Vec<(usize, usize)>,
        seen: &mut BTreeSet<(usize, usize)>,
        pattern: &[char],
        board: &Vec<Vec<char>>,
        res: &mut bool,
    ) {
        if *res == true {
            // 如果已经找到了，就直接返回吧，不用再找了
            return;
        }

        if path.len() == pattern.len() {
            // 找到了
            *res = true;
            return;
        } else {
            if path.len() == 0 {
                // 还没开始走，先去找起点
                for (rowIndex, row) in board.iter().enumerate() {
                    for (columnIndex, value) in row.iter().enumerate() {
                        if *value == pattern[0] {
                            // 找到了
                            let position = (rowIndex, columnIndex);
                            path.push(position);
                            seen.insert(position);
                            Self::backtrack(path, seen, pattern, board, res); // 试着从这里走下去
                            seen.remove(&position);
                            path.pop();

                            if *res == true {
                                return;
                            }
                        }
                    }
                }
            } else {
                let rowCount = board.len();
                let columnCount = board[0].len();

                let last = path.last().unwrap();
                let neighbors = vec![
                    (last.0 as i64 - 1, last.1 as i64),
                    (last.0 as i64 + 1, last.1 as i64),
                    (last.0 as i64, last.1 as i64 - 1),
                    (last.0 as i64, last.1 as i64 + 1),
                ];

                for neighbor in neighbors.iter() {
                    if neighbor.0 >= 0
                        && neighbor.0 < rowCount as i64
                        && neighbor.1 >= 0
                        && neighbor.1 < columnCount as i64
                    {
                        let neighbor = (neighbor.0 as usize, neighbor.1 as usize);
                        if board[neighbor.0][neighbor.1] == pattern[path.len()]
                            && !seen.contains(&neighbor)
                        {
                            // 正好等于下一个字符，也没有发生交叉
                            path.push(neighbor);
                            seen.insert(neighbor);
                            Self::backtrack(path, seen, pattern, board, res);
                            seen.remove(&neighbor);
                            path.pop();

                            if *res == true {
                                return;
                            }
                        }
                    }
                }
            }
        }
    }

    #[cfg(feature = "dfs")]
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let pattern: Vec<char> = word.chars().collect();
        let mut path = vec![];

        return Self::dfs(&board, &mut path, &pattern[..]);
    }

    fn dfs(board: &Vec<Vec<char>>, path: &mut Vec<(usize, usize)>, pattern: &[char]) -> bool {
        if let Some(next) = pattern.first() {
            if let Some(last) = path.last() {
                let rowCount = board.len();
                let columnCount = board[0].len();

                let neighbors = [
                    (last.0 as i64 - 1, last.1 as i64),
                    (last.0 as i64 + 1, last.1 as i64),
                    (last.0 as i64, last.1 as i64 - 1),
                    (last.0 as i64, last.1 as i64 + 1),
                ];

                for neighbor in neighbors.iter() {
                    if 0 <= neighbor.0
                        && neighbor.0 < rowCount as i64
                        && 0 <= neighbor.1
                        && neighbor.1 < columnCount as i64
                    {
                        let neighbor = (neighbor.0 as usize, neighbor.1 as usize);
                        if board[neighbor.0][neighbor.1] == *next && !path.contains(&neighbor) {
                            path.push(neighbor);
                            if Self::dfs(board, path, &pattern[1..]) {
                                return true;
                            } else {
                                path.pop();
                            }
                        }
                    }
                }

                return false;
            } else {
                for (rowIndex, row) in board.iter().enumerate() {
                    for (columnIndex, value) in row.iter().enumerate() {
                        if value == next {
                            let start = (rowIndex, columnIndex);
                            path.push(start);
                            if Self::dfs(board, path, &pattern[1..]) {
                                return true;
                            } else {
                                path.pop();
                            }
                        }
                    }
                }

                return false;
            }
        } else {
            return true;
        }
    }
}

fn main() {
    dbg!(Solution::exist(
        vec![
            "ABCE".chars().collect(),
            "SFCS".chars().collect(),
            "ADEE".chars().collect(),
        ],
        "ABCCED".into()
    )); // true
    dbg!(Solution::exist(
        vec![
            "ABCE".chars().collect(),
            "SFCS".chars().collect(),
            "ADEE".chars().collect(),
        ],
        "SEE".into()
    )); // true
    dbg!(Solution::exist(
        vec![
            "ABCE".chars().collect(),
            "SFCS".chars().collect(),
            "ADEE".chars().collect(),
        ],
        "ABCB".into()
    )); // false
}
