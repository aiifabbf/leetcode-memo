/*
排列组合的下一个组合，按字典序。

比如给 ``1, 2, 3`` 下一个组合是 ``1, 3, 2`` 。

这个题不知道套路的完全不知道怎么做。 `Python的标准库是这么实现的 <https://docs.python.org/3.7/library/itertools.html#itertools.permutations>`_ ， `维基百科上也有 <https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order>`_ 算法。还是个14世纪的人发现的……

一共4步

1.  从右往左，找到第一个满足 `a_i < a_{i + 1}` 的 `i`

    如果找不到，说明数组是递减的，已经是字典序最大的组合了，比如 ``3, 2, 1`` 。这时候把整个数组颠倒一下就好了。

2.  再从右往左，找到第一个满足 `a_i < a_j` 的 `j`
3.  交换 `a_i, a_j` 的值
4.  再把 `i + 1` 以右的substring整个颠倒
*/

struct Solution;

impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        let mut index = None; // 可能找不到满足a[i] < a[i + 1]的i，所以用一个Option

        for i in (1..nums.len()).rev() {
            // 从右往左找到第一个满足a[i] < a[i + 1]的i
            if nums[i - 1] < nums[i] {
                index.replace(i - 1);
                break;
            }
        }

        if index.is_none() {
            // 没找到这样的i
            nums.reverse(); // 整个颠倒
            return;
        }

        let index1 = index.unwrap();
        let mut index2 = index1 + 1;

        for i in (0..nums.len()).rev() {
            // 从右往左找到第一个满足a[i] < a[j]的j
            if nums[i] > nums[index1] {
                index2 = i;
                break;
            }
        }

        nums.swap(index1, index2); // 交换a[i]和a[j]
        &nums[index1 + 1..].reverse(); // 颠倒从i + 1开始的substring
        return;
    }
}

fn main() {
    let mut a = vec![1, 2, 3];
    Solution::next_permutation(&mut a);
    println!("{:?}", a); // 1, 3, 2
}
