/*
有哪些文件内容相同？

按问题描述一步一步做就好了。就是从那个一长串字符串里提取目录名、文件名和内容有点麻烦。
*/

struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn find_duplicate(paths: Vec<String>) -> Vec<Vec<String>> {
        let mut fs: HashMap<String, String> = HashMap::new();
        for directory in paths.iter() {
            let mut iterator = directory.split(" ");
            let directoryName: String = iterator.next().unwrap().clone().to_string();

            for file in iterator {
                let mut iterator = file.split("(");
                let fileName: String = iterator.next().unwrap().clone().to_string();
                let content: Vec<char> = iterator.next().unwrap().chars().collect();
                let length = content.len();
                let content: String = content.into_iter().take(length - 1).collect();
                fs.insert(directoryName.clone() + "/" + &fileName, content);
            }
        }

        // println!("{:?}", fs);

        let mut contentFileNameMapping: HashMap<String, Vec<String>> = HashMap::new();

        for (k, v) in fs.into_iter() {
            contentFileNameMapping.entry(v).or_insert(vec![]).push(k);
        }

        let res: Vec<Vec<String>> = contentFileNameMapping
            .into_iter()
            .filter(|(k, v)| {
                if v.len() > 1 {
                    return true;
                } else {
                    return false;
                }
            })
            .map(|(k, v)| v)
            .collect();
        return res;
    }
}

pub fn main() {
    println!(
        "{:?}",
        Solution::find_duplicate(vec![
            "root/a 1.txt(abcd) 2.txt(efgh)".to_string(),
            "root/c 3.txt(abcd)".to_string(),
            "root/c/d 4.txt(efgh)".to_string(),
            "root 4.txt(efgh)".to_string(),
        ])
    );
}
