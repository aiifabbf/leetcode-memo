/*
用rust又做了一遍。主要想练习一下rust里trait、impl的写法。
*/

struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;
use std::hash::Hash;

trait UnionFind<'a, T> {
    fn root(&'a self, p: &'a T) -> &'a T; // 强行把这个从T变成&T，但其实对于Copy来说，T和&T性能上没什么差别……
    fn isConnected(&'a self, p: &'a T, q: &'a T) -> bool; // 就当练习一下lifetime吧……
    fn union(&mut self, p: T, q: T);
} // 这边我不知道怎么把参数从T变成&T

impl<'a, T> UnionFind<'a, T> for HashMap<T, T>
where
    T: Hash + Eq + Copy, // 这里也是，不知道怎么去掉Copy
{
    fn root(&'a self, p: &'a T) -> &'a T {
        // 这里是python里不同的写法。python里面可以在root()里面一边找root、一边优化图结构，但是这里不行，只能只读。
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

    fn union(&mut self, p: T, q: T) { // 所以把优化图结构的事情移到了这里，不知道这个对性能有什么影响
        let mut p = p;

        while *self.get(&p).unwrap() != p {
            self.insert(p, *self.get(self.get(&p).unwrap()).unwrap()); // 这一行写的真的很难看，不知道有没有更好的写法
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
    pub fn smallest_string_with_swaps(s: String, pairs: Vec<Vec<i32>>) -> String {
        let mut graph: HashMap<i32, i32> = HashMap::new();
        let mut string: Vec<char> = s.chars().collect();

        for pair in pairs.iter() {
            let a = pair[0];
            let b = pair[1];
            graph.entry(a).or_insert(a);
            graph.entry(b).or_insert(b);

            graph.union(a, b);
        }

        // println!("{:?}", graph);

        let mut rootClusterMapping: HashMap<i32, HashSet<i32>> = HashMap::new();

        for k in graph.keys() {
            let root = graph.root(k); // 这里就是不能在root()里优化图的原因。因为如果要在root()里面优化图，必须传一个&mut self进去，可是for循环外面取了一次&self，这里会说不能同时取得可变和不可变引用
            let cluster = rootClusterMapping.entry(*root).or_insert(HashSet::new());
            cluster.insert(*k);
        }

        // println!("{:?}", rootClusterMapping);

        for cluster in rootClusterMapping.values() {
            let mut cluster: Vec<usize> = cluster.iter().map(|v| *v as usize).collect();
            cluster.sort();
            let mut charsInThisCluster: Vec<char> = cluster.iter().map(|i| string[*i]).collect();
            charsInThisCluster.sort();

            // println!("{:?}", charsInThisCluster);

            cluster
                .iter()
                .zip(charsInThisCluster.iter())
                .for_each(|(i, v)| {
                    *string.get_mut(*i).unwrap() = *v;
                });
        }

        let res: String = string.into_iter().collect();
        return res;
    }
}

pub fn main() {
    println!(
        "{:?}",
        Solution::smallest_string_with_swaps("dcab".to_string(), vec![vec![0, 3], vec![1, 2]])
    );
    println!(
        "{:?}",
        Solution::smallest_string_with_swaps(
            "dcab".to_string(),
            vec![vec![0, 3], vec![1, 2], vec![0, 2]]
        )
    );
}
