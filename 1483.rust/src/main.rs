use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::VecDeque;

struct TreeAncestor {
    parents: HashMap<i32, i32>,
    cache: HashMap<i32, Vec<i32>>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TreeAncestor {
    fn new(n: i32, parent: Vec<i32>) -> Self {
        let mut parents: HashMap<i32, i32> = HashMap::new();
        let mut children: HashMap<i32, HashSet<i32>> = HashMap::new();
        let mut cache: HashMap<i32, Vec<i32>> = HashMap::new();

        for (i, v) in parent.into_iter().enumerate() {
            if v != -1 {
                parents.insert(i as i32, v);
                if let Some(targets) = children.get_mut(&v) {
                    targets.insert(i as i32);
                } else {
                    children.insert(v, [i as i32].iter().cloned().collect());
                }
            }
            cache.insert(i as i32, vec![]);
        }

        let mut queue = VecDeque::new();
        queue.push_back(0);

        while let Some(node) = queue.pop_front() {
            if let Some(parent) = parents.get(&node) {
                cache.get_mut(&node).unwrap().push(*parent);
                let mut i = 1;

                while i - 1 < cache[&cache[&node][i - 1]].len() {
                    let target = cache[&cache[&node][i - 1]][i - 1];
                    cache.get_mut(&node).unwrap().push(target);
                    i += 1;
                }
            }

            if let Some(v) = children.get(&node) {
                queue.extend(v.iter());
            }
        }

        return Self {
            parents: parents,
            cache: cache,
        };
    }

    fn get_kth_ancestor(&self, node: i32, k: i32) -> i32 {
        if node == -1 {
            return -1;
        } else if k == 0 {
            return node;
        } else if k == 1 {
            return self.parents.get(&node).cloned().unwrap_or(-1);
        } else {
            let step = 32 - k.leading_zeros() as i32 - 1;
            let modulo = k - 2_i32.pow(step as u32);
            if (step as usize) < self.cache[&node].len() {
                return self.get_kth_ancestor(self.cache[&node][step as usize], modulo);
            } else {
                return -1;
            }
        }
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * let obj = TreeAncestor::new(n, parent);
 * let ret_1: i32 = obj.get_kth_ancestor(node, k);
 */
fn main() {
    let obj = TreeAncestor::new(7, vec![-1, 0, 0, 1, 1, 2, 2]);
    dbg!(obj.get_kth_ancestor(3, 1)); // 1
    dbg!(obj.get_kth_ancestor(5, 2)); // 0
    dbg!(obj.get_kth_ancestor(6, 3)); // -1
}
