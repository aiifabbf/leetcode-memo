/*
.. default-role:: math

给个叫 ``seats`` 的array， ``seat[i] == 1`` 表示第 `i` 个座位上有人。要坐的离两边的人尽可能远，问离最近的人最远的距离是多少。

比如总共有7个座位

::

    0, 1, 2, 3, 4, 5, 6
    1, 0, 0, 0, 1, 0, 1

如果坐在2上，离两边的人最远，距离是2。

挺简单的，先把 ``seats`` 这个array转换一下，变成记录有人的座位的array，比如上面的 ``1, 0, 0, 0, 1, 0, 1`` 经过转换变成 ``0, 4, 6`` ，表示这几个座位上有人。

然后扫描长度为2的窗口

1.  扫描 ``0, 4`` ，发现中间可以坐人，和两边的最大距离是2
2.  扫描 ``4, 6`` ，发现中间可以坐人，和两边的最大距离是2

最后不要忘了，有可能0和6上没人，这时候会出现只有一边有人的情况。比如

::

    0, 1, 2, 3, 4, 5, 6
    0, 0, 0, 0, 1, 0, 0

特殊处理一下就好了。
*/

struct Solution;

impl Solution {
    pub fn max_dist_to_closest(seats: Vec<i32>) -> i32 {
        let count = seats.len();
        let occupied: Vec<usize> = seats
            .into_iter()
            .enumerate()
            .filter(|(i, v)| *v == 1)
            .map(|(i, v)| i)
            .collect(); // 把有人的座位记下来

        return occupied
            .windows(2) // 摘取长度为2的窗口
            .map(|v| (v[1] - v[0]) / 2) // 坐在正中的位置
            .max()
            .unwrap_or(0)
            .max(occupied.first().cloned().unwrap_or(0)) // 如果第一个人不是坐在0座位上，那么我应该坐在0座位上，可以离第一个人最远
            .max(count - 1 - occupied.last().cloned().unwrap_or(count - 1)) as i32;
        // 如果最后一个人不是坐在最后一个座位上，那么我应该坐在最后一个座位上，这样可以离最后一个人最远
    }
}

fn main() {
    dbg!(Solution::max_dist_to_closest(vec![1, 0, 0, 0, 1, 0, 1])); // 2
    dbg!(Solution::max_dist_to_closest(vec![1, 0, 0, 0])); // 3
    dbg!(Solution::max_dist_to_closest(vec![0, 1])); // 1
}
