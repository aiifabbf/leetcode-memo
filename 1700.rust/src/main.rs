/*
.. default-role:: math

有 `n` 个学生在食堂窗口前面排队， ``students[i]`` 是第 `i` 个学生喜欢的三明治种类；窗口里有 `n` 个三明治，第 `i` 个三明治的种类是 ``sandwiches[i]`` 。学生领三明治的流程是这样的：队伍最前面的学生如果发现窗口最前面不是他喜欢的三明治种类，他就会回到队伍的最后。问有多少个学生吃 **不** 到三明治？

既然是easy题，那么就直接暴力模拟就好了。
*/

struct Solution;

use std::collections::VecDeque;

impl Solution {
    pub fn count_students(students: Vec<i32>, sandwiches: Vec<i32>) -> i32 {
        let mut students: VecDeque<i32> = students.into_iter().collect(); // 因为频繁pop_front和pop_back，用VecDeque比较快
        let mut sandwiches: VecDeque<i32> = sandwiches.into_iter().collect();

        loop {
            let mut consumed = 0; // 这一轮有没有学生吃到三明治

            for _ in 0..students.len() {
                if students.front().unwrap() == sandwiches.front().unwrap() {
                    // 如果窗口最前面摆的正好是队伍最前面的学生喜欢的三明治
                    students.pop_front();
                    sandwiches.pop_front(); // 最前面的学生拿走了三明治
                    consumed += 1;
                    break;
                } else {
                    // 如果不是
                    students.rotate_left(1); // 最前面的学生走到队伍的最后面
                }
            }

            if consumed == 0 {
                // 如果这一轮没有学生吃到三明治
                return sandwiches.len() as i32; // 那么再来一轮情况也一样，这些学生根本就吃不到中饭
            }
        }
    }
}

fn main() {
    dbg!(Solution::count_students(
        vec![1, 1, 0, 0,],
        vec![0, 1, 0, 1]
    )); // 0
    dbg!(Solution::count_students(
        vec![1, 1, 1, 0, 0, 1],
        vec![1, 0, 0, 0, 1, 1]
    )); // 3
}
