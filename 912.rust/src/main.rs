/*
.. default-role:: math

把常见的几个排序算法都实现一遍

我暂时写了合并排序、快速排序、计数排序。
*/

struct Solution;

impl Solution {
    // 我觉得最容易理解的合并排序，非常稳定，最优最坏情况都是n ln n，可惜需要额外空间
    // 也是存在不需要额外空间的做法的 <https://stackoverflow.com/questions/2571049/how-to-sort-in-place-using-the-merge-sort-algorithm>
    #[cfg(feature = "merge-sort")]
    pub fn sort_array(nums: Vec<i32>) -> Vec<i32> {
        match nums.len() {
            0 => vec![],
            // 空的话就啥也没有
            1 => nums,
            // 只有一个元素的话就是它本身
            2 => vec![*nums.iter().min().unwrap(), *nums.iter().max().unwrap()],
            // 只有两个元素的话就是两个里面排一下序
            _ => {
                // 大于两个元素的话，就拆成均等分的两部分，左右两边分别排序，然后再合并
                let left = Vec::from(&nums[..nums.len() / 2]);
                let right = Vec::from(&nums[nums.len() / 2..]);

                let left = Solution::sort_array(left);
                let right = Solution::sort_array(right);

                let mut a = &left[..];
                let mut b = &right[..];

                let mut res = vec![];

                while (!a.is_empty()) && (!b.is_empty()) {
                    // 比较两堆牌最前面的那张牌，取小的那张
                    if a[0] > b[0] {
                        res.push(b[0]);
                        b = &b[1..];
                    } else {
                        res.push(a[0]);
                        a = &a[1..];
                    }
                }

                if a.is_empty() {
                    res.extend(b.iter());
                } else {
                    res.extend(a.iter());
                }

                res
            }
        }
    }

    // 我觉得比较难理解的快速排序，不太稳定，最差情况复杂度是n^2，但是优势在于不需要额外空间
    #[cfg(feature = "quick-sort")]
    pub fn sort_array(nums: Vec<i32>) -> Vec<i32> {
        let mut array = nums;
        let length = array.len();
        Self::quickSort(&mut array[..]);
        return array;
    }

    fn quickSort<T>(array: &mut [T])
    where
        T: PartialOrd + Clone,
    {
        if !array.is_empty() {
            // 和合并排序差不多，也是做某件事，然后左右两边分别排序
            let p = Self::partition(array); // 这一步做的事情有两件，一是把选定的pivot放到正确的位置，此后便不再动pivot的位置，二是把所有比pivot小的数字放到pivot的左边、所有大于等于pivot的数字放到pivot的右边
            Self::quickSort(&mut array[..p]); // 然后分别对左右两边做同样的事情
            Self::quickSort(&mut array[p + 1..]);
        }
    }

    fn partition<T>(array: &mut [T]) -> usize
    where
        T: PartialOrd + Clone, // 能不能去掉Clone呢
    {
        let pivot = array.last().unwrap().clone(); // 取最后一个元素作为标杆

        // 这里我看了半天伪代码，发现就是和荷兰国旗 <https://en.wikipedia.org/wiki/Dutch_national_flag_problem> 问题一样的做法，详情可见75和283题
        let mut i = 0;
        let mut j = 0; // 下标在[i, j)区间内的元素都是大于等于pivot的元素

        while j < array.len() - 1 {
            if array[j] >= pivot {
                // 如果右边的元素大于等于pivot，那么直接纳入到水滴里来
                j += 1; // 继续往右看下一个元素
            } else {
                // 如果右边的元素小于pivot，那么让它和水滴最左边的元素交换，这样相当于水滴整体往右移动了一格
                array.swap(i, j);
                i += 1;
                j += 1;
            }
        }

        array.swap(i, array.len() - 1);

        // 下面是wiki <https://en.wikipedia.org/wiki/Quicksort> 上伪代码直接翻译过来的做法
        // let mut i = 0;

        // for j in 0..array.len() {
        //     if array[j] < pivot {
        //         array.swap(i, j);
        //         i += 1;
        //     } // 如果array[j] >= pivot，那就只动j
        // }

        // array.swap(i, array.len() - 1);

        return i;
    }

    #[cfg(feature = "counting-sort")]
    pub fn sort_array(nums: Vec<i32>) -> Vec<i32> {
        use std::collections::HashMap;

        let mut counter = HashMap::new();
        let mut min = std::i32::MAX;
        let mut max = std::i32::MIN;

        for v in nums.into_iter() {
            *counter.entry(v).or_insert(0) += 1;
            min = min.min(v);
            max = max.max(v);
        }

        let mut res = vec![];

        for k in min..max + 1 {
            if let Some(occurrence) = counter.get(&k) {
                res.extend([k].repeat(*occurrence));
            }
        }

        return res;
    }
}

fn main() {
    dbg!(Solution::sort_array(vec![5, 2, 3, 1]));
    dbg!(Solution::sort_array(vec![5, 1, 1, 2, 0, 0]));
}
