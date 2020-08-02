/*
.. default-role:: math

列出从起点到终点的每一条路径

有两种思路

-   从起点到终点的路径是从终点到“下一跳就能到终点”的那些节点的路径、接上那些节点到终点的路径。再把那些节点作为最终的终点，不断递归
-   用回溯，从起点开始，试着往每个方向走下去，记下能最终走到终点的路径

两种本质上是一样的，复杂度应该也一样。
*/

struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    // naive BFS做法，可能会爆内存，因为不是每个节点最后都能走到终点
    // pub fn all_paths_source_target(graph: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    //     let mut outs = graph;

    //     let mut routes: HashMap<i32, HashSet<Vec<i32>>> = HashMap::new();
    //     routes.insert(0, vec![vec![0]].into_iter().collect());

    //     let mut queue = VecDeque::new();
    //     queue.push_back(0 as i32);

    //     while let Some(node) = queue.pop_front() {
    //         for neighbor in outs[node as usize].iter() {
    //             if !routes.contains_key(neighbor) {
    //                 routes.insert(*neighbor, HashSet::new());
    //             }

    //             let routesToNode = routes[&(node as i32)].clone();

    //             for route in routesToNode.into_iter() {
    //                 let mut route = route;
    //                 route.push(*neighbor);
    //                 routes.get_mut(neighbor).unwrap().insert(route);
    //             }

    //             queue.push_back(*neighbor);
    //         }
    //     }

    //     return routes[&(outs.len() as i32 - 1)].iter().cloned().collect();
    // }

    #[cfg(feature = "recursion")]
    pub fn all_paths_source_target(graph: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut outs = HashMap::new();
        let mut ins = HashMap::new();

        for i in 0..graph.len() {
            outs.insert(i as i32, HashSet::new());
            ins.insert(i as i32, HashSet::new());
        }

        for (i, v) in graph.iter().enumerate() {
            for j in v.iter() {
                outs.get_mut(&(i as i32)).unwrap().insert(*j);
                ins.get_mut(j).unwrap().insert(i as i32);
            }
        }

        return Self::routesToTarget(&outs, &ins, graph.len() as i32 - 1)
            .into_iter()
            .collect();
    }

    fn routesToTarget(
        outs: &HashMap<i32, HashSet<i32>>,
        ins: &HashMap<i32, HashSet<i32>>,
        target: i32,
    ) -> HashSet<Vec<i32>> {
        if target == 0 {
            return vec![vec![0]].into_iter().collect();
        }

        let mut res = HashSet::new();

        for source in ins.get(&target).unwrap().iter() {
            res.extend(
                Self::routesToTarget(&outs, &ins, *source)
                    .into_iter()
                    .map(|mut v| {
                        v.push(target);
                        v
                    }),
            );
        }

        return res;
    }

    #[cfg(feature = "backtrack")]
    pub fn all_paths_source_target(graph: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut path = vec![0];
        let mut res = HashSet::new();

        Self::backtrack(&mut path, &graph, &mut res);
        return res.into_iter().collect();
    }

    fn backtrack(path: &mut Vec<i32>, outs: &[Vec<i32>], res: &mut HashSet<Vec<i32>>) {
        if let Some(position) = path.last() {
            if *position == outs.len() as i32 - 1 {
                // 如果现在已经在终点了
                res.insert(path.clone()); // 说明
            } else {
                for neighbor in outs[*position as usize].iter() {
                    // 尝试一下在当前这个位置能往下走的每个选择
                    path.push(*neighbor); // 尝试走一下这个方向
                    Self::backtrack(path, outs, res); // 能不能走到终点全交给下一层了
                    path.pop(); // 撤销，不走这个方向了
                }
            }
        } else {
            path.push(0);
            Self::backtrack(path, outs, res);
        }
    }
}

fn main() {
    dbg!(Solution::all_paths_source_target(vec![
        vec![1, 2],
        vec![3],
        vec![3],
        vec![],
    ])); // [[0, 1, 3], [0, 2, 3]]
    dbg!(Solution::all_paths_source_target(vec![
        vec![4, 14, 3, 12, 5, 2, 8, 1, 10, 6, 13, 7, 11],
        vec![3, 5, 11, 13, 2, 4, 9, 10, 12, 6],
        vec![4, 5, 10, 6, 7, 13, 14, 12, 11, 3, 8],
        vec![7, 5, 6, 9, 13, 12, 11, 4, 14],
        vec![6, 8, 13, 12, 7, 10, 5, 9, 14, 11],
        vec![8, 9, 7, 13, 12, 11, 14, 10, 6],
        vec![8, 10, 14, 11, 13, 7],
        vec![11, 10, 12, 14, 9, 8],
        vec![11, 10, 13, 12, 9],
        vec![12, 13, 11, 10, 14],
        vec![14, 11, 13],
        vec![13, 14, 12],
        vec![14, 13],
        vec![14],
        vec![],
    ]));
}
