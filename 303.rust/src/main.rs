/* 
计算任意一段substring（要连续）的累加和

老生常谈了，积分/前缀和。
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
                    *state = *state + v;
                    return Some(*state);
                }))
                .collect();
            return Self {
                integrals: Some(integrals),
            };
        }
    }

    fn sum_range(&self, i: i32, j: i32) -> i32 {
        if self.integrals.is_some() {
            let integrals = self.integrals.as_ref().unwrap();
            return integrals[j as usize + 1] - integrals[i as usize];
        } else {
            return 0;
        }
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * let obj = NumArray::new(nums);
 * let ret_1: i32 = obj.sum_range(i, j);
 */
fn main() {
    let s = NumArray::new(vec![-2, 0, 3, -5, 2, -1]);
    println!("{:?}", s.sum_range(0, 2)); // 1
    println!("{:?}", s.sum_range(2, 5)); // -1
    println!("{:?}", s.sum_range(0, 5)); // 3
}
