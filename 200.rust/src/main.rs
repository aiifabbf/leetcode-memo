/* 
1表示陆地、0表示水，有多少块陆地？

Union find经典题了。先扫描一遍，把union find graph建好，再扫一遍，取得每个节点的根节点，放到hash set里，hash set的大小就是陆地的数量啦。
*/

struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;
use std::hash::Hash;

trait UnionFind<'a, T> {
    fn root(&'a self, p: &'a T) -> &'a T;
    fn isConnected(&'a self, p: &'a T, q: &'a T) -> bool;
    fn union(&mut self, p: T, q: T);
}

impl<'a, T> UnionFind<'a, T> for HashMap<T, T>
where
    T: Hash + Eq + Copy,
{
    fn root(&'a self, p: &'a T) -> &'a T {
        let mut p = p;

        while self.get(p).unwrap() != p {
            p = self.get(p).unwrap();
        }

        return p;
    }

    fn isConnected(&'a self, p: &'a T, q: &'a T) -> bool {
        let rootOfP = self.root(p);
        let rootOfQ = self.root(q);

        return rootOfP == rootOfQ;
    }

    fn union(&mut self, p: T, q: T) {
        let mut p = p;

        while *self.get(&p).unwrap() != p {
            self.insert(p, *self.get(self.get(&p).unwrap()).unwrap());
            p = *self.get(&p).unwrap();
        }

        let rootOfP = p;
        let mut q = q;

        while *self.get(&q).unwrap() != q {
            self.insert(q, *self.get(self.get(&q).unwrap()).unwrap());
            q = *self.get(&q).unwrap();
        }

        let rootOfQ = q;

        *self.get_mut(&rootOfP).unwrap() = rootOfQ;
    }
}

impl Solution {
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        if grid.is_empty() {
            return 0;
        } else if grid[0].is_empty() {
            return 0;
        }

        let rowCount = grid.len();
        let columnCount = grid[0].len();
        let mut graph = HashMap::new();

        for (rowIndex, row) in grid.iter().enumerate() {
            for (columnIndex, value) in row.iter().enumerate() {
                let position = (rowIndex as isize, columnIndex as isize);

                if *value == '1' {
                    graph.entry(position).or_insert(position);
                    let neighbors = vec![
                        (position.0 - 1, position.1),
                        (position.0 + 1, position.1),
                        (position.0, position.1 - 1),
                        (position.0, position.1 + 1),
                    ];

                    for neighbor in neighbors.into_iter() {
                        if (0..rowCount as isize).contains(&neighbor.0)
                            && (0..columnCount as isize).contains(&neighbor.1)
                        {
                            if grid[neighbor.0 as usize][neighbor.1 as usize] == '1' {
                                graph.entry(neighbor).or_insert(neighbor);
                                graph.union(neighbor, position);
                            }
                        }
                    }
                }
            }
        }

        let islands: HashSet<(isize, isize)> =
            graph.iter().map(|(k, v)| *graph.root(k)).collect();
        return islands.len() as i32;
    }
}

fn main() {
    println!(
        "{:?}",
        Solution::num_islands(vec![
            "11110".chars().collect(),
            "11010".chars().collect(),
            "11000".chars().collect(),
            "00000".chars().collect(),
        ])
    ); // 1
    println!("{:?}", Solution::num_islands(vec![])); // 0
    println!("{:?}", Solution::num_islands(vec![vec![]])); // 0
}
