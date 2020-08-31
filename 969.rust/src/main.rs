/*
.. default-role:: math

给一个array，每次只能选择一个 `i` 然后翻转 ``array[..i]`` ，问每一步选择哪个 `i` 才能最后把array排好序？

比如给 ``3, 2, 4, 1`` ，可以

#.  选择2，翻转 ``3, 2`` ，array变成 ``2, 3, 4, 1``
#.  选择3，翻转 ``2, 3, 4`` ，array变成 ``4, 3, 2, 1``
#.  选择4，翻转 ``4, 3, 2, 1`` ，array变成 ``1, 2, 3, 4``

这样好像没法总结出什么规律。不如这样考虑，翻转可以做成什么事情？排序要做的事情是什么？

对于选择排序来说，每一步要做的事情是挑出array里最大的那个数，放到array的最后，然后那个数就固定在那里不会再动了。

那么这件事能不能用这个奇怪的pancake翻转来实现呢？可以的，还是 ``3, 2, 4, 1``

#.  整个array里最大的数字是4，那么先翻转 ``3, 2, 4`` ，array变成 ``4, 2, 3, 1`` ，再翻转 ``4, 2, 3, 1`` ，array变成 ``1, 3, 2, 4`` ，这样我们成功把最大的数字放到array最后去了，从此4的位置不会再改变了，它就一直待在那里
#.  那么除了4以外最大的数字是啥呢？是3，所以先翻转 ``1, 3`` ，变成 ``3, 1, 2, 4`` ，然后翻转 ``3, 1, 2`` ，变成 ``2, 1, 3, 4`` ，又一次把最大的数字放到了最终位置
#.  同理剩下的是2，这次发现不用翻转 ``2`` ，因为翻转 ``array[..1]`` 没效果，所以直接翻转 ``2, 1`` ，array变成 ``1, 2, 3, 4``
#.  剩下1，还是不用翻转

所以利用pancake翻转来排序的一种做法（当然肯定不是最优的方法）是

#.  找到 ``array[..i]`` 里的最大值，假设是 ``array[j]`` ，那么翻转 ``array[..j + 1]`` ，这样可以把最大值翻转到array的最前面
#.  翻转 ``array[..i]`` ，这样最大值被翻转到了 `i - 1` 这个位置
#.  递归地对 ``array[..i - 1]`` 做同样的事情
*/

struct Solution;

impl Solution {
    pub fn pancake_sort(a: Vec<i32>) -> Vec<i32> {
        let mut steps = vec![];
        let mut array = a;
        Self::swap(&mut array[..], &mut steps);
        return steps.into_iter().map(|v| v as i32).collect();
    }

    fn swap(array: &mut [i32], steps: &mut Vec<usize>) {
        if array.is_empty() {
            return;
        }

        let index = (0..array.len()).max_by_key(|i| array[*i]).unwrap_or(0); // 找到array[..i]里最大值的下标
        if index != array.len() - 1 {
            // 翻转array[..j + 1]，把最大值翻到array[..i]最前面
            steps.push(index + 1);
            &array[..index + 1].reverse();

            // 再翻转array[..i]，把最大值翻到array[..i]最后面
            steps.push(array.len());
            array.reverse();
        } // 如果最大值已经在i - 1了，不需要翻转

        let length = array.len();
        Self::swap(&mut array[..length - 1], steps); // 对array[..i - 1]做同样的事情
    }
}

fn main() {
    dbg!(Solution::pancake_sort(vec![3, 2, 4, 1]));
    dbg!(Solution::pancake_sort(vec![1, 3, 2]));
}
