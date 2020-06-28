struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::VecDeque;

impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let mut ins = HashMap::new();
        let mut outs = HashMap::new();

        for v in prerequisites.iter() {
            outs.entry(v[1]).or_insert(HashSet::new()).insert(v[0]);
            ins.entry(v[0]).or_insert(HashSet::new()).insert(v[1]);
        }

        let mut queue: VecDeque<i32> = (0..num_courses)
            .filter(|v| ins.get(v).map(|w| w.len()).unwrap_or(0) == 0)
            .collect();
        let mut traveled = HashSet::new();

        while let Some(node) = queue.pop_front() {
            for v in outs.get(&node).unwrap_or(&HashSet::new()).iter() {
                ins.get_mut(v).map(|w| w.remove(&node));

                if ins.get(v).map(|w| w.len()).unwrap_or(0) == 0 {
                    queue.push_back(*v);
                }
            }

            traveled.insert(node);
        }

        return traveled.len() == num_courses as usize;
    }
}

fn main() {
    println!(
        "{:#?}",
        Solution::can_finish(
            8,
            vec![
                vec![1, 0],
                vec![2, 6],
                vec![1, 7],
                vec![6, 4],
                vec![7, 0],
                vec![0, 5]
            ]
        )
    ); // true
}
