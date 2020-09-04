/*
.. default-role:: math

给一组左闭右开区间 `[a_i, b_i)` ，把他们合并起来。

比如给 `[1, 3), [2, 6), [8, 10), [15, 18)` 画成图大概是这样

::

    |----|
    1    3
       |-----|  |-----|    |-----|
       2     6  8     10   15    18

其中 `[1, 3)` 和 `[2, 6)` 可以合并成 `[1, 6)` ，所以合并之后结果是 `[1, 6), [8, 10), [15, 18)` 。

比如给 `[1, 4), [4, 5)` 要合并成 `[1, 5)` 。

不知道怎么就想到了排序和stack。可能是受到上面图的启发。先把区间按开始时间从小到大排序。然后依次放入stack

-   如果stack是空的，直接放进去就好了
-   如果stack不是空的，比较一下现在将要放进去的区间和stack顶的区间

    -   如果两个区间没有交集，还是直接放进去

        比如将要放入 `[2, 3)` ，而stack顶的区间是 `[1, 2)` ，两者没有交集，那么直接把 `[2, 3)` 放进去就好了。

    -   如果有交集，那么先pop、再取两个区间的并集、再放进stack

        比如将要放入 `[2, 4)` ，而stack顶的区间是 `[1, 3)` ，那么先pop，再取并集，变成 `[1, 4)` 再放入stack。

不知道怎么证明正确……我猜还是和数学归纳法一样的做法

-   stack为空是初始条件，如果只有一个区间，那么显然是对的
-   stack不为空表示的是假设第 `k` 步正确，现在进入第 `k + 1` 步，将要放入新的区间

    -   如果和stack顶端区间没有交集，那么放入绝对是正确的
    -   如果和stack顶端区间有交集，那么新加入的区间仅仅只会和stack顶端的区间有交集，而不会和前面的区间有交集，这是由排序保证的，将要放入的区间的开始时间不会比stack顶端的区间的开始时间早

        ::

            [   ) <- stack顶端之前的区间
                  [   ) <- stack顶端的区间
            -----------
                     [   ) <- 将要放入的区间

    所以假设第 `k` 步正确，第 `k + 1` 步按我们的做法仍然正确，所以正确。

不知道有没有疏漏。
*/

struct Solution;

impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut intervals: Vec<(i32, i32)> = intervals.into_iter().map(|v| (v[0], v[1])).collect();
        intervals.sort(); // 按开始时间从小到大排序
        let mut stack = vec![];

        for v in intervals.into_iter() {
            if stack.is_empty() {
                stack.push(v);
            } else {
                if stack.last().unwrap().1 < v.0 {
                    // 和stack顶端的区间没有交集
                    stack.push(v); // 直接放进去
                } else {
                    // 有交集
                    let mut merged = stack.pop().unwrap(); // 先pop
                    merged.0 = merged.0.min(v.0);
                    merged.1 = merged.1.max(v.1); // 再合并
                    stack.push(merged); // 再放入
                }
            }
        }

        return stack.into_iter().map(|v| vec![v.0, v.1]).collect();
    }
}

fn main() {
    dbg!(Solution::merge(vec![
        vec![1, 3],
        vec![2, 6],
        vec![8, 10],
        vec![15, 18],
    ])); // [[1, 6], [8, 10], [15, 18]]
    dbg!(Solution::merge(vec![vec![1, 4], vec![4, 5],])); // [[1, 5]]
    dbg!(Solution::merge(vec![vec![1, 4], vec![0, 0],])); // [[0, 0], [1, 4]]
}
