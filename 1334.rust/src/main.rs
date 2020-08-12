/*
.. default-role:: math

`n` 个城市之间有长度不同的公路相连，找到这样一个城市，它与其他城市相连的公路里、长度小于等于某个阈值 `t` 的公路数量比其他城市都少。如果有多个这样的城市，返回编号最大的城市。

和以前做过的求某一个单独的起点到单独的终点的题目不一样了，这道题要求出每个点对 `(i, j)` 之间的最短距离。当然可以对于每个点都当做起点、应用一次Dijkstra算法，但是这样复杂度就是 `O((e + v \ln v) v)` 了。如果边很少的话，很合算，复杂度近似 `O(v^2 \ln v)` ，但是如果边很多，复杂度就是 `O(v^3 + v^2 \ln v)` 了。

.. 其实也还好

有个叫做Floyd的算法 <https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm> 可以在 `O(v^3)` 搞定这件事情，但是它的缺点是没办法算出单独的某个点对之间的最短距离，要算就要整张图、所有点对一起算出来。

我觉得Floyd比Dijkstra还要好理解。它是基于中继的思路来实现的。首先算出所有直接连接的、不经过任何中继节点的最短路径，这样得到是两两之间有直接连接的点对之间的最短路径。然后放宽条件，比如现在允许经过第0个节点，再次更新每个点对在直连或者经过第0个节点中继之后的最短路径。如果有些点原本根本不直接相连，现在有了第0个节点做中继，那么它们就有可能相连了；甚至有些点可能直连根本很远，经过节点0中继之后反而更近。

然后就这样以此类推，允许经过第0个和第1个节点，允许经过第0个、第1个和第2个节点……那么现在考虑一下，假如现在已经算出了 `i, j` 在允许经过第0、第1、……、第 `k - 1` 个节点的前提下的最短路径 `d(i, j, k - 1)` ，现在允许经过第 `k` 个节点了，那么 `d(i, j, k)` 和前面的项有什么关系呢？当然是要试探一下用第 `k` 个节点做中继是不是比以前更近，毕竟之前都不允许用第 `k` 个节点做中继。那么 `i` 和 `j` 用 `k` 做中继的最短路径是多少呢？是 `i` 到中继点 `k` 的最短路径、加上中继点 `k` 到 `j` 的最短路径

.. math::

    d(i, k, k - 1) + d(k - 1, j, k - 1)

当然这不一定是最短的，有可能强行经过 `k` 是多此一举，反而更远，所以再和之前的路径比较一下，选小的那个

.. math::

    d(i, j, k) = \min\{d(i, j, k - 1), d(i, k, k - 1) + d(k - 1, j, k - 1)\}

因为这一轮的结果仅仅和上一轮有关，和上上一轮无关，所以可以去掉 `k` 这一维。
*/

struct Solution;

impl Solution {
    // 关联矩阵，很浪费空间，但是却出奇的快
    #[cfg(feature = "adjacency-matrix")]
    pub fn find_the_city(n: i32, edges: Vec<Vec<i32>>, distance_threshold: i32) -> i32 {
        let n = n as usize;
        let mut graph = vec![vec![std::i64::MAX; n]; n]; // 一开始城市之间都不相连

        for i in 0..n {
            graph[i][i] = 0; // 自己和自己相连
        }

        for edge in edges.into_iter() {
            let a = edge[0] as usize;
            let b = edge[1] as usize;
            let w = edge[2] as i64;

            graph[a][b] = w;
            graph[b][a] = w; // 公路是双向的
        }

        // 下面就是著名的Floyd算法，很简单就这4行
        for relay in 0..n {
            for a in 0..n {
                for b in 0..n {
                    graph[a][b] = graph[a][b].min(graph[a][relay].saturating_add(graph[relay][b])); // 新的路径是从a到中继点、再从中继点到b，有可能比之前的路径更近、也有可能更远，不是必须一定要经过中继点的，所以取一个min
                    graph[b][a] = graph[a][b];
                }
            }
        }

        return (0..n)
            .min_by_key(|v| {
                (
                    graph[*v]
                        .iter()
                        .filter(|target| **target <= distance_threshold as i64)
                        .count(),
                    -(*v as i64),
                )
            })
            .unwrap_or(0) as i32; // 找到道路数量最少的、编号最大的城市
    }

    // 用关联集合存可以省空间，把空间复杂度从O(v^2)降低到O(e)。但是我不知道为啥慢了20多倍……
    #[cfg(feature = "adjacency-set")]
    pub fn find_the_city(n: i32, edges: Vec<Vec<i32>>, distance_threshold: i32) -> i32 {
        use std::collections::HashMap;

        let mut graph: HashMap<i32, HashMap<i32, i32>> = HashMap::new();

        for i in 0..n {
            graph.insert(i, [(i, 0)].iter().cloned().collect());
        }

        for edge in edges.into_iter() {
            let a = edge[0];
            let b = edge[1];
            let w = edge[2];

            if !graph.contains_key(&a) {
                graph.insert(a, HashMap::new());
            }
            graph.get_mut(&a).map(|v| v.insert(b, w));

            if !graph.contains_key(&b) {
                graph.insert(b, HashMap::new());
            }
            graph.get_mut(&b).map(|v| v.insert(a, w));
        }

        for relay in 0..n {
            for a in 0..n {
                for b in 0..n {
                    match (
                        graph[&a].get(&relay).cloned(),
                        graph[&relay].get(&b).cloned(),
                    ) {
                        (Some(route1), Some(route2)) => {
                            if !graph[&a].contains_key(&b) {
                                graph.get_mut(&a).unwrap().insert(b, route1 + route2);
                            } else {
                                let original = graph[&a][&b];
                                let updated = original.min(route1 + route2);
                                graph.get_mut(&a).unwrap().insert(b, updated);
                            }
                            let updated = graph[&a][&b];
                            graph.get_mut(&b).unwrap().insert(a, updated);
                        }
                        _ => {}
                    }
                }
            }
        }

        return (0..n)
            .min_by_key(|v| {
                (
                    graph[&v]
                        .iter()
                        .filter(|(target, distance)| **distance <= distance_threshold)
                        .count(),
                    -*v,
                )
            })
            .unwrap_or(0);
    }
}

fn main() {
    dbg!(Solution::find_the_city(
        4,
        vec![vec![0, 1, 3], vec![1, 2, 1], vec![1, 3, 4], vec![2, 3, 1],],
        4
    )); // 3
    dbg!(Solution::find_the_city(
        6,
        vec![
            vec![0, 3, 7],
            vec![2, 4, 1],
            vec![0, 1, 5],
            vec![2, 3, 10],
            vec![1, 3, 6],
            vec![1, 2, 1],
        ],
        417
    )); // 5
    dbg!(Solution::find_the_city(
        6,
        vec![
            vec![2, 3, 7],
            vec![2, 5, 8],
            vec![0, 2, 8],
            vec![4, 5, 5],
            vec![1, 5, 10],
            vec![3, 4, 3],
            vec![0, 5, 9],
            vec![1, 2, 1],
        ],
        3269
    )); // 5
}
