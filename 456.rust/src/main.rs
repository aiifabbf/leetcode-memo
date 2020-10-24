/*
.. default-role:: math

给个array，问存不存在 `i < j < k` 使得 `a_j > a_k > a_i` 。

比如给个 ``1, 3, 2`` ，存在的。

暴力做法是穷举每个三元组，复杂度是 `O(C_n^3) = O(n^3)` 。

看了一大圈评论区，实在是没看懂 `O(n)` 的做法，自己想了个 `O(n \ln n)` 的做法，很好理解（我觉得）。

对于每个 `j` ，在 `j` 的右侧找比 `a_j` 小的、最大的数字作为 `a_k` ，再看 `j` 的左侧存不存在比 `a_k` 小的数字。

为什么要在 `j` 的右侧找比 `a_j` 小的数字呢？因为要满足 `a_j > a_k` 。那么为什么要找最大的比 `a_j` 小的数字呢？这样才能使得 `j` 左侧更有可能存在比 `a_k` 小的数字。

比如

::

    2 5 3 1
      j

现在 `j = 1, a_j = 5` ，在 `j` 的右侧有3和1，都比5小，按理说都能作为 `a_k` ，但是如果选了1作为 `a_k` ，那么 `j` 的左侧就找不到比 `a_k` 的数字了。

剩下的问题就是选择一个牛逼的数据结构，能迅速在 `j` 的右侧找到小于 `a_j` 的最大数字、能判断在 `j` 的左侧存不存在比 `a_k` 小的数字。

立刻就想到了二分搜索树这一族的数据结构。hash set显然不合适，因为没有顺序信息；array看上去挺合适的，但是每次我们看向下一个 `j` 的时候，都要从array里删掉 `a_j` ，这个开销挺大的。

所以大概的做法是这样，维护两个B tree map（rust提供了 ``BTreeMap`` ，很方便）作为counter，分别叫 ``before`` 和 ``after`` ， ``before`` 里面存 ``a[..j]`` 的直方图， ``after`` 里面存 ``a[j + 1..]`` 的直方图。

对每个 `j` ，都先去 ``after`` 里找小于 `a_j` 的最大的数字，记为 `a_k` 。再去 ``before`` 里找小于 `a_k` 的数字。

还是用上面的例子，假设现在 `j = 1, a_j = 5` ，那么

::

    before == {
        2: 1, // 2出现了一次
    }

    after == {
        3: 1,
        1: 1,
    }

用二分搜索树族数据结构的性质，在 ``after`` 里找到比5小的最大的数字复杂度是 `O(\ln n)` ，之后再去 ``before`` 里找比3小的数字复杂度也是 `O(\ln n)` 。又因为我们对每个 `j` 都要这么做，所以总的复杂度是 `O(n \ln n)` 。
*/

struct Solution;

use std::collections::BTreeMap;

impl Solution {
    pub fn find132pattern(nums: Vec<i32>) -> bool {
        let mut before = BTreeMap::new(); // 当前j的右侧（不包括第j个数字本身）的数字的直方图，也就是a[j + 1..]的直方图
        let mut after = BTreeMap::new(); // 当前j的左侧（不包括第j个数字本身）的数字的直方图，也就是a[..j]的直方图

        // 先更新after。初始的after就是整个array的直方图
        for v in nums.iter() {
            *after.entry(*v).or_insert(0) += 1;
        }

        for b in nums.into_iter() {
            // 对于每个j
            // 因为我们要去j的右侧、也就是a[j + 1..]里找比a[j]小的最大的数字，所以先把a[j]从after里面删掉
            match after.get_mut(&b) {
                Some(count) => {
                    if *count > 1 {
                        *count -= 1;
                    } else {
                        // 如果之前出现次数正好是1，那么减去一次变成0了
                        after.remove(&b); // 那就直接删掉
                    }
                }
                _ => {}
            }
            // 这样after就是a[j + 1..]的直方图了

            if let Some((c, _)) = after.range(..b).rev().next() {
                // 先去a[j + 1..]里找小于a[j]的最大的数字。如果存在的话，记为a[k]
                // .rev()是因为.range()返回的迭代器是从小到大排序的。幸好这个迭代器是双端迭代器，好贴心
                if before.range(..c).next().is_some() {
                    // 再去a[..j]里看存不存在小于a[k]的数字
                    return true;
                }
            }

            *before.entry(b).or_insert(0) += 1; // 更新下a[..j]的直方图下一轮用，把a[j]加进来
        }

        return false;
    }
}

fn main() {
    dbg!(Solution::find132pattern(vec![1, 2, 3, 4])); // false
    dbg!(Solution::find132pattern(vec![3, 1, 4, 2])); // true
    dbg!(Solution::find132pattern(vec![-1, 3, 2, 0])); // true
    dbg!(Solution::find132pattern(vec![1, 0, 1, -4, -3])); // false
    dbg!(Solution::find132pattern(vec![3, 5, 0, 3, 4])); // true
}
