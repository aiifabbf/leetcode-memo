/*
.. default-role:: math

前 `k` 个最高频的元素

短平快的方法当然是直接一个Counter，然后按频次从大到小排序，取前 `k` 个就好了。这样复杂度是 `O(n \ln n)` 。

然而题目明确要求复杂度要低于 `O(n \ln n)` ，所以统计出每个元素出现的频次之后，不要整个都排序，因为万一每个元素都正好出现了一次，那么整个排序的复杂度就是 `O(n \ln n)` 了。

所以改成依次放入一个容量是 `k` 的最小heap里。heap里面存的东西是 ``(v, k)`` ，其中v是元素出现的次数、k是元素。

每次有一个 `(v, k)` 进去的时候，判断一下元素出现的次数和heap顶端元素出现的次数的大小关系。heap顶端元素是出现次数最少的元素。

每次有新元素要进heap之前，先看heap是不是满的，如果heap里面的元素个数不满 `k` ，那么只管放进去就好了。如果heap已经满了，那么要判断一下

-   如果这个新元素出现的次数都小于heap顶端元素出现的次数了，那么说明这个新元素根本没有任何可能进前 `k` 。
-   如果新元素出现的次数大于heap顶端元素出现的次数，那么说明heap顶端元素根本没可能进前 `k` ，直接把它pop掉，放入新元素就好了

最后再读出heap里的所有元素。
*/

struct Solution;

use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let count = k as usize;
        let mut counter = HashMap::new();

        for k in nums.iter() {
            *counter.entry(*k).or_insert(0) += 1;
        }

        let mut heap: BinaryHeap<(Reverse<usize>, i32)> = BinaryHeap::new(); // heap里存的是（元素出现的次数，元素），用Reverse的原因是rust的BinaryHeap默认是最大堆，而我们需要最小堆

        for (k, v) in counter.iter() {
            if heap.len() == count {
                // 如果heap满了
                if let Some(last) = heap.peek() {
                    // 和顶端元素出现的次数比较一下
                    let Reverse(frequency) = last.0;
                    if frequency < *v {
                        // 如果顶端元素出现的次数小于新元素
                        heap.pop(); // 直接pop掉顶端元素，它已经没机会进前k了
                        heap.push((Reverse(*v), *k)); // 放入新元素
                    }
                }
            } else {
                // 如果heap没满
                heap.push((Reverse(*v), *k)); // 只管放进去就好了
            }
        }

        return heap.into_iter().map(|v| v.1).collect();
    }
}

fn main() {
    // 突然发现了dbg这个宏，真方便啊
    dbg!(Solution::top_k_frequent(vec![1, 1, 1, 2, 2, 3,], 2));
    dbg!(Solution::top_k_frequent(vec![1], 1));
}
