/*
.. default-role:: math

对于每个 `a[i]` ，找到它后面第一个比 `a[i]` 小或者相等的元素 `a[j]` 。如果能找到这个 `a[j]` ，那么 `res[i] = a[i] - a[j]` ；如果找不到，那么 `res[i] = a[i]` 。

老生常谈了，单调递减stack。这边因为需要做到比 `a[i]` 小、或者相等，所以是严格单调递减stack。
*/

struct Solution;

impl Solution {
    pub fn final_prices(prices: Vec<i32>) -> Vec<i32> {
        let mut firstLessIndices = vec![None; prices.len()]; // a[i]
        let mut stack = vec![];

        // stack建立的过程是反过来的，a[j]进来的过程中，才知道前面哪些a[i]可以做到 >= a[j]
        for (j, w) in prices.iter().enumerate() {
            while let Some(last) = stack.last().cloned() {
                // 这里还必须cloned，不然stack又有&又有& mut
                let (i, v) = last;
                if w <= v {
                    // a[j] <= a[i]
                    firstLessIndices[i] = Some(j); // 说明对于这个a[i]，找到了对应的a[j]
                    stack.pop(); // 既然已经找到了，就不需要留在stack里面了
                } else {
                    break;
                }
            }

            stack.push((j, w));
        }

        let mut res = vec![];

        for (i, v) in prices.iter().enumerate() {
            if let Some(j) = firstLessIndices[i] {
                // 后面存在一个a[j]小于a[i]
                res.push(*v - prices[j]);
            } else {
                // 不存在
                res.push(*v); // 那就只能原价购买了
            }
        }

        return res;
    }
}

fn main() {
    println!("{:?}", Solution::final_prices(vec![8, 4, 6, 2, 3])); // [4, 2, 4, 2, 3]
}
