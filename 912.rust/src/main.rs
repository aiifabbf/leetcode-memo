/*
.. default-role:: math

把常见的几个排序算法都实现一遍

我暂时写了合并排序、快速排序、计数排序。

人算不如天算，面拼多多被问了heap sort，没写出来很尴尬。痛定思痛，终于花了一上午搞懂了。
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

    // 堆排序
    #[cfg(feature = "heap-sort")]
    pub fn sort_array(nums: Vec<i32>) -> Vec<i32> {
        // heap sort分两步，第一步是把array变成heap。有max heap和min heap之分。所谓max heap就是这样一个树，对于其中任意一个节点，节点的值都大于等于它任意一个子节点的值
        let mut array = nums;
        Self::heapify(&mut array); // 原地把array变成max heap

        // 第二步是不停抽取max heap的顶端元素，也就是array[0]，放到array的后面。第i次抽取的元素放到array.len() - i - 1处，比如第0次抽取的正好就是整个array里最大数，所以放到array.len() - 1处。
        for i in (0..array.len()).rev() {
            array.swap(i, 0); // 用交换来实现pop max heap顶端元素。此时heap的范围从array[0..i + 1]变成了array[0..i]并且可能不再满足heap的性质了
            Self::sink(&mut array[..i], 0); // 所以要把新来的顶端元素下沉放到正确的位置，以维持array[0..i]作为heap的约束
        }

        return array;
    }

    // 把array原地变成最大堆
    fn heapify<T>(array: &mut [T])
    where
        T: PartialOrd,
    {
        // heapify的过程其实就是已有一个heap、加入新元素、把新元素上浮到正确的位置以保证heap的性质的过程
        // 空array自身就是个heap，所以array[0..0]本身就是个heap，第一步是要把array[0]纳入到array[0..0]这个heap里，形成新的heap，使得array[0..1]仍然保持heap的性质
        for i in 0..array.len() {
            // 把第i个数加入到heap里
            Self::swim(array, i);
        }
    }

    // 把节点上浮直到达到顶端、或者父节点的值大于等于这个节点的值
    fn swim<T>(heap: &mut [T], index: usize)
    where
        T: PartialOrd,
    {
        let mut index = index;

        // 把一个节点向上移动，移到正确的位置为止
        while index != 0 && heap[index] > heap[(index - 1) / 2] {
            heap.swap(index, (index - 1) / 2);
            index = (index - 1) / 2;
        }
    }

    // 把节点下沉到底、或者大于等于两个子节点为止
    fn sink<T>(heap: &mut [T], index: usize)
    where
        T: PartialOrd,
    {
        let mut index = index;

        // 把一个节点往下移动，移到正确的位置为止
        while index < heap.len() {
            match (heap.get(index * 2 + 1), heap.get(index * 2 + 2)) {
                (Some(left), Some(right)) => {
                    // 两个子节点都存在的情况
                    let child = if left > right {
                        index * 2 + 1
                    } else {
                        index * 2 + 2
                    }; // 取大的那个节点的下标
                    if &heap[index] < &heap[child] {
                        heap.swap(index, child);
                        index = child;
                    } else {
                        // 大于等于大的那个子节点，所以大于等于两个子节点，所以到位了
                        break;
                    }
                }
                (Some(left), None) => {
                    // 只存在左边节点的情况
                    if &heap[index] < left {
                        heap.swap(index, index * 2 + 1);
                        index = index * 2 + 1;
                    } else {
                        break;
                    }
                }
                (None, Some(right)) => {
                    // 只存在右边节点的情况
                    if &heap[index] < right {
                        heap.swap(index, index * 2 + 2);
                        index = index * 2 + 2;
                    } else {
                        break;
                    }
                }
                _ => {
                    break;
                }
            }
        }
    }
}

fn main() {
    dbg!(Solution::sort_array(vec![5, 2, 3, 1]));
    dbg!(Solution::sort_array(vec![5, 1, 1, 2, 0, 0]));
    dbg!(Solution::sort_array(vec![
        -4, 0, 7, 4, 9, -5, -1, 0, -7, -1
    ]));
}
