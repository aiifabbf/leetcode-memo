/*
.. default-role:: math

给一个二维矩阵，0表示可以通行、1表示障碍。可以上下左右斜向8个方向移动。一开始在左上角，问走到右下角的最短需要几步。

从起点往外一圈一圈BFS遍历、一边遍历一边记下从起点到每个节点的距离就好了。
*/

struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn shortest_path_binary_matrix(grid: Vec<Vec<i32>>) -> i32 {
        let rowCount = grid.len();
        let columnCount = grid[0].len();
        if grid[0][0] == 1 {
            // 如果起点上就是障碍的话
            if rowCount == 1 && columnCount == 1 {
                // 而起点就是终点，那么路径就是[(0, 0)]
                return 1;
            } else {
                // 从起点不可能走到终点
                return -1;
            }
        }

        let mut queue = vec![(0, 0)];
        let mut distances = HashMap::new(); // distance[(i, j)] = d表示从起点走到(i, j)要走d步
        distances.insert((0, 0), 0);
        let mut traveled = HashSet::new(); // 已经遍历过的节点

        while !queue.is_empty() {
            let mut levelQueue = vec![]; // 下一层要遍历的节点

            for node in queue.iter() {
                let neighbors = [
                    (node.0 as i64 - 1, node.1 as i64 - 1), // 左上
                    (node.0 as i64 - 1, node.1 as i64),     // 正上
                    (node.0 as i64 - 1, node.1 as i64 + 1), // 右上
                    (node.0 as i64, node.1 as i64 - 1),     // 左边
                    (node.0 as i64, node.1 as i64 + 1),     // 右边
                    (node.0 as i64 + 1, node.1 as i64 - 1), // 左下
                    (node.0 as i64 + 1, node.1 as i64),     // 正下
                    (node.0 as i64 + 1, node.1 as i64 + 1), // 右下
                ];

                for neighbor in neighbors.into_iter() {
                    if 0 <= neighbor.0
                        && neighbor.0 < rowCount as i64
                        && 0 <= neighbor.1
                        && neighbor.1 < columnCount as i64
                    {
                        let neighbor = (neighbor.0 as usize, neighbor.1 as usize);
                        if grid[neighbor.0 as usize][neighbor.1 as usize] == 0
                            && !traveled.contains(&neighbor)
                            && !levelQueue.contains(&neighbor)
                        {
                            // 到neighbor的一条可能路径是从node直接跳到neighbor，那么走这条路径的话，步数就是 走到node的距离 + node到neighbor的距离
                            let distanceToNode = distances.get(node).unwrap().clone();
                            if let Some(distance) = distances.get_mut(&neighbor) {
                                // 可能之前有别的节点也能跳到这个节点、并且记下了从那个节点跳到这个节点的距离。这个距离有可能不是最小的
                                // 所以比较一下两个距离，取小的那个
                                *distance = (*distance).min(distanceToNode + 1);
                            } else {
                                // 这个节点之前从来没有被更新过距离
                                distances.insert(neighbor, distanceToNode + 1);
                            }
                            levelQueue.push(neighbor);
                        }
                    }
                }

                traveled.insert(*node);
            }

            queue = levelQueue;
        }

        return distances
            .get(&(rowCount - 1, columnCount - 1))
            .unwrap_or(&(-2))
            + 1; // 路径距离是步数+1,
    }
}

fn main() {
    dbg!(Solution::shortest_path_binary_matrix(vec![
        vec![0, 0, 0],
        vec![1, 1, 0],
        vec![1, 1, 0],
    ])); // 4
    dbg!(Solution::shortest_path_binary_matrix(vec![
        vec![0, 1],
        vec![1, 0],
    ])); // 2
}
