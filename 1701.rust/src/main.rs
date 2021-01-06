/*
.. default-role:: math

给个array， ``array[i][0]`` 是第 `i` 个顾客下单的时间， ``array[i][1]`` 是做完第 `i` 个顾客点的菜的时间。饭店里只有一个厨师。问每个顾客等待的平均时间是多少。

哇这题很有意思，我想到了上操作系统实验的时候用过的那个 `discrete event simulator <https://en.wikipedia.org/wiki/Discrete-event_simulation>`_ ，用来仿真不同的进程调度算法。这题也可以看作是仿真first come first serve调度算法。

用 ``now`` 表示当前时间，然后按顾客下单时间从早到晚，遍历每个顾客的订单

-   如果 ``now`` 小于等于顾客下单的时间，说明在顾客下单的瞬间厨师是空闲的，可以立刻开始做这个顾客点的菜，那么当前这个顾客只要等菜做完就可以了，所以当前顾客等待的时间就是做菜的时间。时间点跳到菜做完的瞬间
-   如果 ``now`` 大于顾客下单的时间，说明这个顾客来的时间不巧，厨师正在忙别的事，厨师将在 ``now`` 这个时间点忙完手里的事情，然后才可以开始做这个顾客点的菜品。所以当前顾客等待的时间不止是做菜的时间，还有之前等厨师的时间。时间点同样跳到菜做完的瞬间
*/

struct Solution;

impl Solution {
    pub fn average_waiting_time(customers: Vec<Vec<i32>>) -> f64 {
        let mut now: u64 = 0; // 当前时间
        let mut waited: u64 = 0; // 所有顾客总共等了多少时间
        let length = customers.len(); // 平均等待时间是所有顾客总共等待的时间除以顾客的数量

        for v in customers.into_iter() {
            let start = v[0] as u64; // 顾客下单的时间
            let duration = v[1] as u64; // 做顾客叫的这道菜需要花多少时间
            if now <= start {
                // 如果当前时间小于等于顾客下单的时间，说明在这个顾客下单的时候厨师是空闲的
                now = start + duration; // 厨师可以立刻开始做这个顾客点的菜，做完这道菜之后的时间是start + duration
                waited += duration; // 顾客还是至少要等厨师做完这道菜
            } else {
                // 说明顾客来的时候，厨师在忙着做别的菜，没办法立刻做这个顾客的菜。厨师要到now这个时间点才会空闲
                waited += now - start; // 等厨师忙完手里的菜
                now += duration; // 然后厨师才能开始做现在这个顾客点的菜
                waited += duration;
            }
        }

        return waited as f64 / length as f64;
    }
}

fn main() {
    dbg!(Solution::average_waiting_time(vec![
        vec![1, 2],
        vec![2, 5],
        vec![4, 3],
    ])); // 5
    dbg!(Solution::average_waiting_time(vec![
        vec![5, 2],
        vec![5, 4],
        vec![10, 3],
        vec![20, 1],
    ])); // 3.25
}
