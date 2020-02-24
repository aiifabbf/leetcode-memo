struct Solution;

use std::cmp::min;
use std::collections::HashMap;

impl Solution {
    pub fn find_smallest_region(
        regions: Vec<Vec<String>>,
        region1: String,
        region2: String,
    ) -> String {
        let region1: &str = &region1[..];
        let region2: &str = &region2[..];

        let mut tree: HashMap<&str, &str> = HashMap::new(); // 第一次用&str，好紧张

        for chain in regions.iter() {
            let mut chain = chain.iter(); // chain: Iterator<Item=&String>
            let node: &String = chain.next().unwrap();

            tree.entry(node).or_insert(node);

            for subregion in chain {
                tree.entry(subregion).or_insert(node); // 这里subregion的类型是&String，但是可以放到entry里，可能因为entry的key的类型是&str吧，如果是String那估计就不能放了
            }
        }
        // chain
        let mut chain1: Vec<&str> = vec![region1];
        let mut root: &str = &region1[..];

        while root != *tree.get(root).unwrap() {
            chain1.push(tree.get(root).unwrap());
            root = tree.get(root).unwrap();
        }

        chain1.reverse();

        let mut chain2: Vec<&str> = vec![region2];
        let mut root: &str = &region2[..];

        while root != *tree.get(root).unwrap() {
            chain2.push(tree.get(root).unwrap());
            root = tree.get(root).unwrap();
        }

        chain2.reverse();
        // diff
        for i in 0..min(chain1.len(), chain2.len()) {
            if chain1[i] != chain2[i] {
                return chain1[i - 1].to_string();
            }
        }

        if chain1.len() > chain2.len() {
            return chain2.last().unwrap().to_string();
        } else {
            return chain1.last().unwrap().to_string();
        }
    }
}

pub fn main() {
    println!(
        "{:?}",
        Solution::find_smallest_region(
            vec![
                vec![
                    "Earth".to_string(),
                    "North America".to_string(),
                    "South America".to_string()
                ],
                vec![
                    "North America".to_string(),
                    "United States".to_string(),
                    "Canada".to_string()
                ],
                vec![
                    "United States".to_string(),
                    "New York".to_string(),
                    "Boston".to_string()
                ],
                vec![
                    "Canada".to_string(),
                    "Ontario".to_string(),
                    "Quebec".to_string()
                ],
                vec!["South America".to_string(), "Brazil".to_string()],
            ],
            "Quebec".to_string(),
            "New York".to_string(),
        )
    ); // 这么多to_string()...有没有什么好方法
}
