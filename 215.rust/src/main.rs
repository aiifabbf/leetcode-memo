/*
.. default-role:: math

给一个乱序的array，找到第 `k` 大的数字

最简单的当然是排个序，直接定位到第 `k` 大的数字，复杂度是 `O(n \ln n)` 。

有更快的方法，叫quick select <https://en.wikipedia.org/wiki/Quickselect> ，是快速排序的修改版，运气好的话，可以在数列还没有完全排好的时候就直接得到第 `k` 大的数字。

回顾一下快速排序的过程，因为要找第 `k` 大的数字，那这边就看从大到小排序的过程

1.  选取一个基准数字 ``pivot``
2.  扫描一遍，用荷兰国旗算法完成4件事情

    -   得到一个 ``index`` ，这个 ``index`` 左边的substring ``a[..index]`` 里每个数字都大于等于 ``pivot``
    -   ``index + 1`` 右边的substring ``a[index + 1..]`` 每个数字都小于 ``pivot``
    -   ``a[index]`` 正好就等于基准数字
    -   基准数字的位置以后都不会再改变，永远都是 ``index``

3.  对左半边substring ``a[..index]`` 递归一下
4.  对右半边substring ``a[index + 1..]`` 递归一下

所以可以利用“基准数字在最终array里的位置不再变化”这个性质来写。如果扫描一遍之后，基准数字的位置正好就是 `k` ，那么皆大欢喜，基准数字就是第 `k` 大的数字。

运气不好的话， `k` 可能小于基准数字的位置，或者大于基准数字的位置。也就是说，第 `k` 大数字可能出现在 ``a[..index]`` 里，或者出现在 ``a[index + 1..]`` 里。这时候就要再去左半边或者右半边找。

-   如果在左半边，那很好办，还是找 ``a[..index]`` 里第 `k` 大的数字
-   如果在右半边，就不是 ``a[index + 1..]`` 里第 `k` 大的数字了，因为通过这一遍荷兰国旗算法，前 ``index + 1`` 大的数字都已经确定了，前 ``index + 1`` 个最大的数字正好就是 ``a[..index + 1]`` 。所以这时候应该去右半边找右半边的第 `k - (i + 1)` 大的数字

.. 猿辅导面试被问了这个题，我还根本不知道有quick select这个玩法。
*/

struct Solution;

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = nums;
        let k = k as usize - 1; // 题目给的k是从1开始的，改成从0开始
        return Self::kthLargest(&mut nums[..], k);
    }

    fn kthLargest(array: &mut [i32], k: usize) -> i32 {
        if array.len() == 0 {
            return 0;
        } else {
            let pivot = array[array.len() - 1]; // 随便选取一个基准数字
            let mut left = 0; // 然后开始荷兰国旗算法
            let mut right = 0;

            while right != array.len() - 1 {
                if array[right] >= pivot {
                    array.swap(left, right);
                    left += 1;
                    right += 1;
                } else {
                    right += 1;
                }
            }

            array.swap(left, array.len() - 1);
            // 到这里，我们能保证四件事情：left左边所有的数字都是大于等于基准数字的，array[left]正好就等于基准数字，left + 1的右边都是小于基准数字的，基准数字的位置在最终排好序的数字里已经确定是left、不会再变化了

            if k == left {
                // 所以如果运气好，基准数字的最终位置正好是k
                return pivot; // 那第k大的数字就是基准数字
            } else if k < left {
                // 不巧，第k大的数字还在前面一半
                return Self::kthLargest(&mut array[..left], k); // 那就继续找
            } else {
                // 第k大的数字在后面一半
                return Self::kthLargest(&mut array[left + 1..], k - (left + 1));
                // 去后面找后面半部分里第k - (left + 1)大的数字
            }
        }
    }
}

fn main() {
    dbg!(Solution::find_kth_largest(vec![3, 2, 1, 5, 6, 4], 2)); // 5
    dbg!(Solution::find_kth_largest(
        vec![3, 2, 3, 1, 2, 4, 5, 5, 6],
        4
    )); // 4
}
