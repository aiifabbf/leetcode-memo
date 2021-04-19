/*
.. default-role:: math

写最短处理时间进程调度模拟器。

啊啊啊上操作系统的时候写过这个，超级好玩。本质上是个discrete event simulator aka. 离散事件模拟器。离散的意思是，不是像帝国时代这种即时战略游戏一样、一帧一帧去模拟，每一帧计算下一帧场景上所有对象的状态，而是有一个优先队列，里面按事件的某种特性（比如开始时间）排序，每次从队列里抽出最前面的事件，处理事件，处理事件的过程中可能会产生更多未来的事件，继续放到队列里。

很多模拟器其实都是这种discrete event simulator，比如Verilog模拟器、路由模拟器、调度模拟器。就拿Verilog模拟器来说，可能最开始队列里面只有一个事件，就是电源电压从0到5V，从队列里抽出这个事件之后，会产生更多的事件发生，比如因为连线延迟，某一个MOS管可能要到10ps之后才会感受到电压变化、某个MOS管的输入端电压变高了之类的事情。

这道题是要写进程调度模拟器，并且钦定了实现最短处理时间模拟器。最短处理时间的意思是，每当CPU空闲下来，它都会从任务队列里找最快能完成的任务开始处理。在CPU忙碌的时候，可能有更多的任务出现了，并且被放到了任务队列里。

怎么用离散仿真来做这件事呢？先把所有的任务按出现的时间从早到晚排序，用一个优先队列来放当前CPU可见的任务，按任务处理所需时间从小到大排序。然后用一个变量来存当前时间。

为什么需要限定可见呢？因为站在CPU的角度来说，它在第10秒的时候并不知道第15秒会有一个新任务来，它只能看到第10秒刚刚进入队列、或者第10秒之前进入任务队列的任务。

当CPU空闲的时候，任务队列会有两种情况

-   有任务

    最好了，直接抽出优先队列顶端的任务，把当前时间设置成完成任务的时间，就是直接空降到这个任务完成的时间点。

    因为我们直接空降到任务完成的时间点了，这期间有可能有新的任务来，而我们可能不知道，所以我们要遍历一下时间轴，把这期间的出现的新任务加到队列里。

-   没任务

    说明CPU开始发呆了，我们要去看看未来有没有任务会进入队列，也是2种情况

    -   有任务

        太好了，直接空降到那个任务出现的时间点，然后把那个时间点出现的任务全加入到队列里。

    -   没任务

        CPU会永远空闲下去，仿真结束。
*/

struct Solution;

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn get_order(tasks: Vec<Vec<i32>>) -> Vec<i32> {
        let mut tasks: Vec<(usize, i32, i32)> = tasks
            .into_iter()
            .enumerate()
            .map(|(i, v)| (i, v[0], v[1]))
            .collect();
        tasks.sort_by_key(|v| v.1); // 时间轴按任务出现（就是对CPU可见）时间排序
        let mut futures = &tasks[..]; // 未来任务

        let mut queue = BinaryHeap::new(); // 任务队列，按任务处理时间、任务编号排序。因为Rust的heap是max heap，所以放的是Reverse
        let mut time = 0; // 当前时间
        let mut res = vec![]; // 处理事件的顺序

        loop {
            if let Some(Reverse((duration, i))) = queue.pop() {
                // 如果queue里有任务，从queue里取出用时最少的任务
                res.push(i); // 处理任务
                time = time + duration; // 空降到任务处理完成的那个时间点
            } else {
                // 如果queue里没有任务的话，有两种可能
                if let Some((i, enter, duration)) = futures.first().cloned() {
                    // 有可能下一任务还没来
                    time = enter; // 直接空降到下一个任务开始的时间点
                } else {
                    // 有可能任务已经全部处理完了
                    break; // 退出
                }
            }

            // 在处理任务的期间可能有新的任务来
            while let Some((i, enter, duration)) = futures.first().cloned() {
                if enter <= time {
                    // 把这期间出现的所有新任务都放到队列里
                    futures = &futures[1..];
                    queue.push(Reverse((duration, i)));
                } else {
                    break;
                }
            }
        }

        res.into_iter().map(|v| v as i32).collect()
    }
}

fn main() {
    dbg!(Solution::get_order(vec![
        vec![1, 2],
        vec![2, 4],
        vec![3, 2],
        vec![4, 1],
    ]));
    dbg!(Solution::get_order(vec![
        vec![7, 10],
        vec![7, 12],
        vec![7, 5],
        vec![7, 4],
        vec![7, 2],
    ]));
}
