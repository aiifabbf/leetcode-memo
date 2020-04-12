/*
区间求和，原数组可变。

还是用了前缀和/积分。听说标准做法是线段树……我还没学，学会了再来改。
*/

struct NumArray {
    integrals: Option<Vec<i32>>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumArray {
    fn new(nums: Vec<i32>) -> Self {
        if nums.is_empty() {
            return Self { integrals: None };
        } else {
            let integrals = vec![0]
                .into_iter()
                .chain(nums.into_iter().scan(0, |state, v| {
                    *state = state.clone() + v.clone();
                    return Some(*state);
                }))
                .collect();
            return Self {
                integrals: Some(integrals),
            };
        }
    }

    fn update(&mut self, i: i32, val: i32) {
        let i = i as usize;
        if let Some(integrals) = self.integrals.as_mut() {
            let origin = integrals[i + 1] - integrals[i];
            let delta = val - origin;

            for j in i + 1..integrals.len() {
                integrals[j] += delta;
            }
        }
    }

    fn sum_range(&self, i: i32, j: i32) -> i32 {
        let i = i as usize;
        let j = j as usize;
        if let Some(integrals) = self.integrals.as_ref() {
            return integrals[j + 1] - integrals[i];
        } else {
            return 0;
        }
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * let obj = NumArray::new(nums);
 * obj.update(i, val);
 * let ret_2: i32 = obj.sum_range(i, j);
 */
fn main() {
    let mut obj = NumArray::new(vec![1, 3, 5]);
    println!("{:?}", obj.sum_range(0, 2)); // 9
    obj.update(1, 2);
    println!("{:?}", obj.sum_range(0, 2)); // 8
}
