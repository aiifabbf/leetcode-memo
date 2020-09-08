/*
.. default-role:: math

给个二维矩阵，1表示起点（只有一个），2表示终点（也只有一个），0表示可以走的格子，-1表示障碍物。问从起点到终点，经过每个0、同时每个0只经过一次的路径有多少条。

比如给

::

    1 0 0 0
    0 0 0 0
    0 0 2 -1

总共有两条路，第一条是从1往右边走，走到尽头之后往下，然后左拐。另一条是从1往下走，走到尽头之后右拐，再往上。

用回溯挺好的。在每个格子上，都尝试往上下左右四个方向走下去。符合条件的路径满足两个条件

-   路径经过的最后位置在终点上，也就是一个值是2的格子
-   路径经过的格子数量是矩阵里值是0的格子的数量+2，+2是因为起点和终点也要算
*/

struct Solution;

impl Solution {
    pub fn unique_paths_iii(grid: Vec<Vec<i32>>) -> i32 {
        let mut path = vec![]; // 当前路径
        let mut res = 0; // 总共有多少条符合条件的路径
        let mut length = 2; // 路径长度目标值，用来判断有没有经过所有空位，符合条件的路径上空位的数量一定是0的数量+1个起点+1个终点

        for (i, row) in grid.iter().enumerate() {
            for (j, w) in row.iter().enumerate() {
                if *w == 1 {
                    // 找到起点
                    path.push((i, j));
                }

                if *w == 0 {
                    // 挑出所有的空位
                    length += 1;
                }
            }
        }

        Self::backtrack(&mut path, length, &grid, &mut res); // 从起点开始走
        return res as i32;
    }

    fn backtrack(
        path: &mut Vec<(usize, usize)>,
        length: usize, // 其实这个信息可以完全用grid算出，但是为了效率还是传一下吧
        grid: &Vec<Vec<i32>>,
        res: &mut usize,
    ) {
        let rowCount = grid.len();
        let columnCount = grid[0].len();

        let position = path.last().unwrap(); // 当前位置
        if grid[position.0][position.1] == 2 && path.len() == length {
            // 如果已经到达终点，并且之前经过了所有空位
            *res += 1; // 那么这是一条目标路径
            return;
        }

        let neighbors = [
            (position.0 as i64 - 1, position.1 as i64),
            (position.0 as i64 + 1, position.1 as i64),
            (position.0 as i64, position.1 as i64 - 1),
            (position.0 as i64, position.1 as i64 + 1),
        ]; // 上下左右四个可能走的方向

        for neighbor in neighbors.iter() {
            if 0 <= neighbor.0
                && neighbor.0 < rowCount as i64
                && 0 <= neighbor.1
                && neighbor.1 < columnCount as i64
            {
                let neighbor = (neighbor.0 as usize, neighbor.1 as usize);
                if (grid[neighbor.0][neighbor.1] == 0 || grid[neighbor.0][neighbor.1] == 2) // 这是个可达的空位
                    && !path.contains(&neighbor)
                // 而且之前没有走过
                {
                    path.push(neighbor); // 那就试着走这里
                    Self::backtrack(path, length, grid, res);
                    path.pop(); // 撤销选择
                }
            }
        }
    }
}

fn main() {
    dbg!(Solution::unique_paths_iii(vec![
        vec![1, 0, 0, 0],
        vec![0, 0, 0, 0],
        vec![0, 0, 2, -1],
    ])); // 2
    dbg!(Solution::unique_paths_iii(vec![
        vec![1, 0, 0, 0],
        vec![0, 0, 0, 0],
        vec![0, 0, 0, 2],
    ])); // 4
}
