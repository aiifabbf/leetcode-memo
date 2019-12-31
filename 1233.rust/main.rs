struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn remove_subfolders(folder: Vec<String>) -> Vec<String> {
        let mut folders: Vec<Vec<&str>> = folder.iter()
            .map(|v| {
                let dir: Vec<&str> = v.split("/") // split返回一个Iterator<&str>
                    .skip(1) // 跳过第一个空字符串
                    .collect();
                return dir;
            })
            .collect(); // 把目录从/a/b/c这种拆成a, b, c
        folders.sort(); // 按字典序排序
        let mut seen: HashSet<Vec<&str>> = HashSet::new();

        for folder in folders.iter() { // folder: &Vec<&str>
            let mut broken: bool = false;

            for i in 1..folder.len() {
                if seen.contains(&folder[..i].to_vec()) { // 这里的类型推断不太理解，因为folder是Vec<&str>，所以取切片之后&folder[..i]应该是&[&str]，可是上面seen的类型明明是HashSet<Vec<&str>>，所以一个&[&str]是怎么变成Vec<&str>的呢
                    broken = true; // rust没有python那样的for...else语法，所以只能用一个flag变量来判断是break退出for的还是for自然退出
                    break;
                }
            }
            
            if broken == false { // 如果是for自然退出，说明这个目录是一个主目录
                seen.insert(folder.clone()); // 加入hash set
            }
        }

        let res: Vec<String> = seen.iter()
            .map(|v| { // 这里的v是&Vec<&str>
                format!("{}{}", "/", v.join("/")) // format返回一个String
            })
            .collect(); // 我真的太讨厌rust的generic method的写法了，为什么要::<>这样
        return res;
    }
}

pub fn main() {
    println!("{:?}", Solution::remove_subfolders(vec!["/a","/a/b","/c/d","/c/d/e","/c/f"].iter().map(|v| { v.to_string() }).collect()));
}